"""
题目 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

程序分析 学会分解出每一位数,用字符串的方法总是比较省事。
"""

n = int(input('输入一个正整数：'))
n = str(n)
print('%d位数' % len(n))
print(n[::-1])
