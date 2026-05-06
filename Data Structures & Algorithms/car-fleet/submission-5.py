class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        Stack=[]
        car=[(p,s) for p,s in zip(position, speed)]
        car.sort(reverse=True)
        for p, s in car:
            Stack.append((target-p)/s)
            if len(Stack)>=2 and Stack[-2]>=Stack[-1]: Stack.pop()
        return len(Stack)