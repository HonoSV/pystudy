#!/usr/bin/dev python3
# -*- coding:utf-8 -*-


class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

    __repr__ = __str__


class Fib(object):
    '''
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    '''
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a


f = Fib()
print(f[5])


class Chain(object):

    def __init__(self, path=''):
        self.__path = path

    def __getattr__(self, item):
        return Chain('%s/%s' % (self.__path, item))

    def __str__(self):
        return self.__path

    __call__ = __getattr__
    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('Zhangsan').repos)


class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        if path == 'users':
            return Chain('%s' % self)
        return Chain('%s/%s' % (self, path))

    def __str__(self):
        return self._path

    def __call__(self, value):
        return Chain('%s/%s' % (self, value))

    __repr__ = __str__


print(Chain().status.user.timeline.list)
print(Chain().users('Zhangsan').repos)