from typing import Callable

def caching_fibonacci() -> Callable:
    '''
    Caching closure for storring fibonacci row
    '''
    ## Cache previous calculation of fibonacci row
    cache = {}

    def fibonacci(n: int) -> int:
        '''
        Recursive function for calculating fibonacci number
        '''
        nonlocal cache
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if cache.get(n):
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

print(fib(10))
print(fib(15))
