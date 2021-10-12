def equiv(s):
    if len(s) % 2 == 1:
        return s
    n = len(s) // 2
    a = equiv(s[:n])
    b = equiv(s[n:])

    return a + b if a < b else b + a


a = input()
b = input()
print("YES" if equiv(a) == equiv(b) else "NO")
