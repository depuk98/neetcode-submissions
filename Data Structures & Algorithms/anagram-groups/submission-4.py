class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        do={}
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            # if sorted_text in do:
            #     do[sorted_text].append(strs[i])
            # else:
            #     do[sorted_text]=strs[i]
            do.setdefault(sorted_text, []).append(strs[i])
        return list(do.values())
                    
        