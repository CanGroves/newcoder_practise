'''
题目描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述:
输入一个正浮点数值

输出描述:
输出该数值的近似整数值

示例1
输入
5.5
输出
6
'''

import sys

input_num = sys.stdin.readline().strip()
num = float(input_num)

rest_num = num - int(num)
rest = 0
if rest_num >= 0.5:
    rest = 1
    
ans = int(num) + rest
print(ans)