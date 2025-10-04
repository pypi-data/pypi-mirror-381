"""
The control server for the dummy device.
"""

import multiprocessing
import random
import sys
from typing import Callable

import rich
import typer
import zmq
from cgse_dummy.dummy_dev import Dummy
from egse.command import ClientServerCommand
from egse.connect import get_endpoint
from egse.control import ControlServer
from egse.control import is_control_server_active
from egse.decorators import dynamic_interface
from egse.device import DeviceConnectionError
from egse.device import DeviceConnectionState
from egse.device import DeviceInterface
from egse.log import logger
from egse.logger import remote_logging
from egse.protocol import CommandProtocol
from egse.proxy import Proxy
from egse.response import Failure
from egse.settings import Settings
from egse.storage import TYPES
from egse.storage import is_storage_manager_active
from egse.storage import register_to_storage_manager
from egse.storage import store_housekeeping_information
from egse.storage import unregister_from_storage_manager
from egse.system import attrdict
from egse.system import format_datetime
from egse.system import type_name
from egse.zmq_ser import bind_address
from egse.zmq_ser import connect_address

cs_settings = Settings.load("DUMMY CS")
dev_settings = Settings.load("DUMMY DEVICE")

DEV_HOST = "localhost"
"""The hostname or IP address of the Dummy Device."""
DEV_PORT = dev_settings.PORT
"""The port number for the Dummy Device."""
DEV_NAME = f"Dummy Device {dev_settings.MODEL}"
"""The name used for the Dummy Device, this is used in Exceptions and in the info command."""

READ_TIMEOUT = 10.0  # seconds
"""The maximum time to wait for a socket receive command."""
WRITE_TIMEOUT = 1.0  # seconds
"""The maximum time to wait for a socket send command."""
CONNECT_TIMEOUT = 3.0  # seconds
"""The maximum time to wait for establishing a socket connect."""

# Especially DummyCommand and DummyController need to be defined in a known module
# because those objects are pickled and when de-pickled at the clients side the class
# definition must be known.

commands = attrdict(
    {
        "info": {
            "description": "Info on the Dummy Device.",
            "response": "handle_device_method",
        },
        "get_value": {
            "description": "Read a value from the device.",
        },
        "division": {"description": "Return a / b", "cmd": "{a} {b}"},
    }
)

app = typer.Typer(
    help=f"Dummy control server for the dummy device {dev_settings.MODEL}"
)


def is_dummy_cs_active():
    return is_control_server_active(
        endpoint=connect_address(
            cs_settings.PROTOCOL, cs_settings.HOSTNAME, cs_settings.COMMANDING_PORT
        )
    )


class DummyCommand(ClientServerCommand):
    pass


class DummyInterface(DeviceInterface):
    @dynamic_interface
    def info(self): ...

    @dynamic_interface
    def get_value(self, *args, **kwargs): ...

    @dynamic_interface
    def division(self, a: int | float, b: int | float) -> float:
        """
        Return the result of the number 'a' divided by the number 'b'.

        This method can also be used during testing to cause a ZeroDivisionError
        that should return a Failure object.
        """
        raise NotImplementedError("The division() method has not been implemented.")


class DummyProxy(Proxy, DummyInterface):
    """
    A Proxy that connects to the Dummy control server.

    Args:
        protocol: the transport protocol [default is taken from settings file]
        hostname: location of the control server (IP address) [default is taken from settings file]
        port: TCP port on which the control server is listening for commands [default is taken from settings file]
        timeout (float): the time in seconds before a timeout will occur
    """

    def __init__(
        self,
        protocol=cs_settings.PROTOCOL,
        hostname=cs_settings.HOSTNAME,
        port=cs_settings.COMMANDING_PORT,
        timeout=cs_settings.TIMEOUT,
    ):
        endpoint = get_endpoint(cs_settings.SERVICE_TYPE, protocol, hostname, port)
        super().__init__(endpoint, timeout=timeout)


class DummyController(DummyInterface):
    def __init__(self, control_server):
        super().__init__()

        self._cs = control_server
        self._dev = Dummy(DEV_HOST, DEV_PORT)

    def is_simulator(self):
        return True

    def is_connected(self):
        return self._dev.is_connected()

    def connect(self):
        try:
            self._dev.connect()
            logger.debug(f"Device {self._dev.name} connected.")
        except DeviceConnectionError as exc:
            logger.warning(
                f"Caught {type_name(exc)}: Couldn't establish connection ({exc})"
            )
            raise ConnectionError(
                f"Couldn't establish a connection with the device {self._dev.name}."
            ) from exc

        self.notify_observers(DeviceConnectionState.DEVICE_CONNECTED)

    def disconnect(self):
        try:
            self._dev.disconnect()
            logger.debug(f"Device {self._dev.name} disconnected.")
        except DeviceConnectionError as exc:
            raise ConnectionError(
                f"Couldn't disconnect from device {self._dev.name}."
            ) from exc

        self.notify_observers(DeviceConnectionState.DEVICE_NOT_CONNECTED)

    def reconnect(self):
        if self.is_connected():
            self.disconnect()
        self.connect()

    def info(self) -> str:
        return self._dev.trans("info").decode().strip()

    def get_value(self) -> float:
        return float(self._dev.trans("get_value").decode().strip())

    def division(self, a, b) -> float:
        return a / b


