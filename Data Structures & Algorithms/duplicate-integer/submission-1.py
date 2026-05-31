class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nnums=list(set(nums))
        if len(nums)!=len(nnums):
            return True
        else:
            return False
         