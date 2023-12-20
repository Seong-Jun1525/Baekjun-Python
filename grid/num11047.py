# 동전0
n, k = map(int, input().split())
sum, mok = 0, 0
coin = list(range(n))

for i in range(n):
    coin[i] = int(input())
coin.sort(reverse=True)

for i in range(n):
    if k >= coin[i]:
        mok = k // coin[i]
        sum += mok
        k = k % coin[i]

print(sum)