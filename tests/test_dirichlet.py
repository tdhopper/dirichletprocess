#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dirichlet
----------------------------------

Tests for `dp` module.
"""
import pytest

from random import normalvariate

from dp import DirichletProcess


def test_basic():
    dp = DirichletProcess(lambda: normalvariate(0, 1), alpha=0.1)
    for _ in range(1000):
        dp()


def test_bad_alpha():
    with pytest.raises(ValueError):
        DirichletProcess(lambda: normalvariate(0, 1), alpha=-1)


def test_noncallable_base_measure():
    with pytest.raises(ValueError):
        DirichletProcess(None, alpha=1)


def test_nonhashable_base_measure():
    with pytest.raises(ValueError):
        DirichletProcess(lambda: [], alpha=1)
