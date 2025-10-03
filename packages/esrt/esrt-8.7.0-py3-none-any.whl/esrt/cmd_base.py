import inspect
import io
import json
import os
from pathlib import Path
import sys
import typing as t

import IPython
from pydantic import AliasChoices
from pydantic import AliasGenerator
from pydantic import BeforeValidator
from pydantic import ConfigDict
from pydantic import Field
from pydantic import Json
from pydantic import JsonValue
from pydantic import PlainValidator
from pydantic import TypeAdapter
from pydantic import model_validator
from pydantic import validate_call
from pydantic.alias_generators import to_snake
from pydantic_settings import BaseSettings
from pydantic_settings import CliImplicitFlag
from pydantic_settings import CliPositionalArg
from pydantic_settings import SettingsConfigDict
from rich.console import Console
from rich.progress import BarColumn
from rich.progress import MofNCompleteColumn
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import Task
from rich.progress import TaskProgressColumn
from rich.progress import TextColumn
from rich.progress import TimeElapsedColumn
from rich.progress import TimeRemainingColumn
from rich.progress import TransferSpeedColumn
from rich.prompt import Confirm
from rich.text import Text
from typing_extensions import Self

from .clients import EsClient
from .typealiases import JsonBodyT


console = Console()
stderr_console = Console(stderr=True)
stderr_dim_console = Console(stderr=True, style='dim')


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def _validate_output_console(file_or_tio: t.Union[str, io.TextIOWrapper]) -> Console:
    tio = Path(file_or_tio).open('w') if isinstance(file_or_tio, str) else file_or_tio  # noqa: SIM115
    return Console(file=tio)


OutputConsole = t.Annotated[Console, PlainValidator(_validate_output_console)]


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def _validate_input_file(file_or_tio: t.Union[str, io.TextIOWrapper]) -> io.TextIOWrapper:
    tio = (
        (t.cast(io.TextIOWrapper, sys.stdin) if file_or_tio == '-' else Path(file_or_tio).open('r'))  # noqa: SIM115
        if isinstance(file_or_tio, str)
        else file_or_tio
    )
    return tio


Input = t.Annotated[io.TextIOWrapper, PlainValidator(_validate_input_file)]


json_body_type_adapter = TypeAdapter[JsonBodyT](Json[JsonBodyT])


@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def _validate_json_input(file: str) -> t.Optional[JsonBodyT]:
    tio = t.cast(io.TextIOWrapper, sys.stdin) if file == '-' else Path(file).open('r')  # noqa: SIM115
    s = tio.read().strip() or None
    return None if s is None else json_body_type_adapter.validate_python(s)


JsonInput = t.Annotated[JsonBodyT, PlainValidator(_validate_json_input)]


def rich_text(*objects: t.Any) -> str:  # noqa: ANN401
    """Return a string representation of the object, formatted with rich text."""
    f = io.StringIO()
    Console(file=f).print(*objects)
    return f.getvalue()


class _TransferSpeedColumn(TransferSpeedColumn):
    def render(self, task: 'Task') -> Text:
        """Show data transfer speed."""
        speed = task.finished_speed or task.speed
        if speed is None:
            return Text('?', style='progress.data.speed')
        data_speed = int(speed)
        return Text(f'{data_speed}/s', style='progress.data.speed')


def _to_kebab(s: str) -> str:
    snake = to_snake(s)
    return snake.replace('_', '-')


def to_different_capitalization_conventions(field_name: str) -> list[str]:
    choices = [
        _to_kebab(field_name),
        # to_pascal(field_name),
        to_snake(field_name),
        # to_camel(field_name),
    ]
    return choices


def _validate_to_different_capitalization_conventions(field_name: str) -> AliasChoices:
    choices = to_different_capitalization_conventions(field_name)
    return AliasChoices(*choices)


class _BaseCmd(BaseSettings):
    model_config: t.ClassVar[SettingsConfigDict] = SettingsConfigDict(
        alias_generator=AliasGenerator(validation_alias=_validate_to_different_capitalization_conventions),
    )

    @validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
    def progress(self, *, console: Console, title: str) -> Progress:
        return Progress(
            SpinnerColumn(),
            TextColumn(text_format=title),
            BarColumn(),
            #
            _TransferSpeedColumn(),
            #
            TaskProgressColumn(),
            #
            TimeElapsedColumn(),
            MofNCompleteColumn(),
            TimeRemainingColumn(),
            console=console,
        )

    @staticmethod
    @validate_call(validate_return=True)
    def json_to_str(obj: JsonValue, /) -> str:
        return json.dumps(obj)

    @staticmethod
    def _tty_confirm(prompt: str, /, *, default: t.Optional[bool] = None) -> bool:
        tty = Path(os.ctermid())
        return Confirm.ask(
            prompt=prompt,
            console=Console(file=tty.open('r+')),
            default=t.cast(bool, default),  # ! type bug in rich
            stream=tty.open('r'),
        )


