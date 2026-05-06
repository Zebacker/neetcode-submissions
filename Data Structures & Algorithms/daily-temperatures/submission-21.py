class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[]
        n=len(temperatures)
        for i, val in enumerate(temperatures):
            j, count=i+1, 1
            while j<n:
                if temperatures[j]>val: break
                j+=1
                count+=1
            count=0 if j==n else count
            res.append(count)
        return res


        

                


            

