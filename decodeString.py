class Solution:
    def decodeString(self, s: str) -> str:
        result, k_stack, stack = [], [], []
        i, n = 0, len(s)
        while i < n:
            j = i
            if s[i].isdigit():
                i += 1
                if s[i].isdigit():
                    i += 1
                    if s[i].isdigit():
                        i += 1
                k_stack.append(s[j:i])
                stack.append([])
            elif s[i] == ']':
                new_str = stack.pop() * int(k_stack.pop())
                if stack:
                    stack[-1].extend(new_str)
                else:
                    result.extend(new_str)
            else:
                if stack:
                    stack[-1].append(s[i])
                else:
                    result.append(s[i])
            i += 1
        return "".join(result)
