class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack=[]
        for i in tokens:
            if i == "+": Stack.append(Stack.pop()+Stack.pop())
            elif i=="-": Stack.append(-Stack.pop()+Stack.pop())
            elif i=="*": Stack.append(Stack.pop()*Stack.pop())
            elif i=="/": Stack.append(int((1/Stack.pop())*Stack.pop()))
            else: Stack.append(int(i))
        return Stack[0]

            