from postfix_1 import eval


def test_singleoperand():
    assert eval("4") == 4

def test_add():
    assert eval("26+") == 8

def test_sub():
    assert eval("43-") == 2

