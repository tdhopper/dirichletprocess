#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dirichlet
----------------------------------

Tests for `dirichlet` module.
"""
from scipy import stats

from dirichlet import DirichletProcess


def test_basic():
    def base_distribution():
        return stats.norm().rvs(size=1)[0]
    dp = DirichletProcess(base_distribution, alpha=0.1)
    dp()
