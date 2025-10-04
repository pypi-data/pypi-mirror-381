# This file is part of the Lima2 project
#
# Copyright (c) 2020-2024 Beamline Control Unit, ESRF
# Distributed under the MIT licence. See LICENSE for more info.

"""Lima2 tango device utils"""

import logging
from typing import Protocol, cast

import tango as tg

from lima2.common.exceptions import Lima2DeviceError
from lima2.common.state import DeviceState
from lima2.conductor.utils import DecoratedFunc

logger = logging.getLogger(__name__)


def handle_tango_errors(method: DecoratedFunc) -> DecoratedFunc:
    """Decorator for an async method that may raise a DevFailed / AttributeError.

    If it does, a Lima2DeviceError will be raised with a helpful message.

    Handling AttributeErrors is required for offline devices.
    """

    async def wrapper(self: TangoDevice, *args, **kwargs):  # type: ignore
        try:
            # logger.debug(f"Calling {self.name}.{method.__name__}()")
            return await method(self, *args, **kwargs)
        except tg.DevFailed as e:
            raise Lima2DeviceError(
                f"Error from device {self.name} in call to {method.__name__}():\n  - "
                + "\n  - ".join([arg.desc for arg in e.args]),
                device_name=self.name,
            ) from e
        except AttributeError as e:
            raise Lima2DeviceError(
                f"Attribute error from device {self.name} in call to {method.__name__}(): {e}",
                device_name=self.name,
            ) from e

    return cast(DecoratedFunc, wrapper)


class TangoDevice(Protocol):
    """Lima2 tango device interface.

    Used to benefit from type checking, e.g. when using the list [control, *receivers].
    """

    @property
    def name(self) -> str:
        raise NotImplementedError

    async def ping(self) -> int:
        raise NotImplementedError

    async def acq_state(self) -> DeviceState:
        raise NotImplementedError

    async def stop(self) -> None:
        raise NotImplementedError
