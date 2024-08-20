# Import necessary modules
from functools import reduce

# Task 1: Fibonacci Sequence Generator
def fibonacci(n):
    return (lambda f: f(f, n, [0, 1]))(lambda f, n, acc: acc if len(acc) >= n else f(f, n, acc + [acc[-1] + acc[-2]]))

# Task 2: Concatenate List of Strings
def concatenate_strings(lst):
    return reduce(lambda x, y: x + y, lst)
## hello world -> helloworld

# Task 3: Cumulative Sum of Squares of Even Numbers
def cumulative_sum_squares(lst):
    return list(map(lambda sublst: sum(map(lambda x: x ** 2, filter(lambda y: y % 2 == 0, sublst))), lst))
## cumulative_sum_squares [1, 2, 3], [4, 5, 6]

# Task 4: Higher-Order Function for Cumulative Operations
def cumulative_operation(op):
    return lambda seq: reduce(op, seq)
##factorial and exponentiation functions in shell
# Task 5: Rewrite Program with Nested Functions
def sum_squared_evens(nums):
    return reduce(lambda acc, x: acc + x, map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
##sum_squared_evens 1 2 3 4 -> 20 (since it only counts even numbers)
# Task 6: Count Palindromes in List of Lists
def palindrome_count(lst):
    return list(map(lambda sublst: len(list(filter(lambda x: x == x[::-1], sublst))), lst))
##palindrome_count([['hello', 'noon', 'radar'], ['level', 'world']]) number of palindromes in each list
# Task 7: Lazy evaluation
##Lazy Evaluation is a technique where expressions are not evaluated until their values are actually needed.
# This approach can improve performance by avoiding unnecessary computations and can handle infinite data
# structures.
#squared_values = [square(x) for x in generate_values()]: Here, generate_values() is not evaluated
#immediately. Instead, the generator yields values one at a time as needed. The square function is called
#for each value only when it is needed for processing.
#In summary, lazy evaluation allows computation to be deferred until results are actually needed, improving
#efficiency and enabling handling of potentially large or infinite data streams.

# Task 8: Prime Number Filter
def prime_filter(lst):
    is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))
    return sorted([x for x in lst if is_prime(x)], reverse=True)
## prime_filter 1 2 3 4 5 6 7 -> 2 3 5 7