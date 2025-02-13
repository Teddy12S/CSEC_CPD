from math import gcd

def probability(Y, W):
    # Determine the maximum points rolled by Yakko and Wakko
    max_roll = max(Y, W)
    
    # Dot needs to roll at least max_roll to win
    successful_outcomes = 6 - max_roll + 1  # Count of winning rolls (max_roll, ..., 6)
    
    # Total outcomes on a die
    total_outcomes = 6
    
    # Reduce the fraction
    numerator = successful_outcomes
    denominator = total_outcomes
    divisor = gcd(numerator, denominator)
    
    # Format the result as irreducible fraction
    return f"{numerator // divisor}/{denominator // divisor}"

# Input section
Y, W = map(int, input().split())

# Calculate and display the result
result = probability(Y, W)
print(result)
