class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxlen=0
        for i in range(n):
            res=set()
            for j in range(i,n):
                if s[j] in res:
                    break
                res.add(s[j])
                maxlen=max(maxlen,j-i+1)
        return maxlen



        


        