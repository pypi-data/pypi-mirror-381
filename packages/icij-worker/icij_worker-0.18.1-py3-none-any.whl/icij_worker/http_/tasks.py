import logging
from http.client import HTTPException

from fastapi import APIRouter
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT

from icij_common.logging_utils import TRACE, log_elapsed_time_cm
from icij_worker import Task
from icij_worker.exceptions import UnknownTask
from icij_worker.http_.constants import TASKS_TAG
from icij_worker.http_.dependencies import lifespan_task_manager
from icij_worker.http_.objects import TaskCreationQuery, TaskSearch
from icij_worker.objects import ErrorEvent

logger = logging.getLogger(__name__)


def tasks_router(prefix: str = "/api") -> APIRouter:
    router = APIRouter(prefix=prefix, tags=[TASKS_TAG])

    @router.put("/tasks/{task_id}")
    async def _create_task(task_id: str, task: TaskCreationQuery) -> str:
        task = Task.create(task_id=task_id, task_name=task.name, args=task.args)
        task_manager = lifespan_task_manager()
        is_new = await task_manager.save_task(task)
        if not is_new:
            logger.debug('Task(id="%s") already exists, skipping...', task_id)
            return Response(task.id, status_code=200)
        logger.debug('Task(id="%s") created, queuing...', task_id)
        await task_manager.enqueue(task)
        logger.info('Task(id="%s") queued...', task_id)
        return Response(task.id, status_code=201)

    async def _get_task_(task_id: str) -> Task:
        task_manager = lifespan_task_manager()
        try:
            with log_elapsed_time_cm(
                logger, logging.INFO, "retrieved task in {elapsed_time} !"
            ):
                task = await task_manager.get_task(task_id=task_id)
        except UnknownTask as e:
            raise HTTPException(status_code=404, detail=e.args[0]) from e
        return task

    @router.get("/tasks/{task_id}")
    async def _get_task(task_id: str) -> Task:
        return await _get_task_(task_id)

    @router.get("/tasks/{task_id}/state", response_model=str)
    async def _get_task_state(task_id: str) -> str:
        state = (await _get_task_(task_id)).state.value
        return Response(content=state, media_type="text/plain")

    @router.post("/tasks/{task_id}/cancel", responses={204: {"model": None}})
    async def _cancel_task(
        task_id: str,
        requeue: bool = False,
    ) -> None:  # noqa: FBT001, FBT002
        task_manager = lifespan_task_manager()
        try:
            await task_manager.cancel(task_id=task_id, requeue=requeue)
        except UnknownTask as e:
            raise HTTPException(status_code=404, detail=e.args[0]) from e
        return Response(status_code=HTTP_204_NO_CONTENT)

    @router.get("/tasks/{task_id}/result", response_model=object)
    async def _get_task_result(task_id: str) -> object:
        task_manager = lifespan_task_manager()
        try:
            result = await task_manager.get_task_result(task_id=task_id)
        except UnknownTask as e:
            raise HTTPException(status_code=404, detail=e.args[0]) from e
        return result.result

    @router.get("/tasks/{task_id}/errors")
    async def _get_task_errors(task_id: str) -> list[ErrorEvent]:
        task_manager = lifespan_task_manager()
        try:
            errors = await task_manager.get_task_errors(task_id=task_id)
        except UnknownTask as e:
            raise HTTPException(status_code=404, detail=e.args[0]) from e
        return errors

    @router.post("/tasks", response_model=list[Task])
    async def _search_tasks(search: TaskSearch) -> list[Task]:
        task_manager = lifespan_task_manager()
        with log_elapsed_time_cm(logger, TRACE, "searched tasks in {elapsed_time} !"):
            tasks = await task_manager.get_tasks(
                group=None, task_type=search.name, status=search.status
            )
        return tasks

    return router
