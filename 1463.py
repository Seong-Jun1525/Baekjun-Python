# 1로 만들기
#   X가 3으로 나누어 떨어지면, 3으로 나눈다.
#   X가 2로 나누어 떨어지면, 2로 나눈다.
#   1을 뺀다.
# x = int(input())
# n = x
# count1 = 0

# while x > 1:
#     if x % 3 == 0:
#         x = x // 3
#     elif x % 3 == 1:
#         x -= 1
#     else:
#         x -= 1
#     count1 += 1
#     if(n == 1): break

# count2 = 0
# while n > 1:
#     if n % 3 == 0:
#         n = n // 3
#     elif n % 3 == 1:
#         n = n // 2
#     else:
#         n -= 1
#     count2 += 1
#     if(n == 1): break
# print(count1 if count1 < count2 else count2)
