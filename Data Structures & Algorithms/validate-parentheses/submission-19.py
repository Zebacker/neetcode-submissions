class Solution:
    def isValid(self, s: str) -> bool:
        tems={")":"(", "]":"[", "}":"{"}
        Stack=[]
        for i in s:
            if i in tems.values(): Stack.append(i)
            elif i in tems.keys(): 
                if Stack and tems[i]==Stack[-1]: Stack.pop()
                else: return False
        return True if not Stack else False
        
