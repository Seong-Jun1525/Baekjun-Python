# 킹, 퀸, 룩, 비숍, 나이트, 폰
import sys
piece = [1, 1, 2, 2, 2, 8]
whitePiece = list(map(int, sys.stdin.readline().split()))
for i in range(len(piece)):
    if (piece[i] < whitePiece[i]) or (piece[i] > whitePiece[i]):
        whitePiece[i] = piece[i] - whitePiece[i]
    else:
        whitePiece[i] = 0
for i in range(len(whitePiece)):
    print(whitePiece[i], end=" ")