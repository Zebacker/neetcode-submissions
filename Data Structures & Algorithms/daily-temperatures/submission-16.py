class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        Stack=[]
        tem=[0]*len(temperatures)
        for i, val in enumerate(temperatures):
            while Stack and val>temperatures[Stack[-1]]:
                n=Stack.pop()
                tem[n]=i-n
            Stack.append(i)
        return tem

        

                


            

