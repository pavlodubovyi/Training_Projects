# def caching_fibonacci():

#     cache = {}
    
#     def fibonacci(n):

#         for key in range(0, n + 1): # not just "range(n)", because range doesn't count the last number, we need to add n + 1
#             if key in cache:
#                 value = cache.get(key) # the same as cache[key] - we return the value of a key
#                 return value 
#             else:
#                 if key == 0:
#                     value = 0
#                 elif key == 1:
#                     value = 1
#                 else:
#                     value = cache.get(key - 1, 1) + cache.get(key - 2, 0)
#                 cache[key] = value
#         # print(cache)
#         return cache[n]
    
#     return fibonacci 

# fib = caching_fibonacci()
# num = fib(5)
# print(num)

string = "Hello world"
print(enumerate(string, 1))