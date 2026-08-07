class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # left=0

        # longest=0
        # for right in range(len(prices)):
        #     if prices[right]<prices[left]:
        #         left=right
        #     else:
        #         longest=max(longest, prices[right]-prices[left])
        # return longest        
        maxi=0
        mini=float('inf')

        for i in prices:
            maxi=max(maxi, i-mini)
            mini=min(mini, i)
        return maxi