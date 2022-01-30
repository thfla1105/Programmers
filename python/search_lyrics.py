def solution(words, queries):
    answer = []
    for q in queries:
        st=q.split("?")
        num=0
        if st[0]=='':
            st=list(set(st))
            st.remove('')
            for w in words:
                if w.endswith(st[0]) and len(w)==len(q):
                    
                    num+=1
        
            answer.append(num)
        else:
            st=list(set(st))
            st.remove('')
            for w in words:
                if w.startswith(st[0]) and len(w)==len(q):
                    num+=1
                    
            answer.append(num)
                    
        
    return answer