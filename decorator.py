# encoding: utf-8
import logging
logging.basicConfig(filename='decorator.log', level=logging.DEBUG, format="[%(levelname)-8s]- %(message)s")

def decorator_function(fn):
    def wrapper_function(*args, **kwargs):
        result = fn(*args, **kwargs)
        logging.debug('Recorded by function.')
        logging.info(f'Function {fn.__name__} with Arguments: {args}, {kwargs}')
        return result
    return wrapper_function

@decorator_function
def add(*args):
    return sum(args)

@decorator_function
def sub(x, y):
    return x - y

add(1,2,3,4)
add(2,2,3,4)
sub(10,2)





class decorator_class:
    def __init__(self,fn):
        self.fn = fn

    def __call__(self,*args, **kwargs):
        result = self.fn(*args, **kwargs)
        logging.debug('Recorded by class.')
        logging.info(f'Function {self.fn.__name__} with Arguments: {args}, {kwargs}')
        return result

@decorator_class
def add(*args):
    return sum(args)

@decorator_class
def sub(x, y):
    return x - y

add(1,2,3,4)
add(2,2,3,4)
sub(8,2)