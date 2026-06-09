class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Stack=[]
        for i in tokens:
            if i not in "+-*/": Stack.append(int(i))
            else:
                if i == "+": Stack.append(Stack.pop() + Stack.pop())
                elif i == "-": Stack.append(-Stack.pop() + Stack.pop())
                elif i == "*": Stack.append(Stack.pop()*Stack.pop())
                elif i == "/": Stack.append(int((1/(Stack.pop())*float(Stack.pop()))))
        return Stack[0]