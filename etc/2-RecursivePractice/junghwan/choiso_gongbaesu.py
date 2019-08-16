def cdg_recur(n1, n2):
    
    if n1 < n2:
        return 0

    else:
        if n2 == 0:
            return n1

        else:
            return cdg_recur(n2, n1%n2)


def cdg_loop(n1, n2):

    if n1 < n2:
        return 0
    
    while n2 != 0:
        
        tmp = n1 % n2
        n1 = n2
        n2 = tmp

    return n1


def cgb(n1, n2):
    
    return int((n1 * n2) / cdg_recur(n1, n2))
    


num1 = 12
num2 = 10

print(cgb(num1, num2))