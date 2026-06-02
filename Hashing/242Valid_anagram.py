class Solution(object):
    def isAnagram(self, s, t):
       if len(s)!=len(t):
        return False
       counts, countt = {}, {} 

       for i in range(len(s)):
        counts[s[i]] = 1 + counts.get(s[i],0)
        countt[t[i]] = 1 + countt.get(t[i],0)
       for c in counts:
        if counts[c]!=countt.get(c,0):
            return False
       return True     

      Time Complexity o(n)

optimized 

class Solution(object):
    def majorityElement(self, nums):
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
