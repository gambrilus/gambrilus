s, n = list(map(int, input().split()))
c = []
space = 0
for i in range(n):
    c.append(int(input()))
c.sort()
result = 0
for a in range(len(c)):
    result += c[a]
    if result <= s:
        space += 1
print(space)
