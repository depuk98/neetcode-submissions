class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=0
        out=[]
        for i in range(len(nums)):
            mul=1
            for j in range(len(nums)):
                if i!=j:
                    mul=mul*nums[j]
            out.append(mul)
        return out
        
