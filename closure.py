# encoding: utf-8

def outer_func():
    message = 'Hi'
    def inner_func():
        print(message)

    return inner_func()

outer_func()