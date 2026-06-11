# import ast
# arr = ast.literal_eval(input())
# k = int(input())
# result = sorted(set(arr), reverse=True)[k - 1]
# print(result)


#  Number 2 way

import ast

arr = ast.literal_eval(input())
k = int(input())
print(sorted(set(arr), reverse=True)[k - 1])
