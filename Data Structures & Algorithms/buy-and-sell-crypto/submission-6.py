class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profits=[]
        # result=[]
        # if len(prices)==1:
        #     return 0
        # for i in range(len(prices)):
        
        #     # print(i,"out",prices[i])
        #     for j in range(i+1,len(prices)):
        #         # print(j,"in",prices[j])
        #         profit=prices[j]-prices[i]
        #         profits.append(profit)

        #     p=max(0,max(profits))
        #     result.append(p)
        # # print(result)
        # res=max(0,max(result))

        min_price=prices[0]
        max_profit=0
        for price in prices:
            min_price=min(price,min_price)
            profit=price-min_price
            max_profit=max(profit,max_profit)
        return max_profit
                

        