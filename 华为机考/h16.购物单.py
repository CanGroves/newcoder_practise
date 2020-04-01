'''
题目描述
王强今天很开心，公司发给N元的年终奖。王强决定把年终奖用于购物，他把想买的物品分为两类：主件与附件，附件是从属于某个主件的，下表就是一些主件与附件的例子：
主件	附件
电脑	打印机，扫描仪
书柜	图书
书桌	台灯，文具
工作椅	无
如果要买归类为附件的物品，必须先买该附件所属的主件。每个主件可以有 0 个、 1 个或 2 个附件。附件不再有从属于自己的附件。王强想买的东西很多，为了不超出预算，他把每件物品规定了一个重要度，分为 5 等：用整数 1 ~ 5 表示，第 5 等最重要。他还从因特网上查到了每件物品的价格（都是 10 元的整数倍）。他希望在不超过 N 元（可以等于 N 元）的前提下，使每件物品的价格与重要度的乘积的总和最大。
    设第 j 件物品的价格为 v[j] ，重要度为 w[j] ，共选中了 k 件物品，编号依次为 j 1 ， j 2 ，……， j k ，则所求的总和为：
v[j 1 ]*w[j 1 ]+v[j 2 ]*w[j 2 ]+ … +v[j k ]*w[j k ] 。（其中 * 为乘号）
    请你帮助王强设计一个满足要求的购物单。
 



输入描述:
输入的第 1 行，为两个正整数，用一个空格隔开：N m

（其中 N （ <32000 ）表示总钱数， m （ <60 ）为希望购买物品的个数。）


从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q


（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
 



输出描述:
 输出文件只有一个正整数，为不超过总钱数的物品的价格与重要度乘积的总和的最大值（ <200000 ）。
示例1
输入
1000 5
800 2 0
400 5 1
300 5 1
400 3 0
500 2 0
输出
2200
'''
import sys
N, m = sys.stdin.readline().strip().split()
N, m = int(N), int(m)
N = N // 10 # 价格都是10的倍数，则除以10来节省计算时间
f = [0] * (N+1) # f[j]:花费j*10元时的最大价值量，def 价值量value:=sum(i:1~k) price[i]*w[i]
# 分组背包，每组有4种情况：0: 主件 1: 主件+附件1 2: 主件+附件2 3: 主件+附件1+附件2
# 【mark a mistake】：索引问题！！！m应该用m+1才对！之前觉得没有区别，还节约了一个空间，现在发现其实i的取值与index的取值要匹配才行！index作为主件的索引时是从1开始而不是从0开始的！！所以i也要从1开始才能与之匹配对应过来！！
money = [[0 for j in range(4)] for i in range(m+1)] # 每组的资金
value = [[0 for j in range(4)] for i in range(m+1)] # 每组的价值量


for i in range(1, m+1):
    price, weight, index = map(int, sys.stdin.readline().strip().split())
    price = price // 10 # mark a mistake: forget this!!!
    if index == 0:
        # 为主件，将【每个组合的】主件的钱和价值量更新进去（因为每个组合都包含主件1）
        for k in range(4):
            money[i][k] = money[i][k] + price
            value[i][k] = value[i][k] + price * weight
    elif money[index][0] == money[index][1]:
        # mark a mistake: 上一行的index之前写成了i，导致检查成了附件本身的moeny，
        # ps：然而不能单独买附件本身，所以所有附件的位置都应该为0才对
        # 为附件，且0:主件资金==1: 主件+附件1资金，说明附件1还没加进去，要在1和3情况中将附件1累加进去
        # 情况1
        money[index][1] = money[index][1] + price
        value[index][1] = value[index][1] + price * weight
        # 情况3
        money[index][3] = money[index][3] + price
        value[index][3] = value[index][3] + price * weight
    else:
        # mark a mistake: 上一行的else之前写成了elif money[index][0] == money[index][2]: ，还没理解为啥!!修改了i范围后，尝试把else换回elif，发现也可通过！
        # mark a mistake: 上一行的index之前写成了i，导致检查成了附件本身的moeny，
        # ps：然而不能单独买附件本身，所以所有附件的位置都应该为0才对
        # 为附件，且0:主件资金==2: 主件+附件2资金，说明附件2还没加进去，要在2和3情况中将附件2累加进去 error
        # 情况2
        money[index][2] = money[index][2] + price
        value[index][2] = value[index][2] + price * weight
        # 情况3
        money[index][3] = money[index][3] + price
        value[index][3] = value[index][3] + price * weight

