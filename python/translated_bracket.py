from collections import deque

def balanced_st(w):
    o,c=0,0
    for i in range(len(w)):
        if w[i]=='(':
            o+=1
        else:
            c+=1
        if o==c:
            return w[:i+1],w[i+1:]
    return w,''

def corrected_st(st):
    q=deque()
    for s in st:
        if s=='(':
            q.append(s)
        else:
            if not q:
                return False
            q.pop()    
    return True
        

def solution(p):
    answer = ''
    if len(p)==0:
        return ''
    u,v=balanced_st(p)
    if corrected_st(u):
        return u+solution(v)
    else:
        answer=''
        answer+='('+solution(v)+')'
        for i in range(1,len(u)-1):
            if u[i]=='(':
                answer+=')'
            else:
                answer+='('
        return answer
    return answer