def solution(words, queries):
    answer = []
    word={w for w in words}
    word=sorted(word)
    for q in queries:
        st=q.split("?")
        num=0
        if st[0]=='':
            s=st[-1]
            for w in word:
                if w.endswith(s) and len(w)==len(q):
                    num+=1
                    
            answer.append(num)
        else:
            s=st[0]
            for w in word:
                if w.startswith(s) and len(w)==len(q):
                    num+=1
                    
            answer.append(num)
                    
        
    return answer