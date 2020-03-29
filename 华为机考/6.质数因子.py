'''
题目描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（如180的质因子为2 2 3 3 5 ）

最后一个数后面也要有空格

详细描述：

函数接口说明：

public String getResult(long ulDataInput)

输入参数：

long ulDataInput：输入的正整数

返回值：

String

输入描述:
输入一个long型整数

输出描述:
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入
180
输出
2 2 3 3 5
'''

'''
学过，忘了，ref1:
该整数为x答案序列为ans，初始为空从2枚举到根号x(向下取整)，当前枚举到的数为i;若i是x的因子，则将i加入ans中，并不断将x除以i，直至i不是x的因子若循环结束后x不为1，则说明当前x是最后一个素因子，于是将x加入ans中ans中即为x的所有素因子。时间复杂度为sqrt(x)。
作者：Apale
链接：https://www.zhihu.com/question/353400503/answer/877281873

ref2:
思路：
本题是正整数n的质因子分解问题。n分为3种情况：

1、n=1，特殊数据，既不是质数也不能分解，直接按指定格式输出即可。
2、n是素数，不用分解，直接按指定格式输出即可。要判别n是否为质数，有多种方法，对于本题而言，最简单的方法是使用试商法。因为即使对于n=2147483647=2^31-1范围内的整数，用试商法效率也是很高的，具体参见下面给出的代码。
3、n是大于1的非质数，这正是本题要完成的工作。可以从最小的素数2开始，依次用2,3,4，5，...,sqrt(n)对n进行分解。因为当对2进行分解时，后面关于2的倍数的其他数字也就不能被n整除了，因此也就只对质数的进行计算，记得每次结束某个数字的因式分解之后，更新一下sqrt(n)。
当然，可以考虑采用筛法，事先把一定范围内的质数全部筛选出来，存入数组，然后只用这些质数去分解n，效率会相应提高很多。
（4）本题还有一点需要注意，即打印的格式。
'''

import sys

def prime_div(num):
    ans = list()
    for i in range(2,int(num**0.5)+1):
        while num % i == 0:
            ans.append(i)
            num = num / i
    if num!= 1:
        ans.append(int(num))
    ans.sort()
    return ans

input_num = sys.stdin.readline().strip()
ans = prime_div(int(input_num))
for a in ans:
    print(a, end = ' ')  #mark: arg "end" defalut='\n' i.e.换行，则改为end = ' ' 便不会换行 而是以空格结尾

'''
#ref3:
import math
def divide2prime(n):
    a = []
    for i in range(2,math.ceil(math.sqrt(n))):
        while n%i == 0:
            n=n/i
            a.append(i)
    if n:a.append(int(n))
    return a
 
n = int(input())
ans = divide2prime(n)
for i in ans:
    print(i,end = ' ')
'''
