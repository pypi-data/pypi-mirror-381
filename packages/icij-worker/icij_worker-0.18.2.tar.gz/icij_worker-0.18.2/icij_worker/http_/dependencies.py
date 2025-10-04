import logging
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import cast

from fastapi import FastAPI

from icij_worker import AMQPTaskManager
from icij_worker.http_.config import HttpServiceConfig
from icij_worker.typing_ import Dependency
from icij_worker.utils.dependencies import DependencyInjectionError, run_deps

_TASK_MANAGER: AMQPTaskManager | None = None
_HTTP_SERVICE_CONFIG: HttpServiceConfig | None = None

logger = logging.getLogger(__name__)


async def http_service_config_setup(config: HttpServiceConfig | None, **_) -> None:
    global _HTTP_SERVICE_CONFIG
    _HTTP_SERVICE_CONFIG = config
    logger.info(
        "HTTP Service config: %s\n", _HTTP_SERVICE_CONFIG.model_dump_json(indent=2)
    )


def lifespan_http_service_config() -> HttpServiceConfig:
    if _HTTP_SERVICE_CONFIG is None:
        raise DependencyInjectionError("http service config")
    return cast(HttpServiceConfig, _HTTP_SERVICE_CONFIG)


async def loggers_setup(**_) -> None:
    config = cast(HttpServiceConfig, lifespan_http_service_config())
    config.setup_loggers()


async def task_manager_setup(**_) -> None:
    global _TASK_MANAGER
    config = cast(HttpServiceConfig, lifespan_http_service_config())
    _TASK_MANAGER = config.to_task_manager()
    await _TASK_MANAGER.__aenter__()  # pylint: disable=unnecessary-dunder-call


async def task_manager_teardown(exc_type, exc_val, exc_tb) -> None:  # noqa: ANN001
    global _TASK_MANAGER
    await _TASK_MANAGER.__aexit__(exc_type, exc_val, exc_tb)
    _TASK_MANAGER = None


def lifespan_task_manager() -> AMQPTaskManager:
    if _TASK_MANAGER is None:
        raise DependencyInjectionError("task manager")
    return cast(AMQPTaskManager, _TASK_MANAGER)


BASE_DEPENDENCIES = [
    ("http service config", http_service_config_setup, None),
    ("loggers", loggers_setup, None),
    ("task manager", task_manager_setup, task_manager_teardown),
]


@asynccontextmanager
async def run_http_service_deps(
    app: FastAPI, config: HttpServiceConfig, dependencies: list[Dependency]
) -> AbstractAsyncContextManager:
    app.state.config = config
    async with run_deps(dependencies=dependencies, ctx=app.title, config=config):
        yield