class DummyProtocol(CommandProtocol):
    def __init__(self, control_server: ControlServer):
        super().__init__(control_server)

        self.device_controller = DummyController(control_server)
        self.device_controller.add_observer(self)
        self.device_controller.connect()

        self.load_commands(commands, DummyCommand, DummyController)

        self.build_device_method_lookup_table(self.device_controller)

        self._count = 0

    def get_bind_address(self):
        return bind_address(
            self.control_server.get_communication_protocol(),
            self.control_server.get_commanding_port(),
        )

    def get_status(self):
        return super().get_status()

    def get_housekeeping(self) -> dict:
        logger.debug(f"Executing get_housekeeping function for {type_name(self)}.")

        result = dict()
        result["timestamp"] = format_datetime()

        if self.state == DeviceConnectionState.DEVICE_NOT_CONNECTED:
            return result

        self._count += 1

        # use the sleep to test the responsiveness of the control server when even this get_housekeeping function takes
        # a lot of time, i.e. up to several minutes in the case of data acquisition devices
        # import time
        # time.sleep(2.0)

        return {
            "timestamp": format_datetime(),
            "COUNT": self._count,
            "PI": 3.14159,  # just to have a constant parameter
            "Random": random.randint(0, 100),  # just to have a variable parameter
            "T (ºC)": self.device_controller.get_value(),
        }

    def quit(self):
        logger.info("Executing 'quit()' on DummyProtocol.")

        if self.device_controller.is_connected():
            self.device_controller.disconnect()


class DummyControlServer(ControlServer):
    """
    DummyControlServer - Command and monitor dummy device controllers.

    The sever binds to the following ZeroMQ sockets:

    * a REQ-REP socket that can be used as a command server. Any client can connect and
      send a command to the dummy device controller.

    * a PUB-SUP socket that serves as a monitoring server. It will send out status
      information to all the connected clients every HK_DELAY seconds.

    """

    def __init__(self):
        multiprocessing.current_process().name = "dummy_cs"

        super().__init__()

        self.logger = logger

        self.device_protocol = DummyProtocol(self)
        self.device_protocol.bind(self.dev_ctrl_cmd_sock)

        self.logger.info(
            f"Binding ZeroMQ socket to {self.device_protocol.get_bind_address()} for {type_name(self)}"
        )

        self.poller.register(self.dev_ctrl_cmd_sock, zmq.POLLIN)

        self.set_hk_delay(cs_settings.HK_DELAY)

        self.service_name = cs_settings.PROCESS_NAME

        self.register_service(service_type=cs_settings.SERVICE_TYPE)

    def get_communication_protocol(self):
        return "tcp"

    def get_commanding_port(self):
        return cs_settings.COMMANDING_PORT

    def get_service_port(self):
        return cs_settings.SERVICE_PORT

    def get_monitoring_port(self):
        return cs_settings.MONITORING_PORT

    def get_storage_mnemonic(self):
        return cs_settings.STORAGE_MNEMONIC

    def get_event_subscriptions(self) -> list[str]:
        return ["new_setup"]

    def get_event_handlers(self) -> dict[str, Callable]:
        return {"new_setup": self.handle_event_new_setup}

    def handle_event_new_setup(self, event_data: dict):
        if data := event_data.get("data"):
            self.logger.info(f"Handling 'new_setup' event with {data=}")
        else:
            self.logger.warning("Handling 'new_setup' event, but no 'data' part found.")

    def before_serve(self): ...

    def after_serve(self) -> None:
        self.deregister_service()

    def is_storage_manager_active(self):
        return is_storage_manager_active()

    def store_housekeeping_information(self, data):
        """Send housekeeping information to the Storage manager."""

        store_housekeeping_information(origin=cs_settings.STORAGE_MNEMONIC, data=data)

    def register_to_storage_manager(self) -> None:
        register_to_storage_manager(
            origin=cs_settings.STORAGE_MNEMONIC,
            persistence_class=TYPES["CSV"],
            prep={
                "column_names": list(self.device_protocol.get_housekeeping().keys()),
                "mode": "a",
            },
        )

    def unregister_from_storage_manager(self) -> None:
        unregister_from_storage_manager(origin=cs_settings.STORAGE_MNEMONIC)


@app.command()
def start():
    """Start the dummy control server on localhost."""

    # The following import is needed because without this import, the control server and Proxy will not be able to
    # instantiate classes that are passed in ZeroMQ messages and de-pickled.
    from cgse_dummy.dummy_cs import DummyControlServer  # noqa

    with remote_logging():
        try:
            control_server = DummyControlServer()
            control_server.serve()
        except KeyboardInterrupt:
            print("Shutdown requested...exiting")
        except SystemExit as exit_code:
            print(f"System Exit with code {exit_code}.")
            sys.exit(-1)
        except Exception:  # noqa
            import traceback

            traceback.print_exc(file=sys.stdout)


@app.command()
def stop():
    """Send a quit service command to the dummy control server."""
    with DummyProxy() as dummy:
        logger.info("Sending quit_server() to Dummy CS.")
        sp = dummy.get_service_proxy()
        sp.quit_server()


@app.command()
def status():
    with DummyProxy() as dummy:
        response = dummy.info()
        if isinstance(response, Failure):
            rich.print(f"[red]ERROR: {response}[/]")
        else:
            rich.print(response)


if __name__ == "__main__":
    app()
