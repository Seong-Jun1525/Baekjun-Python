# 수 찾기
n = int(input())
aList = set(map(int, input().split()))

m = int(input())
bList = list(map(int, input().split()))

check = [0] * n

for i in range(m):
    if bList[i] in aList:
        index = list(aList).index(bList[i])
        check[index] += 1

for i in range(n):
    print(check[i])