'''
题目描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)，换行表示结束符，不算在字符里。不在范围内的不作统计。

输入描述:
输入N个字符，字符在ACSII码范围内。

输出描述:
输出范围在(0~127)字符的个数。

示例1
输入
abc
输出
3
'''

'''
不知道python如何取字符的ACSII码
try1:
import sys

input_str = sys.stdin.readline().strip()
count = 0
for s in input_str:
    if int(s) >= 0 and int(s) <= 127:
        count += 1
print(count)
审错题了。。尴尬：计算字符串中含有的不同字符的个数+不在范围内(0~127)的不作统计，忘记条件1了。。
'''

import sys

input_str = sys.stdin.readline().strip()
count = 0
str_exist = list()
for s in input_str:
    if s not in str_exist and int(ord(s)) >= 0 and int(ord(s)) <= 127:
        str_exist.append(s)
        count += 1
print(count)

'''
ref:
inputString = input()
count = 0
stringArr = []
for i in range(len(inputString)):
    if inputString[i] not in stringArr:
        stringArr.append(inputString[i])
for i in range(len(stringArr)):
    if int(ord(stringArr[i])) < 127 and int(ord(stringArr[i]) > 0):
        count = count + 1
print(count)

知识点：
Python ord() 函数
Python 内置函数

描述
ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

语法
以下是 ord() 方法的语法:

ord(c)
参数
c -- 字符。
返回值
返回值是对应的十进制整数。
'''