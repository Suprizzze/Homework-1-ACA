from datetime import datetime
from time import sleep


def profile(func):

    p_file = open("performance.log", "a+")

    def wrapper(*args, **kwargs):

        start = datetime.now()
        res = func(*args, **kwargs)
        x = (datetime.now() - start)
        text = str(datetime.now()) + " - " + str(func.__name__) + " - " + str(x)
        p_file.write(text)
        p_file.write("\n")
        p_file.close()
        return res
    return wrapper


@profile
def foo(x):
    sleep(2)
    return x**2


print(foo(2))
