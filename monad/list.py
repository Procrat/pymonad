#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import chain
from monad import Monad


class List(list, Monad):
    def __init__(self, *args):
        list.__init__(self, args)

    def bind(self, f):
        return List(*list(chain.from_iterable(map(f, self))))
