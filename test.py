from main import add, sub

def test_add():
    assert 4 == add(2,2)
    
def test_sub():
    assert 3 == sub(5,2)
