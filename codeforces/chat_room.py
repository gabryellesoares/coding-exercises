i = 0

for l in input():
    if i > 4:
        break
    if "hello"[i] == l:
        i += 1

print("YES" if i == 5 else "NO")
