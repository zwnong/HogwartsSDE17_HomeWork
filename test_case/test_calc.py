# coding = utf-8
"""
@File     :  test_calc.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  1:20
"""
import sys

a = sys.path.append('../config')
import pytest
from test_code.test_calculator import Calculator


class TestCalculator:
    # 测试加法

    @pytest.mark.login
    def test_add(self):
        calu = Calculator()
        assert 2 == calu.add(1, 1)

    # 测试减法
    @pytest.mark.search
    def div(self):
        pass
