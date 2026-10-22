class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i,num in enumerate(nums): 
            indices[num] = i

        for i,num in enumerate(nums): 
            if target-num in nums and indices[target-num] != i: 
                return[i, indices[target-num]]





        
                