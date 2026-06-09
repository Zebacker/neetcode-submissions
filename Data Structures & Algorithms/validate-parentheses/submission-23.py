class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        bracket_map = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in bracket_map.values(): Stack.append(i)
            elif i in bracket_map.keys():
                if Stack and bracket_map[i] == Stack[-1]: Stack.pop()
                else: return False
        return True if not Stack else False

