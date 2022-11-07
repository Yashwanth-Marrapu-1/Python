# -*- coding: utf-8 -*-
"""Bubble Sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10tHf8HZ2Ctwi0nYyJOplA5eakTQV3VAC

**Bubble Sort**

**Time Complexities :** 

**Best	   -  O(n)**

**Worst	   -  O(n2)**

**Average	 -  O(n2)**
"""

def bubble_sort(arr):
  
  for i in range(len(arr)):
    swap_occurs = False
    for j in range(0,len(arr)-i-1):
      if(arr[j]>arr[j+1]):
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        swap_occurs = True
    if(swap_occurs == False):
      break
    print("swap occured")

if __name__=="__main__":

  arr = [-10,44,22,1,5,77,-11,3,55]
  print("Un-Sorted Array :",arr)
  bubble_sort(arr)
  print("Sorted Array :",arr)