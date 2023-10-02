def find_set(x):
    if parents[x] == x:
        return x
    return find_set(parents[x])


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    parents = [i for i in range(V + 1)]
    # 입력 받고 union함수 호출하여 집합 생성
    for _ in range(E):
        a, b = map(int, input().split())
        union(a, b)
    # 중복제거를 위해 set을 만듬
    res = set()
    # set()에 저장되기 때문에 중복은 제거됨
    for i in range(1, V+1):
        res.add(find_set(i))
    print(f'#{tc} {len(res)}')