from pydantic import AliasChoices
from pydantic import Field
from pydantic_settings import CliImplicitFlag

from .cmd_base import BaseEsCmd
from .cmd_base import IpythonCmdMixin
from .cmd_base import VerboseCmdMixin
from .cmd_base import console
from .cmd_base import stderr_console
from .cmd_base import stderr_dim_console
from .cmd_base import to_different_capitalization_conventions


class EsPingCmd(
    IpythonCmdMixin,
    VerboseCmdMixin,
    BaseEsCmd,
):
    info: CliImplicitFlag[bool] = Field(
        default=True,
        validation_alias=AliasChoices(
            'I',
            *to_different_capitalization_conventions('info'),
        ),
    )

    def cli_cmd(self) -> None:
        if self.verbose:
            stderr_dim_console.out(f'Ping {self.client.hosts}')

        with stderr_console.status('Ping ...') as _status:
            _status.update(spinner='bouncingBall')

            result = self.client.ping()

        if result is False:
            stderr_console.out('Ping failed', style='b red')
            return self.start_ipython_if_need()

        stderr_console.out('Ping ok', style='b green')
        if self.info:
            with stderr_console.status('Info ...') as _status:
                _status.update(spinner='bouncingBall')

                info = self.client.info()

            console.print_json(data=info)

        return self.start_ipython_if_need()
