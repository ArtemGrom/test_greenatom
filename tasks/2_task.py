from functools import partial
from typing import Callable, List


def create_handler(callback: Callable, counter: int = 5) -> List:
    handlers = []
    for step in range(counter):
        # добавляем обработчики для каждого шага с 0 до 4
        handlers.append(partial(callback, step))
    return handlers


def execute_handlers(handlers: List[Callable]) -> None:
    # запускаем добавленные обработчики(шаги с 0 до 4)
    for handler in handlers:
        handler()
