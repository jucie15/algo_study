n = int(input())
res = list()

for i in range(n):
    num = int(input())
    if i is 0:
        res.append(num)
        continue
    for j in range(0, len(res)):
        if num < res[j]:
            res.insert(j, num)
            break
        elif j + 1 is len(res):
            res.append(num)

for num in res:
    print(num, end='')
