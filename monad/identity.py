#!/usr/bin/env python
# -*- coding: utf-8 -*-
from monad import Monad


class Identity(Monad):
    def __init__(self, obj):
        self.obj = obj

    def bind(self, f):
        return f(self.obj)
