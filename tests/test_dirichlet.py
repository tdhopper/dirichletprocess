#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dirichlet
----------------------------------

Tests for `dp` module.
"""
from random import normalvariate

from dp import DirichletProcess


def test_basic():
    dp = DirichletProcess(lambda: normalvariate(0, 1), alpha=0.1)
    for _ in range(1000):
        dp()
