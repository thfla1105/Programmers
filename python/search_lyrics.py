from bisect import bisect_left, bisect_right

def count_by_range(a,left_val,right_val):
    left_idx=bisect_left(a,left_val)
    right_idx=bisect_right(a,right_val)
    return right_idx-left_idx

def solution(words, queries):
    answer = []
    word=[[] for _ in range(100001)]
    reverse_word=[[] for _ in range(100001)]
    
    for w in words:
        word[len(w)].append(w)
        reverse_word[len(w)].append(w[::-1])
        
    for i in range(100001):
        word[i].sort()
        reverse_word[i].sort()
        
    for q in queries:
        num=0
        if q[0]=='?':
            if not reverse_word[len(q)]:
                answer.append(0)
                continue
            num=count_by_range(reverse_word[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','z'))
        else:
            if not word[len(q)]:
                answer.append(0)
                continue
            num=count_by_range(word[len(q)],q.replace('?','a'),q.replace('?','z'))
                    
        answer.append(num)
                    
        
    return answer