from datetime import datetime
from time import sleep
import logging
import functools


def profile(func):

    """ checks the running time of function"""
    logging.basicConfig(format='%(message)s', level="DEBUG", filename='performance.log')
    logger = logging.getLogger()

    @functools.wraps(func)
    def wrapper_time(*args, **kwargs):

        start = datetime.now()
        res = func(*args, **kwargs)
        x = (datetime.now() - start)
        logger.debug(f"{start} - {func.__name__}{args} -  {x}")
        return res
    return wrapper_time


@profile
def foo(x):
    sleep(2)
    return x**2


print(foo(5))


#@profile
#def fact(x):
#    sleep(1)
#    res = 1
#    for i in range(1, x):
#        res *= i
#    return res


#print(fact(10))

