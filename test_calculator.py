from calculator import add, sub, mult, div

def test_add():
	assert add(2, 3) == 5
def test_divide():
	assert div(6, 2) == 3
def test_multily():
        assert mult(2, 3) == 6
def test_subtract():
        assert sub(6, 2) == 4
def test_divide_uneven():
	a,b = 5,2 
	result = div(a,b)
	assert result == 2.5
