x = int(input())
y = int(input())

y1 = y // 100
y2 = (y % 100) // 10
y3 = ((y % 100) % 10)

print(x * y3)
print(x * y2)
print(x * y1)
print(x*y3 + x*y2*10 + x*y1*100)