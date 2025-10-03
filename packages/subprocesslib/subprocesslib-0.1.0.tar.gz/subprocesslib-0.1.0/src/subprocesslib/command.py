import asyncio
import shlex
import subprocess
from asyncio.subprocess import Process
from typing import Any, Self

from .paramspec_from import method_paramspec_from_function


class Command(tuple[str, ...]):
    """Represents a command to be executed.

    It inherits from `tuple[str,..]`.
    Example:
        >>> cmd = Command('ls', '-l')
        >>> isinstance(cmd, tuple)
        True

    The program is the first element of the tuple.
    The arguments are the rest of the elements of the tuple.
    Example:
        >>> cmd = Command('ls', '-l')
        >>> cmd.program
        'ls'
        >>> cmd.args
        ('-l',)

    Arguments are converted to strings using `str()`.
    Example:
        >>> cmd = Command('tail', '-n', 5, '/var/log/syslog')
        >>> cmd
        Command('tail', '-n', '5', '/var/log/syslog')

    The `__call__` method returns a new Command with additional arguments.
    Example:
        >>> cmd1 = Command('ls', '-l')
        >>> cmd2 = cmd1('-a')
        >>> cmd2
        Command('ls', '-l', '-a')
        >>> cmd1
        Command('ls', '-l')

    The `__str__` method returns a string representation of the command.
    It uses shlex.join.
    Example:
        >>> cmd = Command('ls', '-l')
        >>> str(cmd)
        'ls -l'
    """

    def __new__(cls, program: str, *args: Any) -> Self:
        return super().__new__(cls, map(str, (program,) + args))

    def __str__(self) -> str:
        return shlex.join(self)

    def __call__(self, *args: Any) -> Self:
        return self.__class__(*self, *args)

    @property
    def program(self) -> str:
        """Returns the program that was given to Command

        The program is the first element of the Command tuple.

        Example:
            >>> cmd = Command('ls', '-l')
            >>> cmd.program
            'ls'
        """
        return self[0]

    @property
    def args(self) -> tuple[str, ...]:
        """Returns the arguments that will be passed to the program.

        The arguments are the elements after the first element of the Command tuple.

        Example:
            >>> cmd = Command('ls', '-l')
            >>> cmd.args
            ('-l',)
        """
        return self[1:]

    @method_paramspec_from_function(subprocess.Popen)
    def spawn(self, *args, **kwargs) -> subprocess.Popen:
        """Spawn a new process with the command.

        Same as `subprocess.Popen(...)`.
        """
        return subprocess.Popen(
            str(self) if kwargs.get("shell", False) else self,
            *args,
            **kwargs,
        )

    @method_paramspec_from_function(subprocess.run)
    def run(self, *args, **kwargs) -> subprocess.CompletedProcess:
        """Run the command and wait for it to complete.

        Same as `subprocess.run(...)`.
        """
        return subprocess.run(
            str(self) if kwargs.get("shell", False) else self,
            *args,
            **kwargs,
        )

    @method_paramspec_from_function(subprocess.check_output)
    def output(self, *args, **kwargs) -> bytes:
        """Run the command and return its output.

        Same as `subprocess.check_output(...)`.
        """
        return subprocess.check_output(
            str(self) if kwargs.get("shell", False) else self,
            *args,
            **kwargs,
        )

    @method_paramspec_from_function(asyncio.create_subprocess_exec)
    async def spawn_async(self, *args, **kwargs) -> Process:
        """Spawn a new process with the command.

        Same as `asyncio.create_subprocess_exec(...)`.
        """
        if kwargs.get("shell", False):
            program = str(self)
        else:
            program = self.program
            args = self.args + args

        return await asyncio.create_subprocess_exec(program, *args, **kwargs)
