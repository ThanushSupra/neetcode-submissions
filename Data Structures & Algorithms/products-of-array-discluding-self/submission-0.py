class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        prefix = [1] * len(nums)
        for i,num in enumerate(nums): 
            prefix[i] *= pre
            pre *= num
        suf = 1
        for i in range(len(nums)-1,-1,-1): 
            prefix[i] *= suf
            suf *= nums[i]

        return prefix