class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        do={}
        nums.sort()
        for i in range(len(nums)):
            if nums[i] in do:
                do[nums[i]]=do[nums[i]]+1
            else:
                do[nums[i]]=1
        sorted_descending = dict(sorted(do.items(), key=lambda item: item[1], reverse=True))
        top_k_keys = list(sorted_descending.keys())[:k]
        print(sorted_descending,top_k_keys)

        return top_k_keys
            
            
        