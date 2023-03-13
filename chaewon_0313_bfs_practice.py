#백준 2206 벽 부수고 이동하기 
#최단거리 최소이동 bfs
from collections import deque
import sys
def move() :
    N, M = map(int, sys.stdin.readline().split())
    arr = [[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        s = sys.stdin.readline()
        for j in range(M):
            if s[j] == "1":
                arr[i][j] = 1
    mx = [1,-1,0,0]
    my = [0,0,1,-1]
    q = deque() 
    q.append([0,0,1,1]) # x, y,이동한 칸(시작지점 포함이므로 1부터 시작), 벽 남은 횟수
    visited = list(list(list(False for _ in range(M)) for _ in range(N)) for _ in range(2))
    visited[0][0][0] = True
    result = N * M + 1
    while q : 
        x,y,jump,wall = q.popleft()


        if x == M-1 and y == N-1 :  #target인지 검사
            return jump
         
        for i in range(4) :
            x_n = x + mx[i]
            y_n = y + my[i]


            if x_n < 0 or y_n < 0 or x_n >= M or y_n >= N : #보드 범위 벗어남 
                continue
            
            if wall == 0 : #벽 부술 기회 없음 
                    if not visited[1][y_n][x_n] and arr[y_n][x_n]==0  : #벽이 없으면
                        visited[1][y_n][x_n] = True #방문처리
                        q.append([x_n,y_n,jump+1,0])

            else : # 벽 부술 기회 남음 :
                if not visited[0][y_n][x_n] :                   
                    if not arr[y_n][x_n] : #벽이 아니면 그냥 감
                        q.append([x_n, y_n, jump+1, 1])
                        visited[0][y_n][x_n] = True #방문 처리
                    else : 
                        q.append([x_n, y_n, jump+1, 0])   #벽이면 부수고 감
                        visited[1][y_n][x_n] = True #방문 처리

    return -1

# print("input :")
# N, M = map(int, input().split())
# arr = list(list(map(int, list(input()))) for _ in range(N))
print(move())