def fibo_recur(n):

    if n <= 2:
        return 1

    return fibo_recur(n-1) + fibo_recur(n-2)


def fibo_loop(n):
    
    cur = 1
    prev = 1
    tmp = 1

    if n <= 2:
        return 1

    for _ in range(n-2):
        
        cur = tmp + prev
        tmp = prev
        prev = cur

    return cur


num = 6

print(fibo_recur(num))
print(fibo_loop(num))