# encoding: utf-8
# A closure is a function that has access to outer function local variables, even outer function is done execution. Close free variables from enviroment.
# Closures can avoid the use of global values and provides some form of data hiding. It can also provide an object oriented solution to the problem.

import logging

logging.basicConfig(filename='closure.log', level=logging.DEBUG, format="[%(levelname)-8s] - %(message)s")

def logger(func):
    def log_func(*args):
        result = func(*args)
        logging.info('Function: "{}"  with arguments "{}" get result "{}"'.format(func.__name__, args,result))
    return log_func


# def add(x, y):
#     return x + y

def add(*args):
    return sum(args)


def sub(x, y):
    return x - y


add_logger = logger(add)
sub_logger = logger(sub)
add_logger(1,2,3,4,5)
add_logger(69,73)
add_logger(69,73,88)

sub_logger(10, 2)
sub_logger(1, 1e10)
sub_logger(1, 1e-10)