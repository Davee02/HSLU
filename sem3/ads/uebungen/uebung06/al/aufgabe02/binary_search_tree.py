
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung06/al/aufgabe02
# Version: Mon Oct 23 19:05:11 CEST 2023


class BinarySearchTree:
  """
  A Binary-Search-Tree with internal nodes which store key/values and 
  external nodes as 'Leave-Marker' (without key/values).
  """
  
  class _Node:
    
    def __init__(self, bst):
      self._bst = bst  # the Binary-Search-Tree
      self._key = None
      self._value = None
      self._left = None
      self._right = None
      
    def get_key(self):
      return self._key
    
    def set_value(self, value):
      self._value = value
      
    def get_value(self):
      return self._value
    
    def get_left(self):
      return self._left
    
    def get_right(self):
      return self._right
    
    def is_external(self):
      return self._left == None and self._right == None
    
    def convert_to_internal_node(self, key, value):
      self._key = key
      self._value = value
      self._left = self._bst._new_node()
      self._right = self._bst._new_node()
    
    # End of class _Node  
    

  def __init__(self):
    self._root = self._new_node()
        
  def _new_node(self):
    """
    Factory-Method: Creates a new node.

    Returns a new created node.
    """
    return BinarySearchTree._Node(self)
  
  def height(self):
    """
    Calculates the height of this tree.
    
    Returns the height. For an empty tree: -1
    """
    return self._height(self._root)
  
  
  def _height(self, node):
    """
    Calculates recursively the height of the subtree below node.
    
    node: The root of the subtree.
    Returns the height of this subtree. For an empty tree: -1
    """
    
    if node.is_external():
      return -1
    
    left_height = self._height(node.get_left())
    right_height = self._height(node.get_right())

    if (left_height > right_height):
      return left_height + 1
    else:
      return right_height + 1

  def find(self, key):
    """
    Searches for key in the tree. 
    
    key: The key to search for.
    Returns the associated value or None if key is not found.
    """
    node_found = self._search(key, self._root)
    return None if node_found.is_external() else node_found.get_value()
  
  def _search(self, key, node):
    """
    Searches recursively for key in the subtree with node as root. 
    
    key: The key to search for.
    node: The root of the subtree.
    Returns: If key found the corresponding internal node, 
             else the corresponding external node.
    """
    
    if node.is_external() or key == node.get_key():
      return node
    elif key < node.get_key():
      return self._search(key, node.get_left())
    else:
      return self._search(key, node.get_right())
  
  def insert(self, key, value):
    """
    Inserts a key and its associated value into the tree in a way, that a 
    inorder-traverse will return the elements in sorted order.
    """
    found_node = self._search(key, self._root)
    if found_node.is_external():
      found_node.convert_to_internal_node(key, value)
    else:
      found_node.set_value(value)
