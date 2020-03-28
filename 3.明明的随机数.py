'''
题目描述
明明想在学校中请一些同学一起做一项问卷调查，为了实验的客观性，他先用计算机生成了N个1到1000之间的随机整数（N≤1000），对于其中重复的数字，只保留一个，把其余相同的数去掉，不同的数对应着不同的学生的学号。然后再把这些数从小到大排序，按照排好的顺序去找同学做调查。请你协助明明完成“去重”与“排序”的工作(同一个测试用例里可能会有多组数据，希望大家能正确处理)。

Input Param

n               输入随机数的个数

inputArray      n个随机整数组成的数组

Return Value

OutputArray    输出处理后的随机整数

注：测试用例保证输入参数的正确性，答题者无需验证。测试用例不止一组。

样例输入解释：
样例有两组测试
第一组是3个数字，分别是：2，2，1。
第二组是11个数字，分别是：10，20，40，32，67，40，20，89，300，400，15。

输入描述:
输入多行，先输入随机整数的个数，再输入相应个数的整数

输出描述:
返回多行，处理后的结果
'''


'''
错误示范：（主要在于每组都分别算（对）还是全部组合在一起算（错）的区别。。有歧义。。吐血。。）
import sys
numbers = list()
while(1):    
    num = sys.stdin.readline().strip()
    if num is None or num == '':
        break
    num = int(num)
    for i in range(num):
        numbers.append(int(sys.stdin.readline().strip()))
        
set_num = set(numbers)
print('set nums',set_num)
list_num_sorted = sorted(list(set_num))  # mark a mistake: list_num_sorted = list(set_num).sort() ; sort()方法是对原list进行修改，本身只返回None，要用也是要写成:list_num = list(set_num) ; list_num.sort() ; using list_num
print('list_num_sorted',list_num_sorted)
for n in list_num_sorted:
    print(n)
'''

import sys

while(1):    
    try:
        numbers = list()
        num = sys.stdin.readline().strip()
        num = int(num)
        for i in range(num):
            a = sys.stdin.readline().strip()
            numbers.append(int(a))
        set_num = set(numbers)
        #print('set nums',set_num)
        list_num_sorted = sorted(list(set_num))  # mark a mistake: list_num_sorted = list(set_num).sort() ; sort()方法是对原list进行修改，本身只返回None，要用也是要写成:list_num = list(set_num) ; list_num.sort() ; using list_num
        #print('list_num_sorted',list_num_sorted)
        for i in list_num_sorted:
            print(i)
    except:
        break

'''
ref:
while True:
    try:
 
        a,res=int(input()),set()
        for i in range(a):res.add(int(input()))
        for i in sorted(res):print(i)
 
 
    except:
        break
'''