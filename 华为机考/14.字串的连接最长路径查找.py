'''
题目描述
给定n个字符串，请对n个字符串按照字典序排列。
输入描述:
输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
输出描述:
数据输出n行，输出结果为按照字典序排列的字符串。

示例1
输入
9
cap
to
cat
card
two
too
up
boat
boot
输出
boat
boot
cap
card
cat
to
too
two
up
'''

'''
python too easy
C++ ref:
#include "stdio.h"
#include "string.h"
#include "math.h"
#include "stdlib.h"
 
 
static char data[1000][100] = {0};
 
static int comp(void const* a, void const* b)
{
    char* da = (char*)a;
    char* db = (char*)b;
 
    int lena = strlen(da);
    int lenb = strlen(db);
    int i = 0;
    for (i = 0; i < lena && i < lenb; i++)
    {
        if (da[i] > db[i])
        {
            return 1;
        }
        else if (da[i] < db[i])
        {
            return -1;
        }
    }
    if (i < lena)
        return 1;
    if (i < lenb)
        return -1;
    return 0;
}
 
int main()
{
    int n = 0;
 
    scanf("%d", &n);
    int i = 0;
    while (n --)
    {
        scanf("%s", data[i ++]);
    }
 
    qsort(data,i, 100 * sizeof(char), comp);
 
    for (int j = 0; j < i; j++)
    {
        printf("%s\n",data[j]);
    }
    return 0;
}

C++ ref2:
#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;
 
bool compare(const string &s1, const string &s2) {
    return s1<s2;
}
 
int main(){
    int n;
    vector<string> result;
    while(cin >> n){
        while(n!=0){
            n--;
            string t;
            cin >> t;
            result.push_back(t);
        }
        sort(result.begin(),result.end(),compare);
        for(int i = 0;i<result.size();i++){
            cout << result[i] << endl;
        }
    }
}
'''