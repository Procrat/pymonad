#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monad import do
from maybe import Maybe, Just, Nothing
from list import List


def lookup(list_, el):
    try:
        return Just(list_.index(el))
    except:
        return Nothing()


def search123(list_):
    return \
    lookup(list_, 1) >> (lambda x:
    lookup(list_, 2) >> (lambda y:
    lookup(list_, 3) >> (lambda z:
    Maybe.ret('%d %d %d' % (x, y, z)))))


def search123do(list_):
    return \
    do('x = lookup(list_, 1)',
       'y = lookup(list_, 2)',
       'z = lookup(list_, 3)',
       '"%d %d %d" % (x, y, z)')


def double_double(*list_):
    return \
    List(*list_) >> (lambda x:
    2 * [x]) >> (lambda x:
    [2 * x])


if __name__ == '__main__':
    print("-- Maybe monad")
    print(search123([5, 4, 3, 2, 1]))
    print(search123([5, 4, 3, 1]))

    print("\n-- Maybe monad with do-notation")
    print(search123do([5, 4, 3, 2, 1]))
    print(search123do([5, 4, 3, 1]))

    print("\n-- List monad")
    print(double_double(1, 2, 3, 4, 5))
