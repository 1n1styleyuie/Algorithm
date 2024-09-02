# 1063 s3

import sys
input = sys.stdin.readline

king, stone, N = input().split()
# 아스키코드로 변환하여 list에 저장
# 아스키코드 A = 65
k = [int(ord(king[0])-64), int(king[1])]
s = [int(ord(stone[0])-64), int(stone[1])]

move = {'R': [1, 0], 'L': [-1, 0], 'B': [0, -1], 'T': [0, 1], 'RT': [1, 1], 'LT': [-1, 1], 'RB': [1, -1], 'LB': [-1, -1]}

# 움직이는 횟수 만큼 실행
for _ in range(int(N)):
    m = input().rstrip() #지금 이동
    
    # 움직였을 경우의 위치
    nx = k[0] + move[m][0] 
    ny = k[1] + move[m][1]
    
    # 킹 조건 검사
    if 0 < nx <= 8 and 0 < ny <= 8:
    	# 돌과 겹치는지 확인
        if nx == s[0] and ny == s[1]:
            sx = s[0] + move[m][0]
            sy = s[1] + move[m][1]
            # 돌 조건 검사
            if 0 < sx <= 8 and 0 < sy <= 8:
                k = [nx, ny] # 킹 이동
                s = [sx, sy] # 돌 이동 
        else:
            k = [nx, ny] # 킹만 이동
print(f'{chr(k[0] + 64)}{k[1]}')
print(f'{chr(s[0] + 64)}{s[1]}')