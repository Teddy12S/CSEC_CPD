def y_l(a, b):
    years = 0  
 
    
    while a <= b:
        a *= 3  
        b *= 2 
        years += 1  
 
    return years
 
 
a, b = map(int, input().split())
 
 
result = y_l(a, b)
print(result)
