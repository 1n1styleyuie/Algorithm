def f(phone_book):
    # 문자열을 정렬하면 다음과 같이 정렬된다.(https://engineer-mole.tistory.com/271)
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 비교해서 같다면 False
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            return "NO"
    # 다 돌았을 때 문제가 없으면 True
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(str(input()))
    print(f(arr))