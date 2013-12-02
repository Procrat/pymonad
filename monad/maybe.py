#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monad import Monad


class Maybe(Monad):
    @staticmethod
    def ret(obj):
        return Just(obj)


class Nothing(Maybe):
    def bind(self, f):
        return self

    def __repr__(self):
        return "Nothing"


class Just(Maybe):
    def __init__(self, obj):
        self.obj = obj

    def bind(self, f):
        return f(self.obj)

    def __repr__(self):
        return "Just %s" % self.obj
