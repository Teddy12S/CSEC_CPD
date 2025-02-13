def game_score(n, cards):
    sereja_score = 0
    dima_score = 0
    left, right = 0, n - 1
    turn = 0  # 0 for Sereja, 1 for Dima

    while left <= right:
        if cards[left] > cards[right]:
            chosen_card = cards[left]
            left += 1
        else:
            chosen_card = cards[right]
            right -= 1
        
        if turn == 0:  # Sereja's turn
            sereja_score += chosen_card
        else:  # Dima's turn
            dima_score += chosen_card
        
        turn = 1 - turn  # Switch turns

    return sereja_score, dima_score

# Input section
n = int(input())
cards = list(map(int, input().split()))

# Calculate and display the result
result = game_score(n, cards)
print(result[0], result[1])
