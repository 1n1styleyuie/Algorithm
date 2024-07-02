def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2+1):
        num = 1
        res_str = ''
        tmp = s[:i]
        for j in range(i, len(s), i):            
            if tmp == s[j:j+i]:
                num += 1
            else:
                if num != 1:
                    res_str += str(num)+tmp    
                else:
                    res_str += tmp
                tmp = s[j:j+i]
                num = 1
        if num != 1:
            res_str += str(num) + tmp
        else:
            res_str += tmp
        result.append(len(res_str))

    return min(result)