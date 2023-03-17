from datetime import datetime
from time import sleep
import logging


def profile(func):

    logging.basicConfig(format='%(message)s', level=0, filename='performance.log')
    logger = logging.getLogger()

    def timelogger(*args, **kwargs):

        start = datetime.now()
        res = func(*args, **kwargs)
        x = (datetime.now() - start)
        logger.debug(f"{start} - {func.__name__} -  {x}")
        return res
    return timelogger


@profile
def foo(x):
    sleep(2)
    return x**2


print(foo(2))


@profile
def fact(x):
    sleep(1)
    res = 1
    for i in range(1, x):
        res *= i
    return res


print(fact(10))

