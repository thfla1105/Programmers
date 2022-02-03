from collections import defaultdict
from bisect import bisect_left, bisect_right

def count_by_range(a,left_val,right_val):
    left_idx=bisect_left(a,left_val)
    right_idx=bisect_right(a,right_val)
    return right_idx-left_idx

def solution(words, queries):
    answer = []
    word=defaultdict(list)
    reverse_word=defaultdict(list)
    for w in words:
        word[len(w)].append(w)
        reverse_word[len(w)].append(w[::-1])
    for w in words:
        word[len(w)].sort()
        reverse_word[len(w)].sort()
    for q in queries:
        num=0
        if q[0]=='?':
            num=count_by_range(reverse_word[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        else:
            num=count_by_range(word[len(q)],q.replace('?','a'),q.replace('?','z'))
                    
        answer.append(num)
                    
        
    return answer

