class Solution(object):
    def removeDuplicates(self, nums):
      if not nums:
        return 0
      l=1
      for r in range(1,len(nums)):
        if nums[r]!=nums[r-1]:
            nums[l]=nums[r]
            l+=1
      return l        

Time complexity = o(n)
We use two pointers:

r scans the array.
l tracks where the next unique element should go.

Since the array is sorted, r compares the current element with the previous one.

If they are the same, it's a duplicate, so skip it.
If they are different, place the element at l and move l forward.

At the end, l gives the number of unique elements.
