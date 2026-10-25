class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet: 
            if num-1 in numSet: 
                continue
            k = num
            i = 1
            temp = 1
            while k + i in numSet: 
                temp += 1
                i += 1
            longest = max(temp,longest)
        return longest


        
