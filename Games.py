def count_guest_uniform_games(n, teams):
    count = 0
    
    for i in range(n):
        home_color = teams[i][0]  # Home uniform color of team i
        for j in range(n):
            if i != j:  # Only consider games between different teams
                guest_color = teams[j][1]  # Guest uniform color of team j
                if home_color == guest_color:
                    count += 1  # Host team i wears guest uniform for team j's game
    
    return count

# Input section
n = int(input())
teams = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and display the result
result = count_guest_uniform_games(n, teams)
print(result)
