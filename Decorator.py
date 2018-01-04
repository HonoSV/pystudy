#!/usr/bin/env
# -*- coding:utf-8 -*-
import functools
import time
'''
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2015-3-25')


now()
'''
'''
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()

print(now.__name__)
'''

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1 = time.time()
        fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time()-t1))
        return fn(*args, **kw)
    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)

if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')

# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
# 再思考一下能否写出一个@log的decorator，使它支持添加或不添加参数


def log(text):
    if isinstance(text,str):
        def decorator(fn):
            @functools.wraps(fn)
            def wrappers(*args, **kw):
                print('%s, begin call %s' % (text, fn.__name__))
                fn(*args, **kw)
                print('%s, end call %s' % (text, fn.__name__))
                return
            return wrappers
        return decorator
    else:
        @functools.wraps(text)
        def warppers(*args, **kw):
            print('begin call %s' % text.__name__)
            text(*args, **kw)
            print('end call %s' % text.__name__)
            return
        return warppers


@log
def hello():
    print('hi')


hello()
