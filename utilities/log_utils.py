import functools
import time
import logging
import inspect
import builtins
from pathlib import Path


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
            action_log = ''
            verify = ''
            parent_path = Path(__file__).resolve().parents[1]
            for item in inspect.stack():
                if f"{parent_path}/pages" in item.filename:
                    if "self." in item.code_context:
                        str_to_extract = item.code_context[0].split("self.")[1].split("()")[0].removesuffix("\n")
                    else:
                        str_to_extract = item.code_context[0].split(".")[1].split("()")[0].removesuffix("\n")
                if f"{parent_path}/testcases" in item.filename:
                    code_context = item.code_context
                    called_func = code_context[0].split("(")[0]
                    action_log = called_func.split(".")[-1]
                    screen_name = called_func.removesuffix("." + action_log).strip()
                    screen_name = screen_name.replace(".", " > ").replace("_", " ").title()
                    break
            # # 🔴🟢
            if str_to_extract:
                action_log = f"[{screen_name}] {func.__name__}"
            else:
                action_log = f"[{screen_name}] {action_log}"
            if str(func_name).startswith("verify"):
                action_log = f"🟢 {action_log}"
            # Get parameters of the called function
            print_args = print_kwargs = ""
            if isinstance(func, type(lambda: 1)):
                print_args = args[1:]
            print_args = "', '".join(str(i) for i in print_args if i is not None)
            if kwargs:
                print_kwargs = ", " + ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
            action_log += f" [params: '{print_args}'{print_kwargs}]" if print_args or print_kwargs else ""
            action_log = action_log.replace("'', ", "")
            # Execute function
            action_log += f'{testcase_name} - {screen_name} - {action}'
            start_time = time.perf_counter()
            val = func(*args, **kwargs)
            end_time = time.perf_counter()
            run_time = end_time - start_time
            action_log += f' ran in [{'{0:.4f}s'.format(run_time)}]'
            logger.info(action_log)
            return val
        return wrapper

    for k in cls.__dict__.keys():
        if not k.startswith(r"__") and not k.startswith(f"_{cls}__") and callable(getattr(cls, k)):
            setattr(cls, k, inner(cls.__dict__[k], k))
    return cls
