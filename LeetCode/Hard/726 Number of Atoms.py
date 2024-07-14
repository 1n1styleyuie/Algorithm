from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]

        idx = 0

        # idx값이 formula의 길이보다 작을때 까지 반복
        while idx < len(formula):

            # '(' 가 나올 경우 새로운 defaultdict를 만들어 stack에 저장한다.
            # 해당 방법은 괄호가 닫힐 때 괄호 안에 있는 딕셔너리 값들만 계산하기 위함이다.
            if formula[idx] == '(':
                stack.append(defaultdict(int))
                idx += 1

            # 닫힌 괄호일 경우
            elif formula[idx] == ')':
                # 괄호 안에 있는 딕셔너리 전체를 pop하여 꺼내온다.
                curr_map = stack.pop()
                # idx를 +1 하고 multi를 초기화 하는 이유는 괄호 뒤에 오는 숫자를 찾기 위함이다.
                idx += 1
                multi = ''

                while idx < len(formula) and formula[idx].isdigit():
                    multi += formula[idx]
                    idx += 1

                if multi:
                    # multi가 문자열이었기 때문에 정수형으로 변환해준다.
                    multi = int(multi)
                    for a in curr_map:
                        # 여기서 stack[-1]의 값들은 괄호 밖에 저장되어 있는 값들이고 해당 값이 존재하지 않으면 defaultdict로 인해 자동으로 기본값이 주어지면서 값을 더하게 된다.
                        curr_map[a] *= multi
                # multi가 없는 경우엔 그냥 더해주면 된다.
                for a in curr_map:
                    stack[-1][a] += curr_map[a]
            
            # 그 외 경우
            else:
                # 문자 하나를 curr_a에 저장
                curr_a = formula[idx]
                idx += 1

                # 소문자면 문자열에 추가
                while idx < len(formula) and formula[idx].islower():
                    curr_a += formula[idx]
                    idx += 1

                curr_count = ''
                # 숫자면 숫자 저장
                while idx < len(formula) and formula[idx].isdigit():
                    curr_count += formula[idx]
                    idx += 1
                
                # curr_count가 비어있으면 해당 문자는 1만을 가지고 있기 때문에
                if curr_count == '':
                    stack[-1][curr_a] += 1
                else:
                    stack[-1][curr_a] += int(curr_count)

        res = dict(sorted(stack[0].items()))

        ans = ''
        for a in res:
            ans += a
            if res[a] > 1:
                ans += str(res[a])

        return ans 