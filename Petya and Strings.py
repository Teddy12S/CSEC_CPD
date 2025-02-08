def g_f(n, a):
    
    return sorted(a)


n = int(input())
a = list(map(int, input().split()))


r = g_f(n, a)
print(" ".join(map(str, r)))
