def gravity_flip(num_columns, cubes):
    
    return sorted(cubes)
 
 
num_columns = int(input())
cubes = list(map(int, input().split()))
 
 
result = gravity_flip(num_columns, cubes)
print(" ".join(map(str, result)))
