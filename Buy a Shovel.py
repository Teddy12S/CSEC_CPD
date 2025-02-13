def min_shovels(k, r):
    for n in range(1, 11):  # Check for 1 to 10 shovels
        total_cost = n * k
        if total_cost % 10 == 0 or total_cost % 10 == r:
            return n  # Return the minimum number of shovels needed

# Input section
k, r = map(int, input().split())

# Calculate and display the result
result = min_shovels(k, r)
print(result)
