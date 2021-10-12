# problem 268A

teams = []
num = 0

for team in range(int(input())):
    teams.append(input().split())

for i in range(len(teams)):
    for j in range(len(teams)):
        if teams[i][0] == teams[j][1]:
            num += 1

print(num)
