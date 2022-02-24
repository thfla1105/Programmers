from collections import deque
from itertools import product

def solution(board, skill):
    answer = 0
    row=len(board)
    col=len(board[0])
    rc_board=[[i for i in range(row)],[j for j in range(col)]]
    result= set(product(*rc_board))
    for s in skill:
        tp,r1,c1,r2,c2,degree=s[0],s[1],s[2],s[3],s[4],s[5]
        rc=[[i for i in range(r1,r2+1)],[j for j in range(c1,c2+1)]]
        q=set(product(*rc))
        if tp==1:
            degree=-1*degree
        while q:
            tmp=q.pop()
            board[tmp[0]][tmp[1]]+=degree
            if tmp not in result and board[tmp[0]][tmp[1]]>0:
                result.add(tmp)
            if tmp in result and board[tmp[0]][tmp[1]]<=0:
                result.remove(tmp)
    
    answer=len(result)
        
    return answer