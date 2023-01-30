#!/usr/bin/env python
# coding: utf-8

# # Selection Sort
# 
# Time Complexities :
# 
# Best  -  O(n2)
# 
# Worst   -  O(n2)
# 
# Average -  O(n2)

# In[4]:


def selection_sort(arr,size):
  
  for i in range(size):
    min_ind = i
    for j in range(min_ind+1,size):
      if(arr[j]<arr[min_ind]):
        min_ind = j
    arr[i], arr[min_ind] = arr[min_ind], arr[i]

if __name__=="__main__":

  arr = [44,22,1,5,-10,-2,77,11,3,55]
  print("Un-Sorted Array :",arr)
  size = len(arr)
  selection_sort(arr,size)
  print("Sorted Array :",arr)


# In[ ]:





# In[ ]:




