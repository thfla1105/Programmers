from itertools import combinations
from collections import Counter

def split_st(q):
    st = q.split('and')
    sv = str(''.join(st))
    st = sv.split()
    return st

def solution(info, query):
    answer = []
    for q in query:
        st = split_st(q)
        num=0
        for i in info:
            check = True
            for k in range(len(st)-1):
                if st[k]!='-' and st[k] not in i:
                    check= False
            it = i.split()
            if check == True and int(st[-1])<=int(it[-1]):
                num+=1
        answer.append(num)
        
    return answer