# coding = utf-8
"""
@File     :  test_calc.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  1:20
"""
import sys

sys.path.append('..')
print(sys.path)
import pytest
from test_code.test_calculator import Calculator


class TestCalculator:
    # 相加
    @pytest.mark.search
    def test_add(self):
        calu = Calculator()
        assert 2 == calu.add(1, 1)

    @pytest.mark.login
    def div(self):
        pass
