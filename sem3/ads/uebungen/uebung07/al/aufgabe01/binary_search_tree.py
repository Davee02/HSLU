
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung07/al/aufgabe01
# Version: Mon Oct 30 17:59:50 CET 2023


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
      
    def set_key(self, key):
      self._key = key
      
    def get_key(self):
      return self._key
    
    def set_value(self, value):
      self._value = value
      
    def get_value(self):
      return self._value
    
    def set_left(self, left):
      self._left = left
      
    def get_left(self):
      return self._left
    
    def set_right(self, right):
      self._right = right
    
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
    node_found = self._search(key, self._root, None)
    return None if node_found.is_external() else node_found.get_value()
  
  def _search(self, key, node, path_to_root):
    """
    Searches recursively for key in the subtree with node as root. 
    
    key: The key to search for.
    node: The root of the subtree.
    path_to_root: The path from the returned node to root.
    Returns: If key found the corresponding internal node, 
             else the corresponding external node.
    """
    if path_to_root != None:
      path_to_root.insert(0, node)
    if node.is_external() or key == node.get_key():
      return node
    elif key < node.get_key():
      return self._search(key, node.get_left(), path_to_root)
    else:
      return self._search(key, node.get_right(), path_to_root)
  
  def insert(self, key, value):
    """
    Inserts a key and its associated value into the tree in a way, that a 
    inorder-traverse will return the elements in sorted order.
    """
    found_node = self._search(key, self._root, None)
    if found_node.is_external():
      found_node.convert_to_internal_node(key, value)
    else:
      found_node.set_value(value)
  
  def inorder(self):
    """
    Performs an inorder-traverse and returns all key/values as a string.
    
    Returns a string with all key/value-pairs of all nodes in inorder.
    """
    return self._inorder(self._root, "")
  
  def _inorder(self, node, inorderString):
    left_child = node.get_left()
    right_child = node.get_right()
    
    if not left_child.is_external():
      inorderString = self._inorder(left_child, inorderString)
    
    inorderString += f'({node.get_key()}/{node.get_value()}) '

    if not right_child.is_external():
      inorderString = self._inorder(right_child, inorderString)

    return inorderString
  
  def remove(self, key):
    path_to_root = list()
    node_found = self._search(key, self._root, path_to_root)
    if node_found.is_external():
      return None

    left_child = node_found.get_left()
    right_child = node_found.get_right()

    if left_child.is_external() and right_child.is_external():
      return self._removeExternal(left_child, path_to_root)
    elif left_child.is_external() and not right_child.is_external():
      return self._removeExternal(left_child, path_to_root)
    elif not left_child.is_external() and right_child.is_external():
      return self._removeExternal(right_child, path_to_root)
    else:
      path_to_root = list()
      w = self._get_inorderPredecessor(node_found.get_left(), path_to_root)
      value = node_found.get_value()
      node_found.set_key(w.get_key())
      node_found.set_value(w.get_value())
      self._removeExternal(w, path_to_root)
      return value

  def _get_inorderPredecessor(self, node, path_to_root):
    if node.is_external():
      return path_to_root[0]
    path_to_root.insert(0, node)
    return self._get_inorderPredecessor(node.get_right(), path_to_root)

  def _removeExternal(self, external_node, path_to_root):
    """
    Removes an external.
    
    externalNode: The external Node to delete together with its parent.
    pathToRoot: The path from the parent of the external node to the root.
    Returns the value of the parent.
    """

    parent = path_to_root[0]

    node_to_relink = parent.get_right() if parent.get_left() == external_node else parent.get_left()

    if parent != self._root:
      grand_parent = path_to_root[1]
      if grand_parent.get_left() == parent:
        grand_parent.set_left(node_to_relink)
      else:
        grand_parent.set_right(node_to_relink)
    else:
      self._root = node_to_relink

    return parent.get_value()
