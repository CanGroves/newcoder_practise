'''
题目描述
输入一个int型的正整数，计算出该int型数据在内存中存储时1的个数。

输入描述:
 输入一个整数（int类型）

输出描述:
 这个数转换成2进制后，输出1的个数

示例1
输入
5
输出
2
'''

import sys

input_num = sys.stdin.readline().strip()

def ten_to_two(num_ten):
    count = 0
    while(num_ten != 1):
        mod = num_ten % 2
        if mod == 1:
            count += 1
        num_ten = int(num_ten /2)
    count += 1
    return count

print(ten_to_two(int(input_num)))


'''
ref using bin():

num = int(input())
print(bin(num).count('1'))
'''