# -*- coding: utf-8 -*-
from collections import Hashable

from random import betavariate, uniform


def weighted_choice(weights):
    choices = range(len(weights))
    total = sum(weights)
    r = uniform(0, total)
    upto = 0
    for c, w in zip(choices, weights):
        if upto + w > r:
            return c
        upto += w
    raise Exception("Error in weighted_choice.")


class DirichletProcess():
    def __init__(self, base_measure, alpha):
        if alpha <= 0:
            raise ValueError("alpha must be a positive number")
        if not hasattr(base_measure, '__call__'):
            raise ValueError("base_measure must be callable")
        if not isinstance(base_measure(), Hashable):
            raise ValueError("base_measure must return hashable object")
        self.base_measure = base_measure
        self.alpha = alpha

        self.cache = []
        self.weights = []
        self.total_stick_used = 0.

    def __call__(self):
        remaining = 1.0 - self.total_stick_used
        i = weighted_choice(self.weights + [remaining])
        if i < len(self.weights):
            return self.cache[i]
        else:
            stick_piece = betavariate(1, self.alpha) * remaining
            self.total_stick_used += stick_piece
            self.weights.append(stick_piece)
            new_value = self.base_measure()
            self.cache.append(new_value)
            return new_value
