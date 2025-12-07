case = """
3299143-3378031,97290-131156,525485-660941,7606-10180,961703-1031105,6856273537-6856492968,403537-451118,5330-7241,274725-384313,27212572-27307438,926609-954003,3035-3822,161-238,22625-31241,38327962-38415781,778-1155,141513-192427,2-14,47639-60595,4745616404-4745679582,1296-1852,80-102,284-392,4207561-4292448,404-483,708177-776613,65404-87389,5757541911-5757673432,21-38,485-731,1328256-1444696,11453498-11629572,41-66,2147-3014,714670445-714760965,531505304-531554460,4029-5268,3131222053-3131390224
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