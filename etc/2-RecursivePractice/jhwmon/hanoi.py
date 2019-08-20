#하노이의 탑
# A막대기를 B막대기에 오름차순으로 정렬해라

# 원반을 옮기는 함수
def move(x, y):
    val = x.pop(0)
    y.insert(0, val)

def hanoi(cnt, start, end, sub):
    if cnt == 1:
        move(start, end)
        return

    hanoi(cnt - 1, start, sub, end)
    move(start, end)
    hanoi(cnt - 1, sub, end, start)
    return

# 3개의 막대기
listA = [1, 2, 3, 4, 5]
listB = []
listC = []

print("실행 전")
print(listA)
print(listB)
print(listC)

hanoi(5, listA, listC, listB)

print("실행 후")
print(listA)
print(listB)
print(listC)