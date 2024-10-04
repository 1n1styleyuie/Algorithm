# 1541 s2
import sys
input = sys.stdin.readline


'''
적절하게 괄호를 쳐서 식의 값을 최소로 하기 위해서 
'-' 를 기준으로 split하여 리스트에 저장한 후 
묶여있는 값들을 더하여 전체 결과값에서 뺴면 된다.

ex) 55-50+40
'-'를 기준으로 리스트에 저장하면 ['55', '50+40']이다.
리스트의 첫번쨰 값은 무조건 결과값에 더해져야 하고
두번째 값 부터 결과값에서 빼주면 된다.
결국 식은 55 - ( 50 + 40 )이 되는 것이고 결과값이 -35가 나오게 된다.

'''


arr = list(input().rstrip().split('-'))

res = 0
for i in range(len(arr)):
    if i == 0:
        if '+' in arr[i]:
            num = list(map(int, arr[i].split('+')))
            for n in num:
                res += n
        else:
            res += int(arr[i])
    else:
        if '+' in arr[i]:
            num = list(map(int, arr[i].split('+')))
            for n in num:
                res -= n
        else:
            res -= int(arr[i])

print(res)