class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        seenStack = []
        for num in tokens:
        
            if(num == "+"):
                print(seenStack, num)
                seenStack.append(seenStack.pop() + seenStack.pop())
            elif(num == "/"):

                print(seenStack, num)
                v1 = seenStack.pop()
                v2 = seenStack.pop()
                print(v1,v2)
                seenStack.append(int((v2 / v1)))
            elif(num == "-"):
                print(seenStack, num)
                seenStack.append(seenStack[-2] - seenStack[-1])
                hold = seenStack.pop()
                seenStack.pop()
                seenStack.pop()
                seenStack.append(hold)
            elif(num == "*"):
                print(seenStack, num)
                seenStack.append(seenStack.pop() * seenStack.pop())
            else:
                seenStack.append(int(num))
        return seenStack[0]