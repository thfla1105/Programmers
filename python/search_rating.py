from itertools import combinations
from collections import Counter

def split_st(q):
    st = q.replace('and','').split()
    score = int(st[-1])
    while '-' in st:
        st.remove('-')
    st.remove(st[-1])
    st.sort()
    st=str(''.join(st))
    return st,score

def solution(info, query):
    answer = []
    in_data={}
        
    for i in info:
        num=0
        it=i.split()
        for j in range(5):
            combi=list(combinations(sorted(it[:-1]),j))
            score = int(it[-1])
            for c in combi:
                tmp = ''.join(c)
                if tmp in in_data:
                    in_data[tmp].append(score)
                else:
                    in_data[tmp]=[score]
    
    for v in in_data.values():
        v.sort()        
        
    for q in query:
        st, score = split_st(q)
        if st in list(in_data):
            data = in_data[st]
            if len(data)>0:
                start,end=0, len(data)
                while start!=end and start!=len(data):
                    if int(data[(start+end)//2]) >= score:
                        end = (start+end) //2
                    else:
                        start = (start+end)//2+1
                answer.append(len(data)-start)
            else:
                answer.append(0)
    return answer