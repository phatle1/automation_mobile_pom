import inspect
import logging
from pathlib import Path
from functools import wraps
from colorlog import ColoredFormatter
import time

parent_path = Path(__file__).resolve().parents[1]
LOG_LEVEL = logging.INFO
LOG_FORMAT = "\t%(asctime)-6s.%(msecs)03d %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger(__name__)


def create_new_handler_logger(log_level):
    logger.propagate = False
    if not logger.handlers:
        stream = logging.StreamHandler()  # pylint: disable=invalid-name
        stream.setLevel(log_level)
        stream.setFormatter(ColoredFormatter(LOG_FORMAT, "%H:%M:%S"))  # "%Y-%m-%d %H:%M:%S"
        logger.setLevel(log_level)
        logger.addHandler(stream)


create_new_handler_logger(LOG_LEVEL)


def action_log_decorator(cls):
    def inner(func, func_name):
        @wraps(func)
        def wrapper(*args, **kwargs):
            pass


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        val = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print_args = print_kwargs = ""
        if isinstance(func, type(lambda: 1)):
            print_args = args[1:]
            print_args = "', '".join(str(i) for i in print_args if i is not None)
        if kwargs:
            print_kwargs = ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        print(f" [params: '{print_args}'{print_kwargs}]" if print_args or print_kwargs else "")
        # action_log = action_log.replace("'', ", "")  # remove redundant '' if print_args is empty
        print(f"Finished {func.__name__}() result: '{val}' in {run_time:.4f} secs")
        print(f'{func.__code__.co_argcount}')
        print(f'{func.__code__.co_varnames}')
        print(locals().keys())
        print(f'{locals().get("func")}')
        return val

    return wrapper
