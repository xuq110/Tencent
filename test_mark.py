import random
import time

import pytest

count = random.randint(1,5)

@pytest.mark.P0
@pytest.mark.hello
class TestMark:

    @pytest.mark.webtest
    def test_case1(self):
        print('test_case1')
        time.sleep(count)
        assert count == 3

    @pytest.mark.P1
    def test_case2(self):
        print('test_case2')
        time.sleep(count)
        assert count == 4

    def test_case3(self):
        print('test_case3')
        time.sleep(count)
        assert count == 5

if __name__ == '__main__':
    pytest.main(['-m','-k','"P0 and not webtest"','test_mark.py'])