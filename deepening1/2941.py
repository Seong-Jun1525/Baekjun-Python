# 크로아티아 알파벳
import re
word = input()
count = 0
croatiaAlpha = 'c=|c-|dz=|d-|lj|nj|s=|z='
while(1):
    n = re.search(croatiaAlpha, word)
    if n is not None:
        if n.group() == 'c=' or 'c-' or 'dz=' or 'd-' or 'lj' or 'nj' or 's=' or 'z=':
            # print(n.group())
            count += 1
            word = word.replace(n.group(), ' ', 1)
            # print(word)
    else:
        word = word.replace(' ', '')
        break

print(len(word) + count)