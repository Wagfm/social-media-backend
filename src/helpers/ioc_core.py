import controllers
import routes
import services
from helpers.ioc_controllers import IOCControllersContainer
from helpers.ioc_routers import IOCRoutersContainer
from helpers.ioc_services import IOCServicesContainer


class IOCCore:
    def __init__(self) -> None:
        self._routers_container = IOCRoutersContainer()
        self._controllers_container = IOCControllersContainer()
        self._services_container = IOCServicesContainer()
        self._routers_container.wire(packages=[routes])
        self._controllers_container.wire(packages=[controllers])
        self._services_container.wire(packages=[services])

    @property
    def routers_container(self) -> IOCRoutersContainer:
        return self._routers_container

    @property
    def controllers_container(self) -> IOCControllersContainer:
        return self._controllers_container

    @property
    def services_container(self) -> IOCServicesContainer:
        return self._services_container
