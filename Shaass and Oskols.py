def update_bird_counts(n, bird_counts, shots):
    for x, y in shots:
        wire_index = x - 1  # Convert to 0-based index
        bird_position = y - 1  # Convert to 0-based index

        # Birds on the left jump to the upper wire
        if wire_index > 0:  # Check if there's an upper wire
            bird_counts[wire_index - 1] += bird_position

        # Birds on the right jump to the lower wire
        if wire_index < n - 1:  # Check if there's a lower wire
            bird_counts[wire_index + 1] += bird_counts[wire_index] - (bird_position + 1)

        # The wire where the bird was shot now has 0 birds
        bird_counts[wire_index] = 0

    return bird_counts

# Input section
n = int(input())
bird_counts = list(map(int, input().split()))
m = int(input())
shots = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate the final bird counts after all shots
final_counts = update_bird_counts(n, bird_counts, shots)

# Print the result
for count in final_counts:
    print(count)
