'''
题目描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

输入描述:
输入一个int型整数

输出描述:
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

示例1
输入
9876673
输出
37689
'''

import sys

input_num = sys.stdin.readline().strip()
ans_list = list()
for i in range(len(input_num)-1, -1, -1):
    if input_num[i] not in ans_list:
        ans_list.append(input_num[i])
        
for n in ans_list:
    print(n, end='')