class VerboseCmdMixin(_BaseCmd):
    verbose: CliImplicitFlag[bool] = Field(
        default=False,
        validation_alias=AliasChoices(
            'v',
            *to_different_capitalization_conventions('verbose'),
        ),
    )


class OutputCmdMixin(_BaseCmd):
    output: OutputConsole = Field(
        default=t.cast(OutputConsole, sys.stdout),
        validation_alias=AliasChoices(
            'o',
            *to_different_capitalization_conventions('output'),
        ),
    )

    @property
    def is_output_stdout(self) -> bool:
        return self.output.file in [
            sys.stdout,
            getattr(sys.stdout, 'rich_proxied_file', None),  # * rich.progress.Progress
        ]


class ConfirmCmdMixin(VerboseCmdMixin, _BaseCmd):
    yes: CliImplicitFlag[bool] = Field(
        default=True,
        validation_alias=AliasChoices(
            'y',
            *to_different_capitalization_conventions('yes'),
        ),
        description=rich_text('[b blue]Do not ask for confirmation'),
    )

    def confirm(self) -> bool:
        if self.yes is True:
            if self.verbose is True:
                stderr_dim_console.print(self)
            return True

        confirm = self._tty_confirm(rich_text(self, 'Continue?'))
        if confirm is True:
            return True

        stderr_console.print('Aborted!', style='b red')
        return False


class IpythonCmdMixin(_BaseCmd):
    ipython: CliImplicitFlag[bool] = Field(
        default=False,
        validation_alias=AliasChoices(
            'ipy',
            *to_different_capitalization_conventions('ipython'),
        ),
    )

    def _print_user_ns(self, target_ns: dict[str, t.Any], /) -> None:
        stderr_console.print()
        stderr_console.print('variables:')
        for v in target_ns:
            if v.startswith('_'):
                continue
            stderr_console.print(f'* {v}', style='b cyan')

    @property
    def _stdin_is_a_tty(self) -> bool:
        """
        -f - (GOOD)
            sys.stdin.isatty() = True
            sys.stdin.seekable() = False
            color OK!
        |
            sys.stdin.isatty() = False
            sys.stdin.seekable() = False
            color GG!
        -f - <<<
            sys.stdin.isatty() = False
            sys.stdin.seekable() = True
            color GG!
        """
        if 0:
            stderr_console.print(f'{sys.stdin.isatty() = }')
            stderr_console.print(f'{sys.stdin.seekable() = }')
        return sys.stdin.isatty()

    def _replace_stdin(self) -> None:
        tty = Path(os.ctermid())
        sys.stdin = tty.open('r')

    def start_ipython_if_need(self) -> None:
        """
        Maybe replace sys.stdin with a tty file.
        """

        if not self.ipython:
            return

        curr_frame = inspect.currentframe()
        if curr_frame is None:
            stderr_console.print('No current frame', style='b red')
            sys.exit(1)

        target_frame = curr_frame.f_back
        if target_frame is None:
            stderr_console.print('No target frame', style='b red')
            sys.exit(1)

        target_ns = target_frame.f_locals
        self._print_user_ns(target_ns)

        if not self._stdin_is_a_tty:
            self._replace_stdin()

        IPython.start_ipython(argv=[], user_ns=target_ns)


class BaseEsCmd(_BaseCmd):
    client: CliPositionalArg[t.Annotated[EsClient, BeforeValidator(EsClient)]] = Field(
        # default=t.cast(EsClient, '127.0.0.1:9200'),
        validation_alias=AliasChoices(
            'es_host',
        ),
    )


class _InputCmdMixin(_BaseCmd):
    input_: t.Optional[Input] = Field(
        default=None,
        validation_alias=AliasChoices(
            'f',
            *to_different_capitalization_conventions('input'),
        ),
        description=rich_text(
            """[b yellow]example: '-f my_query.json'.""",
            """[b red]Or '-f -' for stdin.""",
            """[b blue]A file containing the search query.""",
        ),
    )
    data: t.Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            'd',
            *to_different_capitalization_conventions('data'),
        ),
        description=rich_text(
            '[b blue]A string containing the search query.',
            '[b red]Exclusive with -f/--input.',
        ),
    )

    @property
    def is_input_stdin(self) -> bool:
        return self.input_ == sys.stdin


class OptionalInputCmdMixin(_InputCmdMixin):
    @model_validator(mode='after')
    def _validate_input(self) -> Self:
        if (self.input_ is not None) and (self.data is not None):
            message = 'Only one of `-f/--input` or `-d/--data` is allowed.'
            raise ValueError(message)

        return self

    def read_input(self) -> t.Optional[str]:
        if self.data is not None:
            return self.data

        if self.input_ is None:
            return None

        return self.input_.read()

    def read_json_input(self) -> t.Optional[JsonBodyT]:
        if self.data is not None:
            if self.data == '':
                return None

            return json_body_type_adapter.validate_python(self.data)

        if self.input_ is None:
            return None

        if self.input_.seekable():
            self.input_.seek(0)

        x = self.input_.read()
        if x == '':
            return None

        return json_body_type_adapter.validate_python(x)


