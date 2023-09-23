
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung01/al/aufgabe03
# Version: Sun Sep 10 18:13:26 CEST 2023

def recursive_sum(n):
  if n == 0:
    return 0
  return n + recursive_sum(n - 1)
  
  
if __name__ == '__main__':  
  
  n = 100
  print("Sum of 0..100 recursively                    = ", recursive_sum(n))
  print("Sum of 0..100 explicitly : n * (n + 1) / 2)  = ", (n * (n + 1) // 2))


  """ Session-Log:

  Sum of 0..100 recursively                    = 5050
  Sum of 0..100 explicitly : n * (n + 1) / 2)  = 5050

  """  
