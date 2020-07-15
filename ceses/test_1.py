import pytest

def test_1():
    '''用例描述：测试demo'''
    a = "hello"
    b = "hello"

    assert a==b

def test_2():
    '''用例描述'''
    a = "hellp"
    b = "hellox"

    assert a==b

if __name__ == '__main__':
    pytest.main(["-s","test_1.py"])