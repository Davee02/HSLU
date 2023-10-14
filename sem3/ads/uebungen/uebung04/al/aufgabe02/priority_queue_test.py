
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung04/al/aufgabe02
# Version: Tue Oct 10 09:56:22 CEST 2023

import sys
import random
from queue import PriorityQueue as PythonPQ
from priority_queue import PriorityQueue


def stress_test():
  print("\nStress-Test: ... ", end = "")
  NUMBER_OF_TESTS = 20000
  LENGTH_RANGE = 10
  DATA_RANGE = 10
  i = 0
  while i < NUMBER_OF_TESTS:
    length = random.choice(range(1, LENGTH_RANGE))
    randoms = []
    j = 0
    while j < length:
      randoms.append(int(random.uniform(0, DATA_RANGE)))
      j += 1
    ourPQ = PriorityQueue(length)
    pythonPQ = PythonPQ(length)
    for r in randoms:
      ourPQ.insert(r, "Value_" + str(r))
      pythonPQ.put(r)
    j = 0
    while j < length:
      if ourPQ.size() != pythonPQ.qsize():
        print("ERROR: wrong size!")
        print("randoms: " + str(randoms))
        sys.exit(1)
      our_removal = ourPQ.remove_min().get_key()
      their_removal = pythonPQ.get()
      if our_removal != their_removal:
        print("ERROR: wrong removeMin()!")
        print("randoms: " + str(randoms))
        sys.exit(2)
      j += 1
    if ourPQ.remove_min() != None:
      print("ERROR: removeMin() != None")
      print("randoms: " + str(randoms))
      sys.exit(3)
    i += 1
  print("o.k.")
    
  
  
if __name__ == '__main__':
  
  pq = PriorityQueue(7)

  print("insert()'s: ")
  pq.print()
  pq.insert(4, "D")
  pq.print()
  pq.insert(5, "E")
  pq.print()
  pq.insert(3, "C")
  pq.print()
  pq.insert(2, "B")
  pq.print()
  pq.insert(1, "A")
  pq.print()
  print("\nmin(): " + str(pq.min()))
  while pq.size() > 1:
    print("remove_min(): " + str(pq.remove_min()))
    pq.print()
  
  stress_test()


""" Session-Log::

insert()'s: 
[None, None, None, None, None, None, None, None]
[None, [(4,D),1], None, None, None, None, None, None]
[None, [(4,D),1], [(5,E),2], None, None, None, None, None]
[None, [(3,C),1], [(5,E),2], [(4,D),3], None, None, None, None]
[None, [(2,B),1], [(3,C),2], [(4,D),3], [(5,E),4], None, None, None]
[None, [(1,A),1], [(2,B),2], [(4,D),3], [(5,E),4], [(3,C),5], None, None]

min(): (1,A)
remove_min(): (1,A)
[None, [(2,B),1], [(3,C),2], [(4,D),3], [(5,E),4], None, None, None]
remove_min(): (2,B)
[None, [(3,C),1], [(5,E),2], [(4,D),3], None, None, None, None]
remove_min(): (3,C)
[None, [(4,D),1], [(5,E),2], None, None, None, None, None]
remove_min(): (4,D)
[None, [(5,E),1], None, None, None, None, None, None]

Stress-Test: ... o.k.

"""
