#백준 18870 실버2
#좌표 압축
import sys

def z() :
    N = int(input())
    d = {}
    point = list(map(int, sys.stdin.readline().split()))
    sortpoint = sorted(set(point))
    idx = 0
    for p in sortpoint :
        if p not in d :
            d[p] = idx
            idx += 1
    
    return ' '.join(list(str(d[x]) for x in point))


print(z())