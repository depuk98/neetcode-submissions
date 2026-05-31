class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        do={}
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if sorted_text in do:
                continue
            do[sorted_text]=[strs[i]]
            for j in range(i+1,len(strs)):
                sorted_texti = "".join(sorted(strs[j]))
                # print(sorted_text,strs[j])
                if sorted_texti==sorted_text:
                    do[sorted_texti].append(strs[j])
                # print(do)
        return list(do.values())
                    
        