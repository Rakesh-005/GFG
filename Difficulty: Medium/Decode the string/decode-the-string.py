
class Solution:
    def decodedString(self, s):
        # code here
        n = len(s)
        stack = []
        ans = ""
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                while stack[-1] != '[':
                    ans = stack.pop() + ans
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number = stack.pop() + number
                number = int(number)
                ans = ans * number
                stack.append(ans)
                ans = ""
        return "".join(stack)

