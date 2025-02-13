def untreated_crimes(n, events):
    officers = 0
    untreated = 0
    
    for event in events:
        if event == -1:  # A crime has occurred
            if officers > 0:
                officers -= 1  # An officer investigates the crime
            else:
                untreated += 1  # No officers available, crime goes untreated
        else:  # Officers are recruited
            officers += event
    
    return untreated

# Input section
n = int(input())
events = list(map(int, input().split()))

# Calculate and display the result
result = untreated_crimes(n, events)
print(result)
