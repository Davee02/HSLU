
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung09/al/aufgabe01
# Version: Mon Nov 13 17:50:17 CET 2023

from collections import deque


def bucket_sort(sequence, n):
  """
  Sorts the sequence.
  
  sequence: Sequence to be sorted.
  n: The upper-bound of all values in sequence: 0..(n-1).
  """
  buckets = [None] * n
  for i in range(len(buckets)):
    buckets[i] = deque()

  while len(sequence) > 0:
    element = sequence.popleft()
    buckets[element].append(element)

  pretty_print(buckets)
  
  for i in range(n):
    while len(buckets[i]):
      element = buckets[i].popleft()
      sequence.append(element)
    

def pretty_print(buckets):
  print(str(buckets).replace("deque", "").replace("(", "").replace(")", ""))
  
    
if __name__ == '__main__':
  
  my_list = [7, 1, 3, 7, 3, 7]
  sequence = deque(my_list)
  print(sequence)
  bucket_sort(sequence, 10)
  print(sequence)
  
 
  """ Session-Log:
  
  deque([7, 1, 3, 7, 3, 7])
  [[], [1], [], [3, 3], [], [], [], [7, 7, 7], [], []]
  deque([1, 3, 3, 7, 7, 7])
  
  """  
