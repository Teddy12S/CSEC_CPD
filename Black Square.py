def total_calories(a, s):
    total = 0
    for char in s:
        total += a[int(char) - 1]  # Convert char to index for calories
    return total

# Input section
a = list(map(int, input().split()))
s = input().strip()

# Calculate and display the result
result = total_calories(a, s)
print(result)
