from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict=defaultdict(list)

        for s in strs:
            countList=[0] * 26

            for count in s:
                countList[ord(count)-ord("a")] +=1# make the freq of each letter in a word to the list
            anaDict[tuple(countList)].append(s)#keys cant be mutable in dict in python

        return list(anaDict.values())
        