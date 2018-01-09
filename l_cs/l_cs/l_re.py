# -*- coding: utf-8 -*-
import re


def is_valid_email(addr):
    r = re.match(r'^(\w+(\.\w*)?)@(\w+).com$', addr)
    if r is not None:
        return True


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


def name_of_email(addr):
    a = re.split(r'@', addr)
    if re.match(r'^<', a[0]):
        b = re.split(r'[<>]', a[0])
        a[0] = b[1]
    return a[0]


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')