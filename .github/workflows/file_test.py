# -*- coding: utf-8 -*-

import pytest

def test_calc_addition():
  # Function test du résultat de 2+4
    output = 2+4
    assert output == 6

def test_calc_substraction():
  # Function test du résultat de 2-4
    output = 2-4
    assert output == -2

def test_calc_multiply():
  # Function test du résultat de 2*4
    output = 2*4
    assert output == 8

def test_coucou():
  # Function test si la résultat renvoie 'hello'
    output='hello'
    assert output == 'hello'
