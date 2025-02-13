def count_groups(n, magnets):
    groups = 1  # Start with one group
    for i in range(1, n):
        if magnets[i] != magnets[i - 1]:  # If current magnet is different from the previous one
            groups += 1
    return groups

# Input section
n = int(input())
magnets = [input().strip() for _ in range(n)]

# Calculate and display the result
result = count_groups(n, magnets)
print(result)
