# -*- coding:utf-8 -*-

import pytest
import sys
sys.path.append("D:\Python36_install\Lib\site-packages")
sys.path.append("..")
from python.calc import Calc

class TestCalc:

    def setup(self):
        self.calc=Calc()

    def test_add(self):
        result =self.calc.add(3,2)
        print(result)

    def test_add_1(self):
        result =self.calc.add(1,2)
        print(result)

    def test_div(self):
        result=self.calc.div(2,2)
        assert 1 == result

# pytest.main(['-vs','test_pytest.py::test_add_1'])