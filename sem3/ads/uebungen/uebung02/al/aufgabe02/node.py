
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung02/al/aufgabe02
# Version: Mon Sep 25 19:08:47 CEST 2023

class Node: 

  def __init__(self, e = None, p = None, n = None):
    self._element = e
    self._next = n
    self._prev = p
        
  def set_element(self, new_elem):
    self._element = new_elem
  
  def set_next(self, new_next):
    self._next = new_next
    
  def set_prev(self, new_prev):
    self._prev = new_prev
    
  def get_element(self):  
    return self._element
  
  def get_next(self):
    return self._next
  
  def get_prev(self):
    return self._prev
  
  
