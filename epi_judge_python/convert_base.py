from test_framework import generic_test
import math


def convert_base(num_as_string: str, b1: int, b2: int) -> str: 
# -----MY SOLUTION, O(n(1+log_b2(b1))) time, O(nlog_b2(b1)) space,
    if len(num_as_string) == 0 or num_as_string == '0':
        return num_as_string
    sign = False
    if num_as_string[0] == '-':
        sign = True  
        num_as_string = num_as_string[1:]

    def b1_to_b10(c: str):
        return int(c) if c in [str(_) for _ in list(range(10))] else ord(c)-55
    def b10_to_b2(ii: int):
        return str(ii) if ii in range(10) else chr(55+ii)

    x, result, = 0, []
    for i in range(1, len(num_as_string) + 1): 
        x += b1_to_b10(num_as_string[-i]) * b1**(i - 1)
    for j in range(math.floor(math.log(x, b2)), -1, -1):
        result.append(str(x // b2**j))
        x %= b2**j
    result = ''.join([b10_to_b2(int(ii)) for ii in result])
    return '-' + result if sign else result 


def test_convert_base():
    assert convert_base(convert_base('615', 7, 13), 13, 7) == '615'
  
    for n in [
                1,
                2,   
                8, 
                9, 
                15,
                16,
                2**32]:
        assert convert_base(str(n), 10, 16) == hex(n)[2:].upper()
        assert convert_base(convert_base(str(n), 10, 16), 16, 10) == str(n)
        assert convert_base(str(n), 10, 8) == oct(n)[2:].upper()
        assert convert_base(convert_base(str(n), 10, 8), 8, 10) == str(n)
        assert convert_base(str(n), 10, 2) == bin(n)[2:].upper()
        assert convert_base(convert_base(str(n), 10, 2), 2, 10) == str(n)

        assert convert_base(str(-n), 10, 16) == '-' + hex(n)[2:].upper()
        assert convert_base(convert_base(str(-n), 10, 16), 16, 10) == str(-n)
        assert convert_base(str(-n), 10, 8) == '-' + oct(n)[2:].upper()
        assert convert_base(convert_base(str(-n), 10, 8), 8, 10) == str(-n)
        assert convert_base(str(-n), 10, 2) == '-' + bin(n)[2:].upper()
        assert convert_base(convert_base(str(-n), 10, 2), 2, 10) == str(-n)
    
    for b1 in [2, 8, 16]:
        for b2 in [2, 8, 16]:
            assert convert_base('0', b1, b2) == '0' 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
