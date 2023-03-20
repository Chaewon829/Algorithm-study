#n2108

#11:00 시작


import sys
import math
from collections import Counter
def mainfunc() :
    N = int(input())
    num = list( int(input()) for _ in range(N))
    print(round(sum(num)/N)) #1. 산술평균
    num.sort()
    print(num[N//2]) #2.중앙값
    counter = Counter(num)
    common = counter.most_common(2)
    if len(common)==1 : print(common[0][0])
    else : 
        if common[0][1]==common[1][1] : print(common[1][0])
        else : print(common[0][0])
    print(num[-1] - num[0])
mainfunc()