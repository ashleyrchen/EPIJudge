from test_framework import generic_test


dictionary = {0: 0, 1: 1}
def fibonacci(n: int) -> int:
    # # -----RECURSIVE SOLUTION, O(2**(n-1)) time, O(n) space, 
    # if n <= 1: return n 
    # return fibonacci(n-1) + fibonacci(n-2)

    # # -----DYNAMIC PROGRAMMING SOLUTION, O(n) time, O(n) space, 
    # for i in range(2, n + 1):
    #     if i not in dictionary:
    #         dictionary[i] = dictionary[i-1] + dictionary[i-2]
    # return dictionary[n]

    # -----DYNAMIC PROGRAMMING SOLUTION, O(n) time, O(1) space,
    minus_two, minus_one = 0, 1
    if n <= 1: return n
    for _ in range(2, n + 1):
        cur = minus_one + minus_two
        minus_two, minus_one = minus_one, cur
    return cur
        

if __name__ == '__main__':
    fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]
    for i in range(len(fib_list)):
        assert fibonacci(i) == fib_list[i]

    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
