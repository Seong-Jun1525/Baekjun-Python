# 과제 안 내신 분?
student = [i for i in range(1, 31)]  # 학생 배열 초기화
x = [0 for i in range(len(student)-2)]  # 과제한 학생 배열 초기화
removeList = set()  # 중복을 피하기 위한 집합 초기화

# 과제를 한 학생 입력받기
for i in range(len(x)):
    xStudent = int(input())
    x[i] = xStudent

# 과제를 한 학생 리스트와 그냥 학생 리스트를 비교해서
# 해당 번호가 그냥 학생 리스트 번호에 없으면 제거 리스트에 추가하기
for i in range(len(x)):
    for j in range(len(student)):
        if x[i] == student[j]:
            removeList.add(j)

# 찾은 인덱스를 역순으로 정렬하여 뒤에서부터 삭제 (앞에서부터 삭제하면 인덱스가 변하면서 문제 발생)
for i in reversed(sorted(removeList)):
    student.pop(i)

# 결과 출력
for i in range(2):
    print(student[i])