class Solution:
    def secondLargestElement(self, nums):
        n=len(nums)
        if n<2:
            return -1
        largest=nums[0]
        for i in range(n):
            if nums[i]>largest:
                largest=nums[i]
        secondlargest=-1
        for i in range(n):
            if nums[i]!=largest:
                if nums[i]>secondlargest:
                    secondlargest=nums[i]
        return secondlargest            

      # Time complexity o(n)
