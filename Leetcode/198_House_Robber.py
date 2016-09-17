class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return max(nums)

        max1 = nums[0]
        max2 = max(nums[0,]nums[1])
        for i in range(2, len(nums)):
            max_all = max(max1 + nums[i], max2)
            max1 = max2
            max2 = max_all
        return max_all
        
