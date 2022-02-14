from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def move(a,b,graph):
    pos=[]
    for i in range(4):
        na=(a[0]+dy[i],a[1]+dx[i])
        nb=(b[0]+dy[i],b[1]+dx[i])
        if graph[na[0]][na[1]]==0 and graph[nb[0]][nb[1]]==0:
            pos.append((na,nb))
            
    if a[0]==b[0]:
        for i in [1,-1]:
            if graph[a[0]+i][a[1]]==0 and graph[b[0]+i][b[1]]==0:
                pos.append((a,(a[0]+i,a[1])))
                pos.append((b,(b[0]+i,b[1])))
    else:
        for i in [1,-1]:
            if graph[a[0]][a[1]+i]==0 and graph[b[0]][b[1]+i]==0:
                pos.append(((a[0],a[1]+i),a))
                pos.append(((b[0],b[1]+i),b))
    return pos
                
    

def solution(board):
    answer = 0
    n=len(board)
    graph=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            graph[i+1][j+1]=board[i][j]
    q=deque([((1,1),(1,2),0)])
    visited=set([((1,1),(1,2))])    
    while q:
        a,b,result=q.popleft()
        if a==(n,n) or b==(n,n):
            answer=result
            break
        for k in move(a,b,graph):
            if k not in visited:
                q.append((*k,result+1))
                visited.add(k)
    return answer