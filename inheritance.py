#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Animal(object):
    def run(self):
        print('animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Cat())


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())


class Timer(object):
    def run(self):
        print('start...')


run_twice(Timer())

a = Timer()
print(isinstance(a, Animal))

print(type(Timer()))
print(type(Animal()))
print(type(Cat()))
print(type(a))
print(dir(Dog()))