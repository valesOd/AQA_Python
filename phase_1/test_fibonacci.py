from phase_1.fibonacci import generateFibonacci

def test_fibonacci_seven():
    assert generateFibonacci(7) == [0,1,1,2,3,5,8,13]

def test_fibonacci_zero():
        assert generateFibonacci(0) == [0]

def test_fibonacci_one():
            assert generateFibonacci(1) == [0,1]