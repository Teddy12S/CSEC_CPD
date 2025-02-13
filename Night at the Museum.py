def min_rotations(name):
    current_position = ord('a')  # Starting position at 'a'
    total_rotations = 0
    
    for char in name:
        target_position = ord(char)  # ASCII value of the target character
        
        # Calculate the direct distance (clockwise and counterclockwise)
        clockwise_distance = (target_position - current_position) % 26
        counterclockwise_distance = (current_position - target_position) % 26
        
        # Add the minimum of the two distances to the total rotations
        total_rotations += min(clockwise_distance, counterclockwise_distance)
        
        # Update the current position to the target character
        current_position = target_position
    
    return total_rotations

# Input section
exhibit_name = input().strip()

# Calculate and display the result
result = min_rotations(exhibit_name)
print(result)
