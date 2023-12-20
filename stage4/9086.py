testCase = int(input())
arr = []
for i in range(testCase):
    word = input()
    arr.append(word.upper())
for i in range(testCase):
    n = len(arr[i])-1
    if n < 0:
        print(arr[i])
    elif n == 0:
        print(arr[i]+arr[i])
    else:
        print(arr[i][0::n])
