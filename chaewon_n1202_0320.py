#백준 n1202 골드2 보석 도둑


#2:24pm 문제 풀이 시작
#가방에 최대 한개의 보석만 넣을 수 있다 -> 비싼거부터 넣어야 할듯 -> 각 가방에 들어갈 수 있는 보석 목록을 찾고, 그 중에서 가장 비싼걸 넣자 
#2:46pm 시도-> 시간초과 -> 리스트 말고 다른걸 써야하나? 생각
#3:30 최소힙과 데큐 사용해봄 -> 시간초과


#4:06 최소힙 최대힙 사용해서 최대한 연산 줄임 -> 통과


import sys
import heapq as hp 
from collections import deque
def thief() :
    answer = 0
    #입력 받기
    N, K = map(int, sys.stdin.readline().split()) #보석 개수, 가방 개수 
    arr = list( list(map(int, sys.stdin.readline().split())) for _ in range(N))
    bag = list( int(sys.stdin.readline()) for _ in range(K))
    hp.heapify(arr)
    hp.heapify(bag)
    d = []
    hp.heapify(d)

    while bag :
        b = hp.heappop(bag) #가장 작은 가방부터 꺼냄    
        while arr  : #각 가방마다 검사 시작
            if arr[0][0] <= b : 
                m, v = hp.heappop(arr)
                hp.heappush(d, [-v,-m])
            else : 
                break 
    
        if d : 
            v, m = hp.heappop(d)
            answer -= v
           
    return answer
print(thief())


