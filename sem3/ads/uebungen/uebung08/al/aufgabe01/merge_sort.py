
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung08/al/aufgabe01
# Version: Sat Nov  4 16:55:39 CET 2023

import random
import sys
from time import time


def merge_sort(s):
  """
  Sorts a list with the merge-sort algorithm.
  
  Precondition: Length must be 2^x.
  s: Sequence to be sorted.
  Returns the sorted sequence.
  """
  n = len(s)
  if n > 1:
    s1, s2 = partition(s, n//2)
    s1 = merge_sort(s1)
    s2 = merge_sort(s2)
    s = merge(s1, s2)

  return s


def partition(s, n):
  return s[:n],s[n:]

def merge(a, b):
  n = len(a) * 2
  s = []

  while len(a) > 0 and len(b) > 0:
    if a[0] < b[0]:
      s.append(a.pop(0))
    else:
      s.append(b.pop(0))

  while len(a) > 0:
    s.append(a.pop(0))
  
  while len(b) > 0:
    s.append(b.pop(0))

  return s 


def verify(orginalData, sortedData):
  correctSorted = orginalData.copy()
  correctSorted.sort()
  for i in range(len(orginalData)):
    if(correctSorted[i] != sortedData[i]):
      print("ERROR: wrong sorted!")
      print("Orginal : ", orginalData)
      print("Sorted  : ", sortedData)
      print(f"index[{i}]: should be: {correctSorted[i]}, but is: {sortedData[i]}")
      sys.exit(1)
  
if __name__ == '__main__':
  
  my_list = [7, 2, 9, 4, 3, 8, 6, 1]
  orginal_list = my_list.copy()
  print(my_list)

  my_list = merge_sort(my_list)
  
  print(my_list)
  verify(orginal_list, my_list)
        
  # Makeing some test to measure the time needed of merge_sort().
  # Creating int-lists, beginning with length of 2^min_exponent
  # until the last array with length of 2^max_exponent.
  min_exponent = 10
  max_exponent = 15
  last_time = sys.float_info.max
  for exp in range(min_exponent, max_exponent + 1):
    length = pow(2, exp)
    MEASUREMENTS = 10
    min_time = sys.float_info.max
    for i in range(MEASUREMENTS):
      data = list(range(length))
      random.shuffle(data)
      #list.reverse(data)
      start = time()
      merge_sort(data)
      end = time()
      time_spent = end - start
      if(time_spent < min_time):
        min_time = time_spent
    print(f"List-Size: {length:6,d}         Time: {min_time*1e3:7.1f} ms          Ratio to last: {min_time / last_time:.1f}")
    last_time = min_time


  """ Session-Log:
  
  [7, 2, 9, 4, 3, 8, 6, 1]
  [1, 2, 3, 4, 6, 7, 8, 9]
  List-Size:  1,024         Time:   ???.? ms          Ratio to last: 0.0
  List-Size:  2,048         Time:   ???.? ms          Ratio to last: ?.?
  List-Size:  4,096         Time:   ???.? ms          Ratio to last: ?.?
  List-Size:  8,192         Time:   ???.? ms          Ratio to last: ?.?
  List-Size: 16,384         Time:   ???.? ms          Ratio to last: ?.?
  List-Size: 32,768         Time:   ???.? ms          Ratio to last: ?.?
  
  """  
