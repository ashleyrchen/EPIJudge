from test_framework import generic_test
from test_framework.test_failure import TestFailure
import math
import functools, string

alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers = list(range(10))
alph_to_num = dict(zip(alphabet, numbers)) # NOTE string.digits.index(_) also does this 
num_to_alph = dict(zip(numbers, alphabet)) # NOTE ord(chr(_)) also does this

def int_to_string(x: int) -> str:
    # # -----NAIVE solution, O(n^2) time, O(n^2) space
    # # NOTE does not work on input like 204, 240 
    # def helper(x):
    #     if x < 10:
    #         return num_to_alph[x]
    #     else:
    #         power = math.floor(math.log(x, 10))
    #         place = 0 
    #         while x > 10**power:
    #             x -= 10**power
    #             place += 1 
    #         return num_to_alph[place] + helper(x)
    # return helper(x)

    # -----IMPROVED solution, O(n) time, O(n) space
    def helper(x):
        s = list()
        power = math.floor(math.log(x, 10))
        for i in reversed(range(power+1)):
            place = 0
            while x >= 10**i:
                x -= 10**i
                place += 1 
            s.append(num_to_alph[place])
        return ''.join(s) 

    if x < -9:
        return '-' + helper(math.fabs(x))
    elif x >= -9 and x < 0: 
        return '-' + num_to_alph[math.fabs(x)]
    elif x >= 0 and x <= 9: 
        return num_to_alph[x]
    return helper(x)

    # # -----TEXTBOOK solution, O(n) time, O(n) space
    # if x == 0: 
    #     return '0'
    # flag, s = '', list()
    # if x < 0: 
    #     flag, x = '-', -x 
    # while x > 0:
    #     s.append(num_to_alph[x % 10])
    #     x //= 10 # shorthand for x = floor(x / 10)
    # return flag + ''.join(reversed(s))    
    
def string_to_int(s: str) -> int:
    # # -----MY SOLUTION, O(n) time, O(1) space
    value, power, sign = 0, 1, 1 
    for i in reversed(range(len(s))):  
        if s[i] == '-':
            sign = -1
            break
        elif s[i] == "+":
            break 
        value += alph_to_num[s[i]] * power
        power *= 10
    return sign * value

    # # -----TEXTBOOK solution, O(n) time, O(1) space
    # return (
    #     functools.reduce(
    #     lambda running_sum, c: running_sum * 10 + string.digits.index(c), # function
    #     s[s[0] == '-' or s[0] == '+':], # NOTE sequence; s[True:] = s[1:], s[False:] = s
    #     0) # initial
    #     * (-1 if s[0] == '-' else 1))


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
