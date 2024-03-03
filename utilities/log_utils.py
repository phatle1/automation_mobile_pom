import functools
import time
import logging
import inspect
import builtins
from pathlib import Path
from functools import wraps

from colorlog import ColoredFormatter
from selenium.common import NoSuchElementException

LOG_LEVEL = logging.INFO
LOG_FORMAT = "\t%(asctime)-6s.%(msecs)03d %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger('pythonConfig')


def create_new_handler_logger(log_level):
    logger.propagate = False
    if not logger.handlers:
        parent_path = Path(__file__).resolve().parents[1]
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
        log_file_name = f'{parent_path}/logs/log{current_time}.txt'

        file_handler = logging.FileHandler(log_file_name, mode="w")
        file_handler.setFormatter(fmt)
        file_handler.setLevel(log_level)
        logger.addHandler(file_handler)


create_new_handler_logger(LOG_LEVEL)


def action_log_decorator(cls):
    def inner(func, func_name):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            screen_name = ''
            testcase_name = ''
            action = ''
            log_action = ''
            str_to_extract = ''
            nested_sub_func_name = ''
            verify = ''
            parent_path = Path(__file__).resolve().parents[1]
            temp_testcase = []
            temp_pages = []
            for item in inspect.stack(0):
                if f"{parent_path}/testcases" in item.filename:
                    temp_testcase.append(item)
                    str_to_extract = item.code_context
                    testcase_name = item.function
                    continue
                if f"{parent_path}/pages" in item.filename:
                    temp_pages.append(item)
                    """
                    if "self." in item.code_context:
                        nested_sub_func_name = item.code_context[0].split("self.")[1].split("()")[0].removesuffix("\n")
                    else:  # handle the called action from another class (alert_popup.)
                        nested_sub_func_name = item.code_context[0].split(".")[1].split("()")[0].removesuffix("\n")
                    """
            for item in temp_pages:
                screen_name = item.filename[slice(item.filename.rfind('/')+1, -3)]
                if item.function.startswith('func'):
                    pass
                if item.function.startswith('action'):
                    action = item.function
                if item.function.startswith('verify'):
                    verify = item.function
            log_action += f'{testcase_name} - {screen_name} - {action}'
            start_time = time.perf_counter()  # get the current time before the action
            val = func(*args, **kwargs)  # execute the action not having values returned
            end_time = time.perf_counter()
            run_time = end_time - start_time  # measure the action's time
            log_action += f' ran in [{'{0:.1f}s'.format(run_time)}]'
            # logger.info(f'{func.__name__} ran in [{'{0:.1f}s'.format(run_time)}]')
            logger.info(log_action)
            return val

        return wrapper

    for k in cls.__dict__.keys():
        if not k.startswith(r"__") and not k.startswith(f"_{cls}__") and callable(getattr(cls, k)):
            setattr(cls, k, inner(cls.__dict__[k], k))
    return cls
