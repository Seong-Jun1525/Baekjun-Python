# ATM
# n = int(input()) # 사람 수 입력 받기
# sum, result, j = 0, 0, 1
# sumList = [0 for i in range(n)] # 사람 수 만큼 리스트 0으로 초기화
# min = list(map(int, input().split())) # 사람 수 만큼 해당 사람이 걸리는 시간 초기화
# temp = min[0]
# for i in range(n):
#     for j in range(n):
#         if min[i] < min[j]:
#             temp = min[i]
#             min[i] = min[j]
#             min[j] = temp
# for i in range(n):
#     sum += min[i]
#     sumList[i] = sum
#     result += sumList[i]
# print(result)

# 아래의 코드는 백준에서 제일 잘한 사람의 코드
import sys
n = int(sys.stdin.readline())
time = list(map(int,sys.stdin.readline().split()))
time.sort() # sort는 정렬 함수. reverse=False 오름차순(기본값), reverse=True 내림차순
sum = 0
for i in range(n):
    sum += time.pop() * (i+1)
print(sum)