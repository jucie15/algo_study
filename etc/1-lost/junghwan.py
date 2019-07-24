n = 5
price = [20, 7, 8, 2, 5]

ans = 10000000000000000

i = 1
idx = 0

while idx < i:

    if i == n:
        idx += 1
        i = idx + 1

    if idx == n-1:
        break
    

    lost = price[idx] - price[i]
    if lost > 0:
        ans = min(ans, lost)

    i += 1


print(ans)
