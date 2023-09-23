 
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung01/al/aufgabe04
# Version: Sun Sep 10 18:14:10 CEST 2023

import random
import sys
from time import time

def insertion_sort(data):
  if (len(data) < 2):
    return data
  
  for i in range (1, len(data)):
    j = i - 1
    val = data[i]
    while j >= 0 and data[j] > val:
      data[j+1] = data[j]
      j -= 1
    data[j+1] = val

  return data

def verify(orginalData, sortedData):
  correctSorted = orginalData.copy()
  correctSorted.sort()
  for i in range(len(orginalData)):
    if correctSorted[i] != sortedData[i]:
      print("ERROR: wrong sorted!")
      print("Orginal : ", orginalData)
      print("Sorted  : ", sortedData)
      print(f"index[{i}]: should be: {correctSorted[i]}, but is: {sortedData[i]}")
      sys.exit(1)
  

if __name__ == '__main__':
  
  data = [5, 4, 2, 3, 1]
  orginalData = data.copy()
  print(data)
  
  insertion_sort(data)
  
  print(data)
  verify(orginalData, data)
  
  # Makeing some test to measure the time needed of insertion_sort().
  # Creating int-lists, beginning with length of 2^minExponent
  # until the last array with length of 2^maxExponent.
  minExponent =  8
  maxExponent = 12
  lastTime = sys.float_info.max
  for exp in range(minExponent, maxExponent + 1):
    length = pow(2, exp)
    MEASUREMENTS = 10
    minTime = sys.float_info.max
    for i in range(MEASUREMENTS):
      data = list(range(length))
      random.shuffle(data)
      start = time()
      insertion_sort(data)
      end = time()
      timeSpent = end - start
      if timeSpent < minTime:
        minTime = timeSpent
    print(f"List-Size: {length:6,d}         Time: {minTime*1e3:7.1f} ms          Ratio to last: {minTime / lastTime:.1f}")
    lastTime = minTime
    
    
  """ Session-Log:
  
  [5, 4, 2, 3, 1]
  [1, 2, 3, 4, 5]
  List-Size:    256         Time:     3.0 ms          Ratio to last: 0.0
  List-Size:    512         Time:    12.6 ms          Ratio to last: 4.3
  List-Size:  1,024         Time:    50.9 ms          Ratio to last: 4.0
  List-Size:  2,048         Time:   202.7 ms          Ratio to last: 4.0
  List-Size:  4,096         Time:   875.6 ms          Ratio to last: 4.3
  
  """  
    
  
