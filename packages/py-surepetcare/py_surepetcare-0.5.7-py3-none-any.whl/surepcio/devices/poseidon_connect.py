import logging

from .device import BaseControl
from .device import BaseStatus
from .device import DeviceBase
from surepcio.command import Command
from surepcio.const import API_ENDPOINT_PRODUCTION
from surepcio.enums import ProductId

logger = logging.getLogger(__name__)


class Control(BaseControl):
    pass


class Status(BaseStatus):
    pass


class PoseidonConnect(DeviceBase[Control, Status]):
    """Representation of a Poseidon Connect device."""

    def refresh(self):
        """Refresh the device status and control settings from the API."""

        def parse(response) -> "PoseidonConnect":
            if not response:
                return self

            self.status = BaseStatus(**{**self.status.model_dump(), **response["data"]})
            self.control = BaseControl(**{**self.control.model_dump(), **response["data"]})
            return self

        return Command(
            method="GET",
            endpoint=f"{API_ENDPOINT_PRODUCTION}/device/{self.id}",
            callback=parse,
        )

    @property
    def product(self) -> ProductId:
        return ProductId.POSEIDON_CONNECT
