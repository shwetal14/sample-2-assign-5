#!/usr/bin/env python
# coding: utf-8

# In[1]:



class Solution(object):
   def myPow(self, x, n):
      power = abs(n)
      res = 1
      while power:
         if power & 1:
            res*=x
         x*=x
         power>>=1
      if n<0:
         return 1/res
      return res
ob1 = Solution()
print(ob1.myPow(10, 2))


# In[ ]:





# In[ ]:




