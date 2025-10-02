from datetime import timedelta
from typing import Optional
from . import types as command_types
from opentrons.protocol_api.tasks import Task


def comment(msg: str) -> command_types.CommentCommand:
    text = msg
    return {"name": command_types.COMMENT, "payload": {"text": text}}


def delay(
    seconds: float, minutes: float, msg: Optional[str] = None
) -> command_types.DelayCommand:
    td = timedelta(minutes=minutes, seconds=seconds)
    actual_min, actual_sec = divmod(td.total_seconds(), 60)

    text = (
        f"Delaying for {int(actual_min)} minutes and " f"{round(actual_sec, 3)} seconds"
    )

    if msg:
        text = f"{text}. {msg}"

    return {
        "name": command_types.DELAY,
        "payload": {"minutes": actual_min, "seconds": actual_sec, "text": text},
    }


def pause(msg: Optional[str] = None) -> command_types.PauseCommand:
    text = "Pausing robot operation"
    if msg:
        text = text + ": {}".format(msg)
    return {
        "name": command_types.PAUSE,
        "payload": {
            "text": text,
            "userMessage": msg,
        },
    }


def resume() -> command_types.ResumeCommand:
    return {
        "name": command_types.RESUME,
        "payload": {"text": "Resuming robot operation"},
    }


def move_labware(text: str) -> command_types.MoveLabwareCommand:
    return {
        "name": command_types.MOVE_LABWARE,
        "payload": {"text": text},
    }


def wait_for_tasks(tasks: list[Task]) -> command_types.WaitForTasksCommand:
    task_ids = [task.created_at.strftime("%Y-%m-%d %H:%M:%S") for task in tasks]
    msg = f"Waiting for tasks that started at: {task_ids}."
    return {
        "name": command_types.WAIT_FOR_TASKS,
        "payload": {"text": msg},
    }


def create_timer(seconds: float) -> command_types.CreateTimerCommand:
    return {
        "name": command_types.CREATE_TIMER,
        "payload": {
            "text": f"Creating background timer for {seconds} seconds.",
            "time": seconds,
        },
    }
