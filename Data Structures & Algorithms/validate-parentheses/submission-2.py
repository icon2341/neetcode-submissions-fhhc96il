class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        oppositeMap ={
            ')': '(',
            '}': '{',
            ']': '['
        }
        for letter in s:
            if(len(stack) > 0):
                # check to see if most recent item in stack IS opposite
                if(letter in oppositeMap):
                    # if closing
                    if stack[-1] != oppositeMap[letter]:
                        return False
                    else:
                        stack.pop()
                else:
                    # if opening
                    stack.append(letter)
            else:
                stack.append(letter)
        if(len(stack) > 0):
            return False
        else:
            return True