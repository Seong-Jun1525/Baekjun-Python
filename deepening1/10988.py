# 팰린드롬(회문)
word = input().lower()

wordList = list(word)
wordList.reverse()
palindrome = ''.join(wordList)

if word == palindrome:
    print(1)
else:
    print(0)