n = int(input())

f = 1
s = 1
for _ in range(1, n-1):
    f, s = s, f+s

print(s)

