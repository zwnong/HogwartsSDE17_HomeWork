# coding = utf-8
"""
@File     :  test_calculator.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  1:20
"""
import pytest
from test_code.calculator import Calculator
from utils.get_real_value import GetRealValue


class TestCalculator:
    data = GetRealValue()

    def setup_class(self):
        self.calc = Calculator()
        print('开始计算')

    def teardown_class(self):
        print('计算结束')

    # 测试加法
    @pytest.mark.add
    @pytest.mark.parametrize(["a", "b", "exp"], data.get_add_real_value(), ids=data.get_ids_real_value())
    def test_add(self, a, b, exp):
        assert exp == self.calc.add(a, b)

    # 测试除法
    @pytest.mark.div
    @pytest.mark.parametrize(["a", "b", "exp"], data.get_div_real_value())
    def test_div(self, a, b, exp):
        if b != 0:
            assert exp == self.calc.div(a, b)
        else:
            try:
                self.calc.div(a, b)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    pytest.main('-vs', 'calculator.py')
