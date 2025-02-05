def n_p(n, problems):
    count = 0  
 
    
    for p in problems:
       
        if sum(p) >= 2:
            count += 1
 
    return count
 
 
n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]
 
 
result = n_p(n, problems)
print(result)
