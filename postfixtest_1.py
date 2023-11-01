from postfix_1 import eval


def test_singleoperand():
    assert eval("4") == 4

def test_add():
    assert eval("26+") == 8

