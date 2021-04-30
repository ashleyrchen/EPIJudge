from test_framework import generic_test


def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1 
        x = x >> 1 
    print(num_bits)
    return num_bits


if __name__ == '__main__':
    count_bits(12)
    count_bits(22)

    # exit(
    #     generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
    #                                    count_bits))
