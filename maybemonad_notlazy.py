#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Maybe(object):
    pass


class Nothing(Maybe):
    def __repr__(self):
        return "Nothing"


class Just(Maybe):
    def __init__(self, obj):
        self.obj = obj

    def __repr__(self):
        return "Just %s" % self.obj


class MaybeMonad(object):
    def __setattr__(self, name, value):
        if isinstance(value, Nothing):
            self._maybe = Nothing
        setattr(self, name, value.obj)

    def ret(self, obj):
        if isinstance(self._maybe, Nothing):
            return Nothing()
        else:
            return Just(obj)


def lookup(list_, el):
    try:
        return Just(list_.index(el))
    except:
        return Nothing()


def search123(list_):
    m = MaybeMonad()
    m.x = lookup(list_, 1)
    m.y = lookup(list_, 2)
    m.z = lookup(list_, 3)
    return m.ret('%d %d %d' % (m.x, m.y, m.z))
