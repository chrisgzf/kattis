input()
temps = [int(n) for n in input().split()]
num = 0

for x in temps:
    if x < 0:
        num += 1

print(num)
