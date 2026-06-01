class Solution(object):
    def twoSum(self, nums, target):
        seen={}
        for i, num in enumerate(nums):
            complement=target-num

            if complement in seen:
                return (seen[complement],i)
            seen[num]=i

Time complexity = o(n)

Create an empty dictionary called seen.
Go through the array one number at a time.
For each number, calculate what number is needed to reach the target (complement = target - num).
Check if that needed number is already in seen.
If yes, return the index of the needed number and the current index.
If not, store the current number and its index in seen.
Continue until the pair is found.
