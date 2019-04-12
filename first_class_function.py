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

def logger(msg):
    def log_message():
        print('Log', msg)
    return log_message

log_hi = logger('Hi') # <function logger.<locals>.log_message at 0x10a096048>
log_hi() # 'Log Hi'

def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    return wrap_text

html = html_tag('h1')
html('Title')