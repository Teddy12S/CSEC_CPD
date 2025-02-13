def min_stones_to_remove(n, s):
    count = 0
    for i in range(1, n):
        if s[i] == s[i - 1]:  # Check if the current stone is the same as the previous one
            count += 1
    return count

# Input section
n = int(input())
s = input().strip()

# Calculate and display the result
result = min_stones_to_remove(n, s)
print(result)
