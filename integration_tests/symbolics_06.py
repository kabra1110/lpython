from sympy import Symbol, sin, cos, exp, log, Abs, pi, diff
from lpython import S

def test_elementary_functions():

    # test sin, cos
    x: S = Symbol('x')
    assert(sin(pi) == S(0))
    assert(sin(pi/S(2)) == S(1))
    assert(sin(S(2)*pi) == S(0))
    assert(cos(pi) == S(-1))
    assert(cos(pi/S(2)) == S(0))
    assert(cos(S(2)*pi) == S(1))
    assert(diff(sin(x), x) == cos(x))
    assert(diff(cos(x), x) == S(-1)*sin(x))

    # test exp, log
    assert(exp(S(0)) == S(1))
    assert(log(S(1)) == S(0))
    assert(diff(exp(x), x) == exp(x))
    assert(diff(log(x), x) == S(1)/x)

    # test Abs
    assert(Abs(S(-10)) == S(10))
    assert(Abs(S(10)) == S(10))
    assert(Abs(S(-1)*x) == Abs(x))

    # test composite functions
    a: S = exp(x)
    b: S = sin(a)
    c: S = cos(b)
    d: S = log(c)
    e: S = Abs(d)
    print(e)
    assert(e == Abs(log(cos(sin(exp(x))))))

test_elementary_functions()