#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dirichlet
----------------------------------

Tests for `dirichlet` module.
"""
from random import normalvariate

from dirichlet import DirichletProcess


def test_basic():
    dp = DirichletProcess(lambda: normalvariate(0, 1), alpha=0.1)
    dp()
