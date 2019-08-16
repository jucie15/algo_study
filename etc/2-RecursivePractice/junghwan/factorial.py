def fact_recur(n):

    if n == 1:
        return 1

    return n * fact_recur(n-1)

def fact_loop(n):
    
    mul = 1

    for i in range(2, n+1):
        mul *= i

    return mul


num = 5

print(fact_recur(num))
print(fact_loop(num))