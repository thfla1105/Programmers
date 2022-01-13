import heapq

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
    
    distance[s]=0
    
    queue=[]
    heapq.heappush(queue,[distance[s],s])
    
    while queue:
        tmp_dist,tmp_dest=heapq.heappop(queue)
        if distance[tmp_dest]<tmp_dist:
            continue
        for next_dest,next_dist in graph[tmp_dest].items():
            dist = tmp_dist+next_dist
            if dist < distance[next_dest]:
                distance[next_dest]=dist
                heapq.heappush(queue,[dist,next_dest])
                
    return distance
            