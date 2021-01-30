# coding = utf-8
"""
@File     :  demo.py
@project  :  
@Author   :  zwnong
@Time     :  2021/1/30  2:16
"""

import pytest
import yaml


class TestClac:
    def test_addition(self):
        pass

    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        print(a + b)
