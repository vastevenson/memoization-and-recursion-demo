"""
Fibonacci sequence: 1,1,2,3,5,8,13,21,34,...
Write a method that takes an input (n) and returns the n'th term of the fibonacci sequence
Ex:
get_nth_fib_term(1) => 1
get_nth_fib_term(6) => 8

Use memoization to make this as efficient as possible for higher terms, like n > 100
"""

# cache to enable memoization to improve runtime complexity
fib_cache = {}

def get_nth_fib_term(n):
    if n in fib_cache:
        return fib_cache[n]

    # base case
    if n == 1 or n == 2:
        val = 1
    # recursive case
    else:
        val = get_nth_fib_term(n-1) + get_nth_fib_term(n-2)

    fib_cache[n] = val

    return val


for i in range(1,1000):
    print(f"Term-{i} is {get_nth_fib_term(i)}")