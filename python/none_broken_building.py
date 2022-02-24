from collections import deque
from itertools import product

def solution(board, skill):
    answer = 0
    for s in skill:
        tp,r1,c1,r2,c2,degree=s[0],s[1],s[2],s[3],s[4],s[5]
        rc=[[i for i in range(r1,r2+1)],[j for j in range(c1,c2+1)]]
        q=deque(product(*rc))
        if tp==1:
            degree=-1*degree
        while q:
            tmp=q.popleft()
            board[tmp[0]][tmp[1]]+=degree
    
    for x in board:
        for y in x:
            if y>0:
                answer+=1
        
    return answer