class Solution(object):
    def firstUniqChar(self, s):
        count ={}
        for c in s:
            count[c]=1 + count.get(c,0)

        for i,c in enumerate(s):
            if count[c]==1:
                return i 
        return -1          

Time complexity = o(n)
