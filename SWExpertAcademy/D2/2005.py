import sys
sys.stdin = open('input.txt')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     PascalTriangle = [ [] for _ in range(N)]
#     PascalTriangle[0] = [1]
#     for i in range(1, N):
#         Pascal = PascalTriangle[i-1]
#         stack = []
#         for j in range(N):
#             if Pascal[-1] == 1 and len(Pascal) != 1:
#                 stack.append(Pascal[-1])
#             elif Pascal[-1] == 1 and len(Pascal) == 1:
#                 stack.append(Pascal.pop())
#             elif Pascal[-1] != 1 and len(Pascal) != 1:
#                 number = Pascal.pop()
#                 stack.append(number + Pascal[-1])
#             PascalTriangle[j].append(stack)
#
#     print(PascalTriangle)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    pascal = [[1] * i for i in range(1, N+1)]
    for i in range(2, N):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    print(f'#{tc}')
    for k in range(N):
        print(*pascal[k])