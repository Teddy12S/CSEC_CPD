def d_w(n, s):
   
    a_wins = s.count('A')  
    d_wins = s.count('D')  
 
  
    if a_wins > d_wins:
        return "Anton"
    elif d_wins > a_wins:
        return "Danik"
    else:
        return "Friendship"
 
 
n = int(input())
s = input()
 
 
result = d_w(n, s)
print(result)
