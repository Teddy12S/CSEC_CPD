def final_position(s, t):
    position = 0  # Starting position (0-based index)
    
    for instruction in t:
        if position < len(s) and s[position] == instruction:
            position += 1  # Move to the next stone if the color matches
    
    return position + 1  # Convert to 1-based index

# Input section
s = input().strip()
t = input().strip()

# Calculate and display the result
result = final_position(s, t)
print(result)
