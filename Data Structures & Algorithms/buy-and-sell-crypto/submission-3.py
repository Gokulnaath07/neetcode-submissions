class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Dynamic Programining
        # mini=float('inf')
        # maxi=0

        # for i in prices:
        #     mini=min(mini, i)

        #     maxi=max(maxi, i-mini)
        # return maxi

        left =0
        right=1
        profit=0

        while right<len(prices):
            if prices[left]<prices[right]:
                profit=max(profit, prices[right]-prices[left])
            else:
                left=right
            right+=1
        return profit
            
            
            
            

        

        