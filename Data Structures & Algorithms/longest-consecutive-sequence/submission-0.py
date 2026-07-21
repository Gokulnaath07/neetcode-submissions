class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        #we dont need the duplicate numbers so use sets.
        #so we are using comparing two numbers here
        #first see whether there are any number has the imiidate left number in this set
        #if not then go to a loop see whether there are numbers available after that (Consecutive)
        #this will go on till we have that consecutive next number
        #Also we have to follow the current streak and a overall streak.
        #Current inside while and overall inside the outer loop for every number where we check is that have a left number in set
        #Return the value of overall streak
        sets=set(nums)
        length=0

        for num in sets:
            if num-1 not in sets:
                current_num=num
                current=1

                while current_num+1 in sets:
                    current_num +=1
                    current+=1
                length=max(length, current)
        return length
            
        