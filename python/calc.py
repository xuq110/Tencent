# -*- coding:utf-8 -*-
# type hints 类型提示

class Calc:

    def add(self, a,b):
        return a + b

    def div(self, a,b):
        return a / b

    def minus(self, a,b):
        return a - b

    def mull(self, a,b):
        try:
            return a * b
        except:
            return "Dividend can not be zero"