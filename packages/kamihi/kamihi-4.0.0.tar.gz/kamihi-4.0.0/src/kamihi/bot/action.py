"""
Action helper class.

License:
    MIT

"""

from __future__ import annotations

import inspect
from collections.abc import Callable
from pathlib import Path
from typing import Annotated, Any, get_args, get_origin

import loguru
from jinja2 import Environment, FileSystemLoader, Template, select_autoescape
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm import Session
from telegram import Update
from telegram.constants import BotCommandLimit
from telegram.ext import ApplicationHandlerStop, CallbackContext, CommandHandler

from kamihi.db import RegisteredAction, get_engine
from kamihi.tg import send
from kamihi.tg.handlers import AuthHandler
from kamihi.users import get_user_from_telegram_id

from .utils import COMMAND_REGEX


class Action:
    """
    Action class for Kamihi bot.

    This class provides helpers for defining actions, their commands and their handlers.

    Attributes:
        name (str): The name of the action.
        commands (list[str]): List of commands associated.
        description (str): Description of the action.

    """

    name: str
    commands: list[str]
    description: str

    _func: Callable
    _valid: bool = True
    _logger: loguru.Logger
    _templates: Environment

    def __init__(self, name: str, commands: list[str], description: str, func: Callable) -> None:
        """
        Initialize the Action class.

        Args:
            name (str): The name of the action.
            commands (list[str]): List of commands associated.
            description (str): Description of the action.
            func (Callable): The function to be executed when the action is called.

        """
        self.name = name
        self.commands = commands
        self.description = description

        self._func = func
        self._logger = logger.bind(action=self.name)

        self._validate_commands()
        self._validate_function()

        if not self.is_valid():
            self._logger.warning("Failed to register")
            return

        self.save_to_db()

        self._templates = Environment(
            loader=FileSystemLoader(Path(self._func.__code__.co_filename).parent),
            autoescape=select_autoescape(default_for_string=False),
        )

        self._logger.debug("Successfully registered")

    def _validate_commands(self) -> None:
        """Filter valid commands and log invalid ones."""
        min_len, max_len = BotCommandLimit.MIN_COMMAND, BotCommandLimit.MAX_COMMAND

        # Remove duplicate commands
        self.commands = list(set(self.commands))

        # Filter out invalid commands
        for cmd in self.commands.copy():
            if not COMMAND_REGEX.match(cmd):
                self._logger.warning(
                    "Command '/{cmd}' was discarded: "
                    "must be {min_len}-{max_len} chars of lowercase letters, digits and underscores",
                    cmd=cmd,
                    min_len=min_len,
                    max_len=max_len,
                )
                self.commands.remove(cmd)

        # Mark as invalid if no commands are left
        if not self.commands:
            self._logger.warning("No valid commands were given")
            self._valid = False

    def _validate_function(self) -> None:
        """Validate the function passed."""
        # Check if the function is a coroutine
        if not inspect.iscoroutinefunction(self._func):
            self._logger.warning(
                "Function should be a coroutine, define it with 'async def {name}()' instead of 'def {name}()'.",
                name=self._func.__name__,
            )
            self._valid = False

        # Check if the function has valid parameters
        parameters = inspect.signature(self._func).parameters
        if any(
            param.kind in (inspect.Parameter.VAR_POSITIONAL, inspect.Parameter.VAR_KEYWORD)
            for param in parameters.values()
        ):
            self._logger.warning(
                "Special arguments '*args' and '**kwargs' are not supported in action"
                " parameters, they will be ignored. Beware that this may cause issues."
            )
            self._valid = False

    @property
    def handler(self) -> AuthHandler:
        """Construct a CommandHandler for the action."""
        return AuthHandler(CommandHandler(self.commands, self.__call__), self.name) if self.is_valid() else None

    def is_valid(self) -> bool:
        """Check if the action is valid."""
        return self._valid

    def save_to_db(self) -> None:
        """Save the action to the database."""
        with Session(get_engine()) as session:
            sta = select(RegisteredAction).where(RegisteredAction.name == self.name)
            existing_action = session.execute(sta).scalars().first()
            if existing_action:
                existing_action.description = self.description
                session.add(existing_action)
                self._logger.trace("Updated action in database")
            else:
                session.add(RegisteredAction(name=self.name, description=self.description))
                self._logger.trace("Added action to database")
            session.commit()

    @classmethod
    def clean_up(cls, keep: list[str]) -> None:
        """Clean up the action from the database."""
        with Session(get_engine()) as session:
            statement = select(RegisteredAction).where(RegisteredAction.name.not_in(keep))
            actions = session.execute(statement).scalars().all()
            for action in actions:
                session.delete(action)
            session.commit()

    # skipcq: PY-R1000
    async def __call__(self, update: Update, context: CallbackContext) -> None:  # noqa: C901
        """Execute the action."""
        if not self.is_valid():
            self._logger.warning("Not valid, skipping execution")
            return

        self._logger.debug("Executing")

        pos_args = []
        keyword_args = {}

        for name, param in inspect.signature(self._func).parameters.items():
            match name:
                case "update":
                    value = update
                case "context":
                    value = context
                case "logger":
                    value = self._logger
                case "user":
                    value = get_user_from_telegram_id(update.effective_user.id)
                case "templates":
                    value = {
                        name: self._templates.get_template(name)
                        for name in self._templates.list_templates(extensions=".jinja")
                    }
                case s if s.startswith("template"):
                    if get_origin(param.annotation) is Annotated:
                        args = get_args(param.annotation)
                        if len(args) == 2 and args[0] is Template and isinstance(args[1], str):
                            value = self._templates.get_template(args[1])
                        else:
                            self._logger.warning(
                                "Invalid Annotated arguments for parameter '{name}'",
                                name=name,
                            )
                            value = None
                    else:
                        value = self._templates.get_template(f"{self.name}.md.jinja")
                case _:
                    self._logger.warning(
                        "Parameter '{name}' is not supported, it will be set to None",
                        name=name,
                    )
                    value = None

            if param.kind == inspect.Parameter.POSITIONAL_ONLY:
                pos_args.append(value)
            else:
                keyword_args[name] = value

        result: Any = await self._func(*pos_args, **keyword_args)

        await send(result, update, context)

        self._logger.debug("Finished execution")
        raise ApplicationHandlerStop

    def __repr__(self) -> str:
        """Return a string representation of the Action object."""
        return f"Action '{self.name}' ({', '.join(f'/{cmd}' for cmd in self.commands)}) [-> {self._func.__name__}]"
