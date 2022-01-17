
def solution(play_time, adv_time, logs):
    answer = ''
    play_sec=str_to_int(play_time)
    adv_sec=str_to_int(adv_time)
    logs_sec=[[str_to_int(y) for y in x.split('-')] for x in logs]
    all_sec=[0]*(play_sec+1)
    
    sorted(logs_sec)
    
    for log in logs_sec:
        all_sec[log[0]]=all_sec[log[0]]+1
        all_sec[log[1]]=all_sec[log[1]]-1
        
    for p in range(1,play_sec+1):
        all_sec[p]=all_sec[p]+all_sec[p-1]
    
    for p in range(1,play_sec+1):
        all_sec[p]=all_sec[p]+all_sec[p-1]
    
    
    answer=int_to_str(idx)
    return answer


def str_to_int(time):
    hh,mm,ss=time.split(":")
    second=int(hh)*3600+int(mm)*60+int(ss)
    return second

def int_to_str(second):
    mm, ss = divmod(second, 60)
    hh, mm = divmod(mm, 60)
    time='{}:{:0>2}:{:0>2}'.format(hh, mm, ss)
    return time
    