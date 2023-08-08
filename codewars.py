"""Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

  12 ==> 21
 513 ==> 531
2017 ==> 2071"""

# import time
# start_time = time.process_time()

# from functools import reduce


# def factorial(n):

#     length_n = len(str(n))
#     return reduce(lambda x, y: x * y, range(1, length_n+1))


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

n = 204321
print(next_bigger(n))

# end_time = time.process_time()
# elapsed_time = (end_time - start_time) * 1000
# print(elapsed_time)