# class Solution:

#     def validPop(self,left,right):
#         if left=="(" and right==")":
#             return True
#         elif left=="{" and right=="}":
#             return True
#         elif left=="[" and right=="]":
#             return True
#         else:
#             return False

#     def isValid(self, s: str) -> bool:
#         stack = []
#         push_op = ["(","{","["]
#         pop_op = [")","}","]"]
#         for i in s:
#             if i in push_op:
#                 stack.append(i)
#             elif i in pop_op and len(stack)!=0 and self.validPop(stack[-1],i):
#                 stack.pop()
#             else:
#                 return False
            
            

#         if len(stack)==0:
#             return True
#         else:
#             return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return len(stack) == 0
        