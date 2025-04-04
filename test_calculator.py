# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 14:35:37 2025

@author: jdev1
"""

from calculator import add, divide, clear_history, history

def test_add():
    clear_history()
    assert add(2, 3) == 5
    assert "add( 2,3) equals: 5" in history()

def test_divide_by_zero():
    clear_history()
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
