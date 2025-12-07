case = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""

from utils import parse_input

a = parse_input(case)
input = []
for i in a:
    b = i.split(',')
    for v in b:
        if v != '':
            input.append(v)

def get_range(a:str):
    num1, num2 = a.split('-')
    return int(num1), int(num2)

def solution():
    invalid = 0
    for i in input:
        num1, num2 = get_range(i)
        # print(num1, num2)
        for i in range(num1, num2+1):
            if len(str(i)) % 2 != 0:
                continue
            half_len = int(len(str(i)) / 2)
            if half_len == float:
                continue
            left, right = str(i)[:half_len], str(i)[half_len:]
            if left == right:
                invalid = invalid + i
    print(invalid)
solution()