# m: 加入购物车的物品的最大个数
for i in range(1, m+1):
    # N:购物总资金上限，【只能倒序遍历，因为背包的思维是可用空间从大到小，求当前每个子状态的最优，】
    # 【如果顺序遍历，背包容量变大，之前遍历的子状态的最优结论就被推翻了】
    for j in range(N, -1, -1):
        for k in range(4):
            if j >= money[i][k]:
                # 【将每组的购物资金 整体视为 一个容量，这样才不会出现主件重复放入的情况，这也是其他答案犯错的地方】
                # 【f[j]：表示总花费为j*10元时的最大价值量】
                f[j] = max(f[j], f[ j - money[i][k] ] + value[i][k])
                # 动态规划：f[j]取 不买这组的最大价值量 与 买了这组后的剩下的钱买得到的最大价值量+本组的价值量 中的较大值

print(f[N]*10)

'''
ref:
链接：https://www.nowcoder.com/questionTerminal/f9c6f980eeec43ef85be20755ddbeaf4
来源：牛客网
linjiexin
难点：1. 0-1背包的常规思路，放入附件进购物单时连带放入对应主键，会导致主键被重复放入
2. 对dp数组进行状态更新时，容量（这里的购物单总花费）需要倒序遍历，否则先前遍历的子状态最优总价值会失效
n,m=map(int,input().split())
f=[0]*n #购物单总价值
#分组背包，每组有四种情况，a.主件 b.主件+附件1 c.主件+附件2 d.主件+附件1+附件2
v=[[0 for i in range(4)] for j in range(m+1)] #每组的资金
w=[[0 for i in range(4)] for j in range(m+1)] #每组的重要度
 
n=n//10#价格为10的整数倍，节省时间
for i in range(1,m+1):
    x,y,z=map(int,input().split())
    x=x//10
    if z==0:
        # 主件，同时给每个组合初始化主件的金额跟重要度
        for t in range(4):
            v[i][t], w[i][t] = v[i][t]+x, w[i][t]+x* y
    elif v[z][1]==v[z][0]:#附件且a==b，意味着附件1没加入，这时候累加b跟d情况
        v[z][1],w[z][1] = v[z][1] + x, w[z][1] + x* y
        v[z][3],w[z][3] = v[z][3] + x, w[z][3] + x* y
    else:#附件且a!=b，意味着附件1加入了附件2没加入，这时候累加c跟d情况
        v[z][2], w[z][2] = v[z][2] + x, w[z][2] + x* y
        v[z][3], w[z][3] = v[z][3] + x, w[z][3] + x* y
# m:加入购物单的物品个数上限
for i in range(1, m+1):
    # n:购物总资金上限，只能倒序遍历，因为背包的思维是可用空间从大到小，求当前每个子状态的最优，
    # 如果顺序遍历，背包容量变大，之前遍历的子状态的最优结论就被推翻了
    for j in range(n, -1, -1):
        for k in range(4):
            if j >= v[i][k]:
                # 将每组的购物资金 整体视为 一个容量，这样才不会出现主件重复放入的情况，这也是其他答案犯错的地方
                # f[j]：表示总花费为j钱时的最大购物价值
                f[j] = max(f[j], f[j-v[i][k]]+w[i][k])
print(10*f[n])
'''