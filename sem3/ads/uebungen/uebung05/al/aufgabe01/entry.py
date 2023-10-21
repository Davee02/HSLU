
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung05/al/aufgabe01
# Version: Mon Oct 16 18:32:00 CEST 2023


class Entry:

  def __init__(self, key, value):
    self._key = key
    self._value = value
        
  def get_key(self):
    return self._key

  def get_value(self):
    return self._value

  def set_value(self, value):
    old_value = self._value
    self._value = value
    return old_value
  
  def __iter__(self):
    yield self._key
    yield self._value
    
  def __eq__(self, other):
    return (isinstance(other, type(self)) and tuple(self) == tuple(other))
    
  def __hash__(self):
    return hash(tuple(self))
  
  def __str__(self):
    return "(" + str(self._key) + "," + str(self._value) +")"
