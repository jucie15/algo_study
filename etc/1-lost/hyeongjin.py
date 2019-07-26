n =int(input("데이터의 갯수를 입력하세요"))
price=[]
x=0
while len(price) != n:
    rand=random.randrange(1,50)
    price.append(rand)
    for y in range(len(price)-1):
        if price[y] == price[-1]:
            del price[-1]
print(price)
result=max(price)
for i in range(len(price)):
    if(result==1):
        break;
    for j in range(i+1,len(price)):
        if price[i]>price[j]:
            if price[i]-price[j]<result:
                result=price[i]-price[j]
print(result)
