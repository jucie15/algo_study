n = int(input())

prev = 1
cur = 1
tmp = 1

for i in range(n-2):

    cur = prev + tmp
    tmp = prev
    prev = cur

print(cur)