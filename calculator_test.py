from calculator import add

# given 
def test_add():
    # when
    result = add(5, 10)
    # then
    assert result == 15

def test_add_with_negativ_number():
    result = add(-1, -2)
    assert result == -3