class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > len(nums) // 2:
                return num

Time complexity = o(n)
      
