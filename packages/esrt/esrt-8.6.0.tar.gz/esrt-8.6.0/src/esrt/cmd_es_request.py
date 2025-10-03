import typing as t

from pydantic import AfterValidator
from pydantic import AliasChoices
from pydantic import BeforeValidator
from pydantic import Field

from .cmd_base import BaseEsCmd
from .cmd_base import DefaultPrettyCmdMixin
from .cmd_base import EsHeadersCmdMixin
from .cmd_base import EsParamsCmdMixin
from .cmd_base import IpythonCmdMixin
from .cmd_base import OptionalInputCmdMixin
from .cmd_base import OutputCmdMixin
from .cmd_base import VerboseCmdMixin
from .cmd_base import rich_text
from .cmd_base import stderr_console
from .cmd_base import to_different_capitalization_conventions
from .typealiases import HttpMethod


def _validate_url(value: str) -> str:
    if not value.startswith('/'):
        value = f'/{value}'
    return value


class EsRequestCmd(
    OptionalInputCmdMixin,
    EsHeadersCmdMixin,
    EsParamsCmdMixin,
    DefaultPrettyCmdMixin,
    OutputCmdMixin,
    IpythonCmdMixin,
    VerboseCmdMixin,
    BaseEsCmd,
):
    method: t.Annotated[HttpMethod, BeforeValidator(str.upper)] = Field(
        default='GET',
        validation_alias=AliasChoices(
            'X',
            *to_different_capitalization_conventions('method'),
            *to_different_capitalization_conventions('request'),
        ),
    )
    url: t.Annotated[str, AfterValidator(_validate_url)] = Field(
        default='/',
        validation_alias=AliasChoices(
            'u',
            *to_different_capitalization_conventions('url'),
        ),
        description=rich_text('[b blue]Absolute url (without host) to target'),
    )

    def cli_cmd(self) -> None:
        if self.verbose:
            stderr_console.print(self)

        with stderr_console.status('Request ...') as _status:
            _status.update(spinner='bouncingBall')

            response = self.client.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=self.params,
                body=self.read_input(),
            )

        if isinstance(response, str):
            self.output.out(response)
            return self.start_ipython_if_need()

        if self.pretty:
            self.output.print_json(data=response)
        else:
            self.output.print_json(data=response, indent=None)

        return self.start_ipython_if_need()
