from postfix_1 import eval


def test_singleoperand():
    assert eval("4") == 4

def test_add():
    assert eval("26+") == 8

def test_sub():
    assert eval("43-") == 1

def test_mul():
    assert eval("34*") == 12

def test_div():
    assert eval("82/") == 5

