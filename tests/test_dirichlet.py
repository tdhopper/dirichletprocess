#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dirichlet
----------------------------------

Tests for `dirichlet` module.
"""
from numpy.random import normal

from dirichlet import DirichletProcess


def test_basic():
    dp = DirichletProcess(normal, alpha=0.1)
    dp()
