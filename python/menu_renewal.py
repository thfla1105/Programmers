from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        order=[]
        for o in orders:
            com=combinations(sorted(o),c)
            order+=com
        cnt = Counter(order)
        if len(cnt)!=0 and max(cnt.values())!=1:
            for t in cnt:
                if(cnt[t]==max(cnt.values())):
                    answer.append(str(''.join(t)))

    return sorted(answer)