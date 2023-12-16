# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from graphs.heap_priority_queue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
  """A locator-based priority queue implemented with a binary heap."""

  #------------------------------ nested Locator class ------------------------------
  class Locator(HeapPriorityQueue._Item):
    """Token for locating an entry of the priority queue."""
    __slots__ = '_index'                 # add index as additional field

    def __init__(self, k, v, j):
      super().__init__(k,v)
      self._index = j

  #------------------------------ nonpublic behaviors ------------------------------
  # override swap to record new indices
  def _swap(self, i, j):
    super()._swap(i,j)                   # perform the swap
    self._data[i]._index = i             # reset locator index (post-swap)
    self._data[j]._index = j             # reset locator index (post-swap)

  def _bubble(self, j):
    if j > 0 and self._data[j] < self._data[self._parent(j)]:
      self._upheap(j)
    else:
      self._downheap(j)

  #------------------------------ public behaviors ------------------------------
  def insert(self, key, value):
    """Insert a key-value pair."""
    print("APQ.insert(" + str(key) + ", " + str(value) + ")")
    token = self.Locator(key, value, len(self._data)) # initiaize locator index
    self._data.append(token)
    self._upheap(len(self._data) - 1)
    return token

  def replace_key(self, loc, newkey):
    """Update the key for the entry identified by Locator loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    oldkey = loc._key
    loc._key = newkey
    self._bubble(j)
    return oldkey

  def replace_value(self, loc, newvalue):
    """Update the value for the entry identified by Locator loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    oldvalue = loc._value
    loc._value = newvalue
    return oldvalue

  def remove(self, loc):
    """Remove and return the (k,v) pair identified by Locator loc."""
    j = loc._index
    if not (0 <= j < len(self) and self._data[j] is loc):
      raise ValueError('Invalid locator')
    if j == len(self) - 1:                # item at last position
      self._data.pop()                    # just remove it
    else:
      self._swap(j, len(self)-1)          # swap item to the last position
      self._data.pop()                    # remove it from the list
      self._bubble(j)                     # fix item displaced by the swap
    return (loc._key, loc._value)             
