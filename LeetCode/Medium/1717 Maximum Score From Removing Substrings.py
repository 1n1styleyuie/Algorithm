class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        total = 0
        # ab, ba중 큰값을 high_pair, 작은값을 low_pair로 설정
        if x > y:
            high_pair = "ab"
            low_pair = "ba"
        else:
            high_pair = "ba"
            low_pair = "ab"

        # 처음 보낼때는 s 전체를 보내고 남은 문장을 string_first에 저장
        string_first = self.remove_string(s, high_pair)
        # 제거된 숫자는 보낸 문장에서 return된 문장의 길이의 // 2한 값
        remove_count = (len(s) - len(string_first)) // 2
        total += remove_count * max(x, y)

        # 두번째 보낼때는 string_first를 보내고 남은 문장을 받음
        string_second = self.remove_string(string_first, low_pair)
        # 제거된 숫자는 보낸 문장에서 return된 문장의 길이의 // 2한 값
        remove_count = (len(string_first) - len(string_second)) // 2
        total += remove_count * min(x, y)

        return total

        
    def remove_string(self, input_string: str, target_pair: str) -> str:
        char_stack = []

        for current_char in input_string:
            # 현재 문자가 찾을 문자의 뒷문자와 같고 리스트안에 저장되어 있는 값이 존재하며 값이 찾을 문자의 앞문자와 같을 경우에만 pop
            if current_char == target_pair[1] and char_stack and char_stack[-1] == target_pair[0]:
                char_stack.pop()
            else:
                char_stack.append(current_char)
                
        return "".join(char_stack)