#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict
from monad import Monad


class Probability(Monad):
    def __init__(self, probs):
        self.probs = probs

    def bind(self, f):
        probs = defaultdict(int)
        for (outcome, prob) in self.probs.items():
            for noutcome, nprob in f(outcome).items():
                probs[noutcome] += nprob * prob
        return Probability(probs)
