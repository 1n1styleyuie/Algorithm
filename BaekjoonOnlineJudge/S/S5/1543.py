import sys
input = sys.stdin.readline

sentence = list(input().rstrip())
word = list(input().rstrip())
cnt = 0
idx = 0

while idx < (len(sentence) - len(word) + 1):
    # 슬라이싱한 문자열이 word랑 같으면 카운트하고 인덱스값을 문자열 뒤에서 시작하도록 저장
    if sentence[idx:idx+len(word)] == word:
        cnt += 1
        idx += len(word)
    else:
        idx += 1

print(cnt)