# 공 바꾸기
n, m = map(int,input().split())
x = 1
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = x
    x += 1
for i in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    temp = arr[x]
    arr[x] = arr[y]
    arr[y] = temp
for i in range(n):
    print(arr[i], end=" ")