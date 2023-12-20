# 공 넣기
n, m = map(int, input().split())
arr = [0 for _ in range(n)]
for i in range(m):
    i,j,k = input().split()
    i = int(i)
    for x in range(i-1, int(j)):
        arr[x] = int(k)
for x in range(n):
    print(arr[x], end=" ")
