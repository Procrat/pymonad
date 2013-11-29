#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect


class Monad(object):
    def __rshift__(self, f):
        return self.bind(f)

    def bind(self, f):
        raise NotImplementedError

    @staticmethod
    def ret(object_):
        raise NotImplementedError


def do(*args):
    frame = inspect.currentframe()
    try:
        globals_ = frame.f_back.f_globals
        locals_ = frame.f_back.f_locals
    finally:
        del frame
    return _do(args, globals_, locals_)


def _do(args, globals_, locals_):
    if len(args) > 1:
        [name, value] = map(lambda x: x.strip(), args[0].split('='))
        value = eval(value, globals_, locals_)

        def do_some_more(true_value):
            locals_[name] = true_value
            return _do(args[1:], globals_, locals_)

        if len(args) == 2:
            return value.bind(lambda x: value.ret(do_some_more(x)))
        else:
            return value.bind(do_some_more)

    else:
        return eval(args[0], globals_, locals_)
