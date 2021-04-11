# -*- coding:utf-8 -*-
'''
import pytest
import yaml
from ..python.calc import *

# 定义获取数据的类
class Yamldata:
    def __init__(self,data_path):
        #初始化获取yaml文件中的数据
        self.data=yaml.safe_load(data_path)

    #
'''
import pytest
import pytest_assume
class TestDemo1():
    # 类名要以Test开始
    def test_one(self):
        print("开始执行 test_one 方法")
        x = 'this'
        # assert 'h' in x
        pytest.assume('h' not in x)
        pytest.assume(1 == 2)
        pytest.assume('x' in 'xxx')

    def test_two(self):
        print("开始执行 test_two 方法")
        x = 'may'
        assert 'm' in x

    def test_three(self):
        print("开始执行 test_three 方法")
        x = 'this'
        assert 'y' in x


class TestDemo2():
    def test_demo_one(self):
        print("开始执行 test_demo_one 方法")
        x = 'this'
        assert 'h' in x

    def test_demo_two(self):
        print("开始执行 test_demo_two 方法")
        x = 'may'
        assert 'm' in x

    def test_demo_three(self):
        print("开始执行 test_demo_three 方法")
        x = 'this'
        assert 'y' in x

if __name__ == '__main__':
#执行模块里的所有用例
    pytest.main()
# 执行模块里的所有用例
    # pytest.main("-v -x TestDemo1")
    # 另一种写法
    #pytest.main(['-v', '-x', 'TestDemo2'])