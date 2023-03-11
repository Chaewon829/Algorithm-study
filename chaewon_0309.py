#가장 큰 정사각형 찾기
#DP- 동적계획법
def solution(board):
    answer = 0
    if len(board) == 1 : return 1
    for i in range(1,len(board)) :
        for j in range(1,len(board[0])) :
            if board[i][j] :
                board[i][j] = min([board[i-1][j-1],board[i-1][j],board[i][j-1]]) +1 
                answer = max(answer, board[i][j])                
    return answer**2