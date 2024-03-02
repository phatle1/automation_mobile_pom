import builtins
import inspect
import logging
import time
from functools import wraps
from pathlib import Path

from colorlog import ColoredFormatter
from selenium.common import NoSuchElementException


LOG_LEVEL = logging.INFO
LOG_FORMAT = "\t%(asctime)-6s.%(msecs)03d %(log_color)s%(levelname)7s | %(log_color)s%(message)s"
logging.root.setLevel(LOG_LEVEL)
logger = logging.getLogger('pythonConfig')


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
            # Get screen name and action name based on the current called class
            screen_name = ""
            action_log = ""
            nested_sub_func_name = ""
            parent_path = Path(__file__).resolve().parents[1]
            for item in inspect.stack():
                if f"{parent_path}/pages" in item.filename:
                    # Handle the called action from the same class (self.)
                    if "self." in item.code_context[0]:
                        nested_sub_func_name = item.code_context[0].split("self.")[1].split("()")[0].removesuffix("\n")
                    else:  # handle the called action from another class (alert_popup.)
                        nested_sub_func_name = item.code_context[0].split(".")[1].split("()")[0].removesuffix("\n")
                if f"{parent_path}/testcases" in item.filename:
                    code_context = item.code_context
                    called_func = code_context[0].split("(")[0]
                    action_log = called_func.split(".")[-1]
                    screen_name = called_func.removesuffix("." + action_log).strip()
                    screen_name = screen_name.replace(".", " > ").replace("_", " ").title()
                    break
            if nested_sub_func_name:
                action_log = f"[{screen_name}] {nested_sub_func_name}"
            else:
                action_log = f"[{screen_name}] {action_log}"
            if str(func_name).startswith("verify"):
                action_log = "⛳ " + action_log

            # Get parameters of the called function
            print_args = print_kwargs = ""
            if isinstance(func, type(lambda: 1)):
                print_args = args[1:]
            print_args = "', '".join(str(i) for i in print_args if i is not None)
            if kwargs:
                print_kwargs = ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            action_log += f" [params: '{print_args}'{print_kwargs}]" if print_args or print_kwargs else ""
            action_log = action_log.replace("'', ", "")  # remove redundant '' if print_args is empty

            # Execute the function
            start_time = time.perf_counter()  # get the current time before the action
            result = True
            reason_fail = ""
            if func_name.startswith("verify"):  # verification actions
                result, reason_fail = func(*args, **kwargs)  # execute the action having values returned
            else:  # interaction actions
                try:
                    func(*args, **kwargs)  # execute the action not having values returned
                except Exception as ex:
                    result = False
                    reason_fail = f"\n{ex.msg.split(';')[0]}"  # noqa
            end_time = time.perf_counter()
            run_time = end_time - start_time  # measure the action's time
            log = f"{action_log} [{'{0:.1f}s'.format(run_time)}]{reason_fail}"
            if result:
                logger.info(log)
            else:  # handle the failure by verify or action step
                builtins.is_test_failed = True
                # Save a fail screenshot locally
                test_case_id = builtins.test_file.split("_")[1]
                builtins.driver.save_screenshot(parent_path + f"{test_case_id}_{func_name}.png")
                if func_name.startswith("verify"):  # failed by verify step: log warning, continue the test
                    logger.warning("❌ " + log)
                else:  # failed by action step: log error, stop the test
                    logger.error("❌ " + log)
                    raise NoSuchElementException(reason_fail)

        return wrapper

    for k in cls.__dict__.keys():
        if not k.startswith(r"__") and not k.startswith(f"_{cls}__") and callable(getattr(cls, k)):
            setattr(cls, k, inner(cls.__dict__[k], k))
    return cls