class RequiredInputCmdMixin(_InputCmdMixin):
    def read_input(self) -> str:
        if self.data is not None:
            return self.data

        if self.input_ is None:
            if sys.stdin.isatty():
                stderr_console.print('stdin is not a tty', style='b red')
                sys.exit(1)
            self.input_ = t.cast(io.TextIOWrapper, sys.stdin)

        return self.input_.read()


class _NdInputCmdMixin(_BaseCmd):
    input_: t.Optional[Input] = Field(
        default=None,
        validation_alias=AliasChoices(
            'f',
            *to_different_capitalization_conventions('input'),
        ),
        description=rich_text(
            Text("""example: '-f my_query.ndjson'.""", style='b yellow'),
            Text("""Or '-f -' for stdin.""", style='b red'),
            Text('A NDJSON (Newline delimited JSON) file containing the bulk request.', style='b blue'),
        ),
    )
    data: t.Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            'd',
            *to_different_capitalization_conventions('data'),
        ),
        description=rich_text(
            Text('A string containing the search query.', style='b blue'),
            Text('Exclusive with -f/--input.', style='b red'),
        ),
    )


class OptionalNdInputCmdMixin(_NdInputCmdMixin):
    @model_validator(mode='after')
    def _validate_input(self) -> Self:
        if (self.input_ is not None) and (self.data is not None):
            message = 'Only one of `-f/--input` or `-d/--data` is allowed.'
            raise ValueError(message)

        return self

    def read_iterator_input(self) -> t.Iterable[str]:
        if self.data is not None:
            return self.data.strip().splitlines(keepends=True)

        if self.input_ is None:
            stderr_console.print('no input', style='b red')
            sys.exit(1)

        if self.input_.seekable():
            self.input_.seek(0)

        return (x for x in self.input_ if x.strip())


class RequiredNdInputCmdMixin(_NdInputCmdMixin):
    @model_validator(mode='after')
    def _validate_input(self) -> Self:
        if (self.input_ is not None) and (self.data is not None):
            message = 'Only one of `-f/--input` or `-d/--data` is allowed.'
            raise ValueError(message)

        return self

    def read_iterator_input(self) -> t.Iterable[str]:
        if self.data is not None:
            return self.data.strip().splitlines(keepends=True)

        if self.input_ is None:
            if sys.stdin.isatty():
                stderr_console.print('stdin is not a tty', style='b red')
                sys.exit(1)
            self.input_ = t.cast(io.TextIOWrapper, sys.stdin)

        if self.input_.seekable():
            self.input_.seek(0)

        return (x for x in self.input_ if x.strip())


class EsIndexCmdMixin(BaseEsCmd):
    index: t.Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            'i',
            *to_different_capitalization_conventions('index'),
        ),
        description=rich_text(
            """[b yellow]example: '--index=i01,i02'""",
            """[b blue]A comma-separated list of index names to search; use `_all` or empty string to perform the operation on all indices""",  # noqa: E501
        ),
    )


class EsDocTypeCmdMixin(BaseEsCmd):
    doc_type: t.Optional[str] = Field(
        default=None,
        validation_alias=AliasChoices(
            *to_different_capitalization_conventions('doc_type'),
        ),
        description=rich_text(
            '[b blue]A comma-separated list of document types to search; leave empty to perform the operation on all types'  # noqa: E501
        ),
    )


class EsHeadersCmdMixin(BaseEsCmd):
    headers: dict[str, JsonValue] = Field(
        default_factory=dict,
        validation_alias=AliasChoices(
            'H',
            *to_different_capitalization_conventions('header'),
        ),
        description=rich_text(
            """[b yellow]example: '--header a=1 --header b=false'""",
            """[b blue]Additional parameters to pass to the query""",
        ),
    )


class EsParamsCmdMixin(BaseEsCmd):
    params: dict[str, JsonValue] = Field(
        default_factory=dict,
        validation_alias=AliasChoices(
            'p',
            *to_different_capitalization_conventions('param'),
        ),
        description=rich_text(
            """[b yellow]example: '--param a=1 --param b=false'""",
            """[b blue]Additional parameters to pass to the query""",
        ),
    )


class DryRunCmdMixin(BaseEsCmd):
    dry_run: CliImplicitFlag[bool] = Field(
        default=False,
        validation_alias=AliasChoices(
            'n',
            *to_different_capitalization_conventions('dry_run'),
        ),
    )


class DefaultPrettyCmdMixin(BaseEsCmd):
    pretty: CliImplicitFlag[bool] = Field(
        default=True,
    )


class DefaultNotPrettyCmdMixin(BaseEsCmd):
    pretty: CliImplicitFlag[bool] = Field(
        default=False,
    )
