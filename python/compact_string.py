def solution(s):
    answer = 1000
    if len(s)==1:
        answer=1
        return answer
    for i in range(1,len(s)//2+1):
        fragment=[s[j:j+i] for j in range(0,len(s),i)]
        compact=''
        cnt=1
        for k in range(1,len(fragment)):
            if fragment[k]==fragment[k-1]:
                cnt+=1
            else:
                if cnt!=1:
                    c=cnt
                    compact+=str(c)+fragment[k-1]
                else:
                    compact+=fragment[k-1]
                cnt=1
        if cnt!=1:
            c=cnt
            compact+=str(c)+fragment[len(fragment)-1]
        else:
            compact+=fragment[len(fragment)-1]
        if len(compact)<answer:
            answer=len(compact)
    return answer