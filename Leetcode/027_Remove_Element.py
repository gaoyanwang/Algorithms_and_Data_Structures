class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # Extreme case
        if nums == []:
            return 0
        # if len(nums) == 1:
        #   if nums[0] != val:
        #       return 1
        #   else:
        #       return 0

        # normal case: two pointers, j for detection, j follow
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == val:
                j = j + 1
            else:
                nums[i] = nums[j]
                i = i + 1
                j = j + 1
        return i
