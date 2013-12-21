#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monad import Monad


class LogMonad(Monad):
    def __init__(self, obj, log=None):
        self.obj = obj
        self.logs = [log] if not log is None else []

    def bind(self, f):
        fn = f(self.obj)
        fn.logs[:0] = self.logs
        return fn

    @staticmethod
    def ret(obj):
        return LogMonad(obj)


def log(message):
    return (lambda x: LogMonad(x, message))
