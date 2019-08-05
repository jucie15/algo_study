n = int(input())

two_list = [64, 32, 16, 8, 4, 2, 1]
stick_len = n
cnt = 0

for i in two_list:

    if stick_len >= i:
        stick_len -= i
        cnt += 1

    else:
        pass

    if stick_len == 0:
        print(cnt)
        break

