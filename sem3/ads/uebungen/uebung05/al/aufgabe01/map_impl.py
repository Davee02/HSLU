
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Oct 16 18:32:00 CEST 2023

from entry import Entry


class MapImpl:
  
  def __init__(self):  
    self._list = []
  
  def size(self):
    return len(self._list)
  
  def is_empty(self):
    return self.size() < 1
  
  def put(self, key, value):
    existing_entry = self._get_entry(key)
    if existing_entry == None:
      self._list.append(Entry(key, value))
      return None
    existing_entry_copy = self.get(key)
    existing_entry.set_value(value)
    return existing_entry_copy
      
  def get(self, key):
    entry = self._get_entry(key)
    return None if entry == None else entry.get_value()

  def remove(self, key):
    for entry in self._list:
      if entry.get_key() == key:
        self._list.remove(entry)
        return entry.get_value()
    return None
    
  def values(self):
    values = []
    for entry in self._list:
      values.append(entry.get_value())
    return values
  
  def key_set(self):
    keys = []
    for entry in self._list:
      keys.append(entry.get_key())
    return set(keys)
  
  def entry_set(self):
    return set(self._list)
  
  def printMap(self, prefix = ""):
    print(prefix + "Printing map (" + str(self.size()) + " Entries): ")
    for e in self._list:
      print(f"  {e.get_key():3d}: {e.get_value()}")
      
  def _get_entry(self, key):
    for entry in self._list:
      if entry.get_key() == key:
        return entry
    return None