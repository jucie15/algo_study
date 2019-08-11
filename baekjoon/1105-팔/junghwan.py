s = input().split()

L = s[0]
R = s[1]


cnt = 0

if len(L) != len(R):
    cnt = 0

else:
    for i in range(len(L)):

        if L[i] == R[i]:

            if L[i] == '8':
                cnt += 1

        else:
            break


print(cnt)
