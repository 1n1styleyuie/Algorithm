# 9375 s3
tc = int(input())
for _ in range(tc):
    n = int(input())
    clothes = {}
    for _ in range(n):
        a, b = input().split()
        # 같은 카테고리가 있으면 추가
        if b in clothes:
            clothes[b].append(a)
        # 없으면 새로 저장
        else:
            clothes[b] = [a]
        
    cnt = 1
    for x in clothes:
        # 카테고리 안에 있는 의상 수와 안입는 경우를 더해서 곱함
        cnt *= (len(clothes[x])+1)
    # 아무것도 안입는 경우는 빼줘야 하기에 -1하여 출력
    print(cnt-1)