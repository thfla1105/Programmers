from collections import deque

INF = int(1e9)

def solution(n, s, a, b, fares):
    answer = 0    
    graph={}
    for f in fares:
        if f[0] in graph:
            graph[f[0]][f[1]]=f[2]
        else:
            graph[f[0]]={f[1]:f[2]}
        if f[1] in graph:
            graph[f[1]][f[0]]=f[2]
        else:
            graph[f[1]]={f[0]:f[2]}

    a_dis = dijkstra(n,graph,a)
    b_dis = dijkstra(n,graph,b)
    s_dis = dijkstra(n,graph,s)
    
    min_d = INF
    for i in range(1,n+1):
        c = a_dis[i]+b_dis[i]+s_dis[i]
        if c<min_d and c<INF:
            min_d=c
    
    answer = min_d
    return answer

def dijkstra(n,graph,s):
    distance=[INF]*(n+1)
    visited=[False]*(n+1)
    
    distance[s]=0
    visited[s]=True
    
    for k,v in graph[s].items():
        distance[k]=v
        
    for i in range(n-1):
        min_v=INF
        tmp=0
        for l in range(1,n+1):
            if distance[l]<min_v and not visited[l]:
                min_v=distance[l]
                tmp=l

        visited[tmp]=True
        if tmp!=0:
            for key,value in graph[tmp].items():
                cost = distance[tmp] + value
                if cost < distance[key]:
                    distance[key]=cost
    
    return distance
            