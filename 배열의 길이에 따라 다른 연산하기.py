def solution(arr, n):
    answer = []
    remain = 0
    
    if len(arr)%2 == 0:
        remain = 1
    
    for i, v in enumerate(arr):
        if i%2 == remain :
            v = v+n
        answer.append(v)
    
    return answer