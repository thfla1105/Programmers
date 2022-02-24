def solution(board, skill):
    answer = 0
    row=len(board)
    col=len(board[0])
    building=[[0 for _ in range(col+1)] for _ in range(row+1)]
    for tp,r1,c1,r2,c2,degree in skill:
        if tp==1:
            degree=-1*degree
        building[r1][c1]+=degree
        building[r1][c2+1]-=degree
        building[r2+1][c1]-=degree
        building[r2+1][c2+1]+=degree
    
    for j in range(col):
        for i in range(row):
            building[i+1][j]+=building[i][j]
    
    for i in range(row):
        for j in range(col):
            building[i][j+1]+=building[i][j]
            
    for i in range(row):
        for j in range(col):
            board[i][j]+=building[i][j]
            if board[i][j]>0:
                answer+=1
        
        
    return answer