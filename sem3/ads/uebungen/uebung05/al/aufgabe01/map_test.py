
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Oct 16 18:32:00 CEST 2023

from map_impl import MapImpl


if __name__ == '__main__':
  
  the_map = MapImpl()
  
  print("map.size()     : " + str(the_map.size()))
  print("map.is_empty() : " + str(the_map.is_empty()))
  
  print("\nmap.put(1, \"one\") : " + str(the_map.put(1, "one")))
  the_map.printMap()
  print("map.size()     : " + str(the_map.size()))
  print("map.is_empty() : " + str(the_map.is_empty()))
  
  the_map.put(2, "two")
  the_map.put(3, "three 1")
  the_map.printMap("\n")
  
  print("\nmap.put(3, \"three 2\") : " + str(the_map.put(3, "three 2")))
  the_map.printMap()

  print()
  print("map.get(2) : " + str(the_map.get(2)))
  print("map.get(4) : " + str(the_map.get(4)))
  
  print("\nmap.remove(2) : " + str(the_map.remove(2)))
  the_map.printMap()

  print("\nmap.key_set()  : " + str(the_map.key_set()))
  print("map.values()   : " + str(the_map.values()))
  print("map.entrySet() : " + ",".join(map(str, the_map.entry_set())))

  
  
""" Session-Log (Note: The order of the entries is irrelevant): 

map.size()     : 0
map.is_empty() : True

map.put(1, "one") : None
Printing map (1 Entries): 
    1: one
map.size()     : 1
map.is_empty() : False

Printing map (3 Entries): 
    1: one
    2: two
    3: three 1

map.put(3, "three 2") : three 1
Printing map (3 Entries): 
    1: one
    2: two
    3: three 2

map.get(2) : two
map.get(4) : None

map.remove(2) : two
Printing map (2 Entries): 
    1: one
    3: three 2

map.key_set()  : {1, 3}
map.values()   : ['one', 'three 2']
map.entrySet() : (1,one),(3,three 2)

"""
