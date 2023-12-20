# 영수증
import sys
totalPrice = int(sys.stdin.readline())
n = int(sys.stdin.readline())
sum = 0

for i in range(n):
    list1 = list(map(int,sys.stdin.readline().split()))
    sum += list1[0] * list1[1]


if sum == totalPrice:
    print('Yes')
else:
    print('No')