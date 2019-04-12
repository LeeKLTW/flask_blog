# encoding: utf-8

def square(x):
    return x**2

def qube(x):
    return x**3

def my_map(func, arg_list):
    result = [func(arg) for arg in arg_list]
    return result

square_list = my_map(square, [0,1,2])
qube_list = my_map(qube,[0,1,2])

