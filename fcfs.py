def fcfs(requests,head):
    s=[]
    total_head_moment=0
    for request in requests:
        total_head_moment+=abs(head-request)
        head=request
        s.append(request)
    return total_head_moment,s
if __name__=="__main__":
    requests=[42,53,75,61,21,3]
    head=50
    total_head_moment,s=fcfs(requests,head)
    print(total_head_moment)
    print(s)