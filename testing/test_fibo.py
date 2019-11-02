from fibo import fib


def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(10) == 55