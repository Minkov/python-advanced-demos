import math

# Binary search
# 1 2 3 4 5 6 7 8 9 10 11 12
# => max steps =  3 < log(2)12 < 4
# searching for 8
# 1:12
# -> take mid, 6, and compare with 8
# 7:12
# -> take mid, 9, and compare with 8
# 7:8
# -> take mid, 7, and compare with 8
# 8:8

### BREAK UNTILL 7:40 ###

# Searching for 591
# 1024
# Try 1: 512,  answer: >
# Try 2: (512+1024)/2=768, answer: <
# Try 3: (512+768)/2=640, answer: <
# Try 4: (512+640)/2=576, answer: >
# Try 5: (576+640)/2=608, answer: <
# Try 6: (576+608)/2=592, answer: <
# Try 7: (576+592)/2=584, answer: >
# Try 8: (584+592)/2=588, answer: >
# Try 9: (588+592)/2=590, answer: >
# Try 10: (590+592)/2=591, answer: =

# Binary search:
# Calculate log, square root, ...

def calculate_log(x, base_as_str):
    if base_as_str == 'natural':
        return math.log(x)

    base = int(base_as_str)

    return math.log(x, base)

#
# print(calculate_log(10, 10))
# print(calculate_log(1024, 2))
# print(calculate_log(1024 * 1024, 2))  # 2^10 * 2^10 = 2^20
# print(calculate_log(10, 'natural'))
