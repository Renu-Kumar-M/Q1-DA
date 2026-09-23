from app import multiply, divide
def test_multiply():
    assert multiply(3, 4) == 12
def test_divide():
    assert divide(12, 3) == 4