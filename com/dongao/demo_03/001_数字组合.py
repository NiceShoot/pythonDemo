"""
    有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

# 方法一
# total = 0
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (j != k) and (i != k):
#                 print(i, j, k)
#                 total += 1
# print(total)

# 方法二
import itertools
arr = [1, 2, 3, 4]
count = 0
for i in itertools.permutations(arr, 3):
    print(i)
    count += 1
print("count = ", count)
for i in itertools.combinations(arr, 3):
    print(i)
