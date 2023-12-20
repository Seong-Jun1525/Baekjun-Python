# 회의실 배정
n = int(input())
timeList = [[0 for i in range(2)] for i in range(n)]
max_count = 0
valid_time_list = []

for i in range(n):
    sp, ep = input().split()
    timeList[i][0], timeList[i][1] = int(sp), int(ep)

for i in range(n):
    if timeList[i][0] == timeList[i][1]:
        max_count += 1
    else:
        valid_time_list.append(timeList[i])

print(valid_time_list)
timeList = list(set([tuple(set(valid_time_list)) for i in valid_time_list]))

print(timeList)
print(max_count)

# ep = timeList[0][1]

# for p in range(n):
#     p += 1
#     if(p >= n):
#         break
#     if ep <= timeList[p][0]:
#         print(ep, " <= ", timeList[p][0], p)
#         ep = timeList[p][1]
#         max += 1