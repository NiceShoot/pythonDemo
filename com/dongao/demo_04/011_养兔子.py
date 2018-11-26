"""
    题目 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

    程序分析 我认为原文的解法有点扯，没有考虑3个月成熟的问题，人家还是婴儿怎么生孩子？考虑到三个月成熟，可以构建四个数据，
    其中：一月兔每个月长大成为二月兔，二月兔变三月兔，三月兔变成年兔，成年兔（包括新成熟的三月兔）生等量的一月兔。
"""


def fun(x):
    if x == 1 or x == 2:
        return 2
    else:
        return fun(x - 1) + fun(x - 2)


month = int(input("请输入要繁殖的月数："))
for i in range(month):
    print('第%d个月共' % (i + 1), fun(i + 1), '对兔子')
