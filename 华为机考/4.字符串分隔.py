'''
题目描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述:
连续输入字符串(输入2次,每个字符串长度小于100)

输出描述:
输出到长度为8的新字符串数组

示例1
输入
abc
123456789
输出
abc00000
12345678
90000000
'''

import sys

outs = list()

def part(in_str):
    global outs
    str_len = len(in_str)
    num = int(str_len / 8)
    remain_num = str_len % 8
    if num > 0:
        for i in range(1,num+1): #mark a mistake:range(num+1) will conut i=0 into case the append an empty str'' to outs
            outs.append(str(in_str[8*(i-1):8*i]))
            #print(outs)
    if remain_num != 0:
        make_up_str = str(in_str[8*num:]) + '0'*(8-remain_num)
        outs.append(make_up_str)
        #print(outs)
        
for i in range(2):
    input_str = sys.stdin.readline().strip()
    if input_str != '':
        part(input_str)
#print(outs)
for o in outs:
    print(o)