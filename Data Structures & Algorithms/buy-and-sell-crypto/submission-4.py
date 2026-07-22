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
        profit=0

        for right in range(len(prices)):
            if prices[left]<prices[right]:
                profit=max(profit, prices[right]-prices[left])
            else:
                left=right
        return profit
            
            
            
            

        

        