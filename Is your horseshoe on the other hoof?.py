def min_horseshoes_to_buy(horseshoe_colors):
    unique_colors = set(horseshoe_colors)  # Get unique colors
    return 4 - len(unique_colors)  # Calculate how many more are needed

# Input section
horseshoe_colors = list(map(int, input().split()))

# Calculate and display the result
result = min_horseshoes_to_buy(horseshoe_colors)
print(result)
