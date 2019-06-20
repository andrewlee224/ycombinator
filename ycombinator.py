"""Implement a Y-combinator using lambda functions to transform a recursive function into a
non-recursive one. The Y-combinator is one of the fundamental results of lambda calculus. Note that
while the Y-combinator itself is recursive, there is a more complex non-recursive version of it
called a U-combinator.

More of a theoretical exercise rather than a practical one - the fixed-point version is slower than
standard recursion in Python. There are more advanced versions of the combinator as mentioned
above - like U-combinator, or combinators with memoization capabilities.
"""

import time


Y = lambda F: (
    (lambda x:
        F(lambda y: (x(x))(y))
    )
    (lambda x:
        F(lambda y: (x(x))(y))
    )
)


fact_wrapper = lambda fact: (
    lambda n:
        1 if (n == 0) else (n * fact(n-1))
)


fixed_point_fact = Y(fact_wrapper)


def fact_recursive(n):
    if n == 0: return 1
    return n * fact_recursive(n-1)


if __name__ == '__main__':
    # a quick benchmark

    t0 = time.time()
    val = fact_recursive(300)
    t1 = time.time()
    print("Recursive version: output in time {}".format(t1 - t0))

    t2 = time.time()
    val = fixed_point_fact(300)
    t3 = time.time()
    print("Fixed-point version: output in time {}".format(t3 - t2))
