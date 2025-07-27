#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pytest
from Calculator import Calculator


# In[4]:


def test_add_positive_numbers():
    calc = Calculator(8,2)
    assert calc.add()==10

def test_subtract():
    calc = Calculator(8,2)
    assert calc.subtract()==6

def test_multiply():
    calc = Calculator(8,2)
    assert calc.multiply()==16

def test_divide():
    calc = Calculator(8,2)
    assert calc.divide()==4

def test_divide_float():
    calc = Calculator(7,2)
    assert calc.divide()==3.5

def test_divide_by_self():
    calc = Calculator(8,8)
    assert calc.divide()==1.0

def test_divide_by_zero():
    calc = Calculator(8,0)
    with pytest.raises(ValueError,match="divide by zero"):
        calc.divide()

def test_initial_values():
    calc = Calculator(100, 200)
    assert calc._a == 100
    assert calc._b == 200


# In[ ]:




