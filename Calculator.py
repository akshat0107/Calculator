#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Calculator:
    def __init__(self,a,b):
        self._a=a
        self._b=b

    def add(self):
        return self._a+self._b

    def subtract(self):
        return self._a-self._b

    def multiply(self):
        return self._a*self._b

    def divide(self):
        if self._b==0:
            raise ValueError("divide by zero")
        return self._a/self._b

