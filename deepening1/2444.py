# 별 찍기-7
# import sys
# n = int(sys.stdin.readline())
# star = 1
# line = 2*n-1
# t = 0
# for i in range(line):
#     for j in range(n-1):
#         print("", end=" ")
#     for s in range(star):
#         print("*", end="")
#     if t == 0:
#         star += 2
#         n -= 1
#     elif t == 1:
#         star -= 2
#         n += 1
#     if n == 0 or star == line:
#         t = 1
#     if i == line - 1:
#         break
#     else:
#         print()
a=int(input())
for i in range(1,a+1):
    print(' '*(a-i)+'*'*(2*i-1))
for i in range(1,a):
    print(' '*i+'*'*(2*a-2*i-1))