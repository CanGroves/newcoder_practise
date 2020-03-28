'''
计算字符串最后一个单词的长度，单词以空格隔开。
输入描述:
一行字符串，非空，长度小于5000。

输出描述:
整数N，最后一个单词的长度。

示例1
输入
hello world
输出
5
'''

str_list = list(str(input()).split())
str_last = str_list[-1]
last_len = len(str_last)
print(last_len)