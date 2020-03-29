'''
题目描述
数据表记录包含表索引和数值（int范围的整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
4
0 1
0 2
1 2
3 4
输出
0 3
1 2
3 4
'''

import sys

num = sys.stdin.readline().strip()
input_dic = dict()
for i in range(int(num)):
    #try:
    input_pair = sys.stdin.readline().strip()
    # print(type(input_pair))
    # mark a mistake :input_pair = list(sys.stdin.readline().strip()),
    # list没有split()方法，且输入的tyoe为str，str可split()
    key, value = input_pair.split()
    key = int(key)
    value = int(value)
    if key in input_dic.keys():
        input_dic[key] = input_dic[key] + value
    else:
        input_dic [key] = value
    #except:
    #    print('input error!')
        
sorted(input_dic.items(), key=lambda item : item[0])

for k in input_dic.keys():
    print(k, input_dic[k]) # mark a mistake: print(k, ' ', input_dic[k]):去掉中间的空格，因为print( , )本身会以空格为间隔


