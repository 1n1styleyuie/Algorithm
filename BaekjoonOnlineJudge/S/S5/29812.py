# 29812 s5
import sys
input = sys.stdin.readline


n = int(input())
s = input().rstrip()
d, m = map(int, input().split())

energy = 0
res = 0
hyu = {'H' : 0, 'Y' : 0, 'U' : 0}

idx = 0
while idx < n:
    if s[idx] in ['H', 'Y', 'U']:
        hyu[s[idx]] += 1
    else:
        cnt = 1
        while idx + 1 < n and s[idx+1] != 'H' and s[idx+1] != 'Y' and s[idx+1] != 'U':
            cnt += 1
            idx += 1
        
        if cnt * d <= d + m:
            energy += cnt * d
        else:
            energy += d + m
    
    idx += 1




if not energy:
    print('Nalmeok')
else:
    print(energy)


arr = sorted(hyu.items(), key = lambda x : x[1])
if not arr[0][1]:
    print('I love HanYang University')
else:
    print(arr[0][1])