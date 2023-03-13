#백준 2206 벽 부수고 이동하기 
#최단거리 최소이동 bfs
from collections import deque

def move(N,M,arr) :
    m = [[1,0],[0,1],[-1,0],[0,-1]]
    q = deque() 
    q.append([0,0,1,1]) # x, y,이동한 칸(시작지점 포함이므로 1부터 시작), 벽 남은 횟수
    visited = list(arr for i in range(2))
    visited[0][0][0] = 1 
    while q : 
        x, y, jump, wall = q.popleft()
        if x == M-1 and y == N-1 : return jump
        else : 
            for i in range(4) :
                x_n = x + m[i][0]
                y_n = y + m[i][1]
                if x_n >= 0 and x_n < M and y_n >= 0 and y_n < N : #보드 위
                    if visited[wall][y_n][x_n] == 0 : #벽없음
                        q.append([x_n,y_n,jump+1, wall])
                        visited[wall][y_n][x_n] = 1 #방문처리
                    else : #벽있음
                        if wall : #부술 기회 남음 
                            q.append([x_n, y_n, jump+1, 0])
                            visited[0][y_n][x_n] = 1
    return -1

print("input :")
N, M = map(int, input().split())
arr = list(list(map(int, list(input()))) for _ in range(N))
print(move(N,M,arr))