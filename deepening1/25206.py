# 너의 평점은
def average(SI):
    creditTotal = 0 # 전공과목별 (학점 × 과목평점)의 합
    totalScore = 0 # 학점의 총합
    for idx in range(len(SI)):
        idx1 = float(SI[idx][1])
        idx2 = SI[idx][2]

        if idx2 == 'P' or idx2 == 'p':
            continue
        else:
            if idx2 == 'A+' or idx2 == 'a+':
                creditTotal += idx1*4.5
            elif idx2 == 'A0' or idx2 == 'a0':
                creditTotal += idx1*4.0
            elif idx2 == 'B+' or idx2 == 'b+':
                creditTotal += idx1*3.5
            elif idx2 == 'B0' or idx2 == 'b0':
                creditTotal += idx1*3.0
            elif idx2 == 'C+' or idx2 == 'c+':
                creditTotal += idx1*2.5
            elif idx2 == 'C0' or idx2 == 'c0':
                creditTotal += idx1*2.0
            elif idx2 == 'D+' or idx2 == 'd+':
                creditTotal += idx1*1.5
            elif idx2 == 'D0' or idx2 == 'd0':
                creditTotal += idx1*1.0
            elif idx2 == 'F' or idx2 == 'f':
                creditTotal += 0.0
            totalScore += idx1
    return round(creditTotal/totalScore, 6)
StudentInfo = {}

for j in range(20):
    try:
        input_str = input()
        # 입력된 문자열을 공백을 기준으로 분리
        strings = input_str.split()

        # 분리된 문자열이 3개가 아니면 예외 발생
        if len(strings) != 3:
            raise ValueError("세 개의 문자열을 정확히 입력하세요.")

        # 분리된 문자열 각각을 변수에 저장
        subject, credit, grade = strings
        StudentInfo[j] = [subject, credit, grade]
    except ValueError as ve:
        print("error {ve}")

avg = average(StudentInfo)
print(avg)