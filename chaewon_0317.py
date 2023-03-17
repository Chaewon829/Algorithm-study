#백준 1931 실버1 
#8:55pm 문제 풀기 시작

#일단 회의를 시작 순서로 정렬해 봐야될것같다
#순회하면서 조건 세워보자


import sys


def meet() :
    N = int(input())
    meetings = []
    for _ in range(N) :
       x, y = map(int, sys.stdin.readline().split())
       meetings.append([x,y])
    time = -1
    answer = 0
    meetings.sort()
    for start, end in meetings :
        if time <= start : #회의실 이용 가능 
            time = end
            answer += 1
        elif end < time :
            time = end
    return answer


print(meet())





