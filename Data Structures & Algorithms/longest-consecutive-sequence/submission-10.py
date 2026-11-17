class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cur_set=set(nums)
        longest=0
        counter=0
        for i in nums:
            if i-1 not in cur_set:
                current_num=i
                counter=0
                while current_num in cur_set:
                    current_num +=1
                    counter+=1
                longest=max(longest, counter)
        return longest