def check(ans):
    for x,y,a in ans:
        if a==0:
            if y==0 or (x,y-1,0) in ans or (x,y,1) in ans or (x-1,y,1) in ans:
                continue
            else:
                return False
        else:
            if (x,y-1,0) in ans or (x+1,y-1,0) in ans or ((x+1,y,1) in ans and (x-1,y,1) in ans):
                continue
            else:
                return False
    
    return True


def solution(n, build_frame):
    answer = set()
    
    for dx,dy,a,b in build_frame:
        xya=(dx,dy,a)
        if b==1:
            answer.add(xya)
            if not check(answer):
                answer.remove(xya)
        else:
            answer.remove(xya)
            if not check(answer):
                answer.add(xya)
    
    answer=[list(ans) for ans in answer]
    answer.sort(key=lambda x:(x[0],x[1],x[2]))
    return answer