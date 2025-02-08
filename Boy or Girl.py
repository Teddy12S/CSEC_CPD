def b_o_g(username):
   
    distinct_chars = set(username)
    
    if len(distinct_chars) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


username = input()


result = b_o_g(username)
print(result)
