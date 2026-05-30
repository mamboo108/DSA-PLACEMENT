    def containsDuplicate(self, nums):
       hashset=set()
       n=len(nums)
       for n in nums:
            if n in hashset:
                return True
            hashset.add(n)    
       return False   
      
Time Complexity o(n)

Implemented using Hashset
A HashSet is a data structure that stores unique elements only.
In Python, a HashSet is implemented using a set.  
