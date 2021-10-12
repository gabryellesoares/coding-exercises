# problem 25A

input()
numbers = [int(n) % 2 for n in input().split()]

print(numbers.index(sum(numbers) == 1) + 1)
