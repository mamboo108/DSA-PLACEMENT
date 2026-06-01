class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        expected=n*(n+1)//2
        actual=sum(nums)
        return expected - actual

Time Complexity o(n)

n = len(nums) → Find how many numbers are in the array.
expected = n * (n + 1) // 2 → Calculate the sum of all numbers from 0 to n.
actual = sum(nums) → Calculate the sum of the numbers present in the array.
expected - actual → The difference is the missing number.
