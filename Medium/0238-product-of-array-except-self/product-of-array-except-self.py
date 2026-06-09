import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero=nums.count(0)
        
        if zero>1:
            return [0]*len(nums)
        if zero==1:
            total=[]
            

            for i in nums:
                if i !=0:
                    total.append(i)
            produ=math.prod(total)
            result=[]
            
            for i in nums:
                if i==0:
                    result.append(produ)
                else:
                    result.append(0)
            return result
        total=math.prod(nums)
        return [total//i for i in nums]
            