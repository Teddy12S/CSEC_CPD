def m_m(m):
    
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                
                return abs(i - 2) + abs(j - 2)
 
 
m = [list(map(int, input().split())) for _ in range(5)]
 
 
r = m_m(m)
print(r)
