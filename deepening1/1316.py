# 그룹 단어 체커
def is_group_word(word):
    seen_chars = set()
    for i, char in enumerate(word):
        # 현재 문자가 이미 등장했고, 이전 문자와 다르다면 그룹 단어가 아님
        if char in seen_chars and word[i - 1] != char:
            return 0
        seen_chars.add(char)
    return 1
wordCount = int(input())
check = 0
i = 1
while(i <= wordCount):
    word = input().lower()
    check += is_group_word(word)
    i += 1
print(check)