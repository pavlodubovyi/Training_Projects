"""Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071"""
from itertools import permutations

def next_bigger(n):
    
    num_list = []
    final_list = []
    
    variants = list(permutations(str(n)))
    for el in variants:
        num_str = "".join(el)
        num_list.append(int(num_str))
    
    sorted_list = sorted(num_list)
    for num in sorted_list:
        if num > n:
            final_list.append(num)
            result = final_list[0]
        else:
            result = -1
    
    return result

n = 2111
print(next_bigger(n))