
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung03/al/aufgabe02
# Version: Sun Oct  1 20:01:13 CEST 2023

import enum
from no_such_node_exception import NoSuchNodeException


ROOT_INDEX = 1

class VectorTree:
  
  class _child_side(enum.Enum):
    LEFT = enum.auto()
    RIGHT = enum.auto()

  def __init__(self):
    self._binary_tree = []
    self._binary_tree.append(None)
    self._binary_tree.append(None)
    self._size = 0
    
  def root(self):
    return self._binary_tree[1]
  
  def set_root(self, root):
    self._remove_node_at_pos(ROOT_INDEX)
    self._binary_tree[ROOT_INDEX] = root
    self._size = 1
    
  def parent(self, child):
    if self.is_root(child):
      return None
    index = self._position(child) // 2
    return self._binary_tree[index]
    
  def left_child(self, parent):
    index = self._position(parent) * 2
    if not self._has_node_at_position(index):
      return None
    return self._binary_tree[index]

  def right_child(self, parent):
    index = self._position(parent) * 2 + 1
    if not self._has_node_at_position(index):
      return None
    return self._binary_tree[index]

  def is_internal(self, node):
    has_left_child = self.left_child(node) is not None
    has_right_child = self.right_child(node) is not None
    return has_left_child or has_right_child

  def is_external(self, node):
    return not self.is_internal(node)
  
  def is_root(self, node):
    return self.root() == node

  def set_right_child(self, parent, child):
    parent_index = self._position(parent)
    child_index = parent_index * 2 + 1
    self._set_child_at_pos(child, child_index)
  
  def set_left_child(self, parent, child):
    parent_index = self._position(parent)
    child_index = parent_index * 2
    self._set_child_at_pos(child, child_index)
      
  def _set_child_at_pos(self, child, pos):
    self._assure_size(pos)
    self._remove_node_at_pos(pos)
    self._binary_tree[pos] = child
    self._size += 1

  def remove_right_child(self, parent):
    parent_index = self._position(parent)
    child_index = parent_index * 2 + 1
    self._remove_node_at_pos(child_index)

  def remove_left_child(self, parent):
    parent_index = self._position(parent)
    child_index = parent_index * 2
    self._remove_node_at_pos(child_index)

  def _remove_node_at_pos(self, pos):
    if not self._has_node_at_position(pos):
      return
    self._binary_tree[pos] = None
    self._size -= 1
    self._remove_node_at_pos(pos * 2) # left child
    self._remove_node_at_pos(pos * 2 + 1) # right child

  def size(self):
    return self._size

  def print_vector(self, message):
    print("\n" + message)
    print(self._binary_tree)

  def _position(self, node):
    try:
      return self._binary_tree.index(node)
    except ValueError:
      raise NoSuchNodeException("Node doesn't exist: " + node)
    
  def _has_node_at_position(self, pos):
    if pos > (len(self._binary_tree) - 1):
      return False
    return self._binary_tree[pos] != None
  
  def _assure_size(self, index):
    current_length = len(self._binary_tree)
    if index >= current_length:
      new_length = 2 * current_length
      i = current_length
      while i < new_length: 
        self._binary_tree.append(None)
        i += 1
