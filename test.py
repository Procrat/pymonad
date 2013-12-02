#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt

from monad import do
from monad.chance import ChanceMonad
from monad.list import List
from monad.log import LogMonad, log
from monad.maybe import Maybe, Just, Nothing


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


def log_example():
    return \
    LogMonad(7) >> (lambda x:
    LogMonad(x + 5, '+ 5')) >> \
    log('Logging the life, yo') >> (lambda y:
    LogMonad(y / 2, '/ 2'))


def floor_sqrt_distribution(dist):
    return \
    ChanceMonad(dist) >> (lambda x:
    {int(sqrt(x)): 1})


if __name__ == '__main__':
    print('-- Maybe monad')
    print(search123([5, 4, 3, 2, 1]))
    print(search123([5, 4, 3, 1]))

    print('\n-- Maybe monad with do-notation')
    print(search123do([5, 4, 3, 2, 1]))
    print(search123do([5, 4, 3, 1]))

    print('\n-- List monad')
    print(double_double(1, 2, 3, 4, 5))

    print('\n-- Log monad')
    log_m = log_example()
    print('Result: %s, Logs: %s' % (log_m.obj, log_m.logs))

    print('\n-- Chance monad')
    dist = {x: 1 / 10 for x in range(10)}
    print(floor_sqrt_distribution(dist).probs)
