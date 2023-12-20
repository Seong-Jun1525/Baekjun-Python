n = int(input())
arr=[]
count = 0
arr = list(map(int, input().split()))
v = int(input())
for i in range(n):
    if v == arr[i]:
        count += 1
print(count)