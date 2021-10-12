n, m = map(int, input().split())

for i in range(n):
    out = ""
    line = input()

    for j in range(len(line)):
        if line[j] == ".":
            if (i+j) % 2 == 0:
                out += "B"
            else:
                out += "W"
        else:
            out += "-"
    print(out)
