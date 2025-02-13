def correct_word(s):
    # Count uppercase and lowercase letters
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = len(s) - upper_count
    
    # Determine the correct case
    if upper_count > lower_count:
        return s.upper()
    else:
        return s.lower()

# Input section
s = input()

# Calculate and display the result
result = correct_word(s)
print(result)
