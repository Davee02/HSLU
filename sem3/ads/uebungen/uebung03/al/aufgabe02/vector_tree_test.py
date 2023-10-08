
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung03/al/aufgabe02
# Version: Sun Oct  1 20:01:13 CEST 2023

from vector_tree import VectorTree
from vector_tree import NoSuchNodeException

if __name__ == '__main__':
  
  vt = VectorTree()
  
  vt.print_vector("Empty tree:")
    
  if vt.size() != 0:
    raise Exception("Bad size: " + str(vt.size()) + " != 0")
  
  if vt.root() != None:
      raise Exception("vt.root() != None")
    
  a = 'A'
  vt.set_root(a)
  vt.print_vector("Setting root with 'A':")
  if vt.size() != 1:
    raise Exception("Bad size: " + str(vt.size()) + " != 1")
  if not vt.is_root(a):
    raise Exception("not vt.root(a)")
  if vt.root() != a:
    raise Exception("vt.root() != a: " + vt.root())
  if not vt.is_external(a):
    raise Exception("not vt.is_external(a)")
  if vt.parent(a) != None:
    raise Exception("vt.parent(a) != None")
  

  d = 'D'
  vt.set_right_child(vt.root(), d)
  vt.print_vector("Setting right child of 'A' with 'D':")
  if  vt.size() != 2:
    raise Exception("Bad size: " + str(vt.size()) + " != 2")
  if not vt.right_child(vt.root()) == d:
    raise Exception("not vt.right_child(vt.root()) == d : " + vt.right_child(vt.root()))
  if not vt.is_external(d):
    raise Exception("not vt.is_external(d)")
  if not vt.is_internal(vt.root()):
    raise Exception("!vt.is_internal(vt.root()")
  if not vt.parent(d) == a:
    raise Exception("not vt.parent(d) == a")
    
    
  b = 'B'
  vt.set_left_child(vt.root(), b)
  vt.print_vector("Setting left child of 'A' with 'B':")
  if vt.size() != 3:
    raise Exception("Bad size: " + str(vt.size()) + " != 3")

  f = 'F'
  vt.set_right_child(b, f)
  vt.print_vector("Setting right child of 'B' with 'F':")
    
  h = 'H'
  vt.set_right_child(f, h)
  vt.print_vector("Setting right child of 'F' with 'H':")
  
  
  
  g = 'G'
  vt.set_left_child(f, g)
  vt.print_vector("Setting left child of 'F' with 'G':")
  if vt.size() != 6:
    raise Exception("Bad size: " + str(vt.size()) + " != 6")
  if not vt.is_internal(f):
    raise Exception("not vt.is_internal(f)")
  if not vt.is_external(h):
    raise Exception("not vt.is_external(h)")
  if not vt.right_child(vt.right_child(vt.left_child(vt.root()))) == h:
    raise Exception("not vt.right_child(vt.right_child(vt.left_child(vt.root()))) == h")

  vt.remove_left_child(b)
  if vt.size() != 6:
    raise Exception("Bad size: " + str(vt.size()) + " != 6")

  vt.remove_right_child(b)
  vt.print_vector("Removing right child of 'B':")
  if vt.size() != 3:
    raise Exception("Bad size: " + str(vt.size()) + " != 3")
  if not vt.is_external(b):
    raise Exception("not vt.is_external(b)")
    
  vt.set_right_child(d, 'J')
  vt.print_vector("Setting right child of 'D' with 'J':")

  vt.set_right_child(a, 'X')
  vt.print_vector("Setting right child of root 'A' with 'X':")
  if vt.size() != 3:
    raise Exception("Bad size: " + str(vt.size()) + " != 3")

  vt.set_root('Y')
  vt.print_vector("Setting root with 'Y':")
  if vt.size() != 1:
    raise Exception("Bad size: " + str(vt.size()) + " != 1")

  print("\nTesting if root is external: ", end = "")
  if not vt.is_external(vt.root()):
    raise Exception("not vt.is_external(vt.root())")
  print("o.k.")

  print("\nAsking for node which does not exist: ", end = "")
  rightChild = vt.right_child('Y')
  if rightChild != None:
    raise Exception("rightChild != None")
  print("o.k.")
    
  print("\nUsing node which does not exist: ", end = "")
  noSuchNodeException = None
  try: 
    vt.set_right_child('A', 'B')
  except (NoSuchNodeException) as e:
    noSuchNodeException = e
  if noSuchNodeException == None:
    raise Exception("NoSuchNodeException missing!")
  print("o.k.")

 
  
""" Session-Log::

Empty tree:
[None, None]

Setting root with 'A':
[None, 'A']

Setting right child of 'A' with 'D':
[None, 'A', None, 'D']

Setting left child of 'A' with 'B':
[None, 'A', 'B', 'D']

Setting right child of 'B' with 'F':
[None, 'A', 'B', 'D', None, 'F', None, None]

Setting right child of 'F' with 'H':
[None, 'A', 'B', 'D', None, 'F', None, None, None, None, None, 'H', None, None, None, None]

Setting left child of 'F' with 'G':
[None, 'A', 'B', 'D', None, 'F', None, None, None, None, 'G', 'H', None, None, None, None]

Removing right child of 'B':
[None, 'A', 'B', 'D', None, None, None, None, None, None, None, None, None, None, None, None]

Setting right child of 'D' with 'J':
[None, 'A', 'B', 'D', None, None, None, 'J', None, None, None, None, None, None, None, None]

Setting right child of root 'A' with 'X':
[None, 'A', 'B', 'X', None, None, None, None, None, None, None, None, None, None, None, None]

Setting root with 'Y':
[None, 'Y', None, None, None, None, None, None, None, None, None, None, None, None, None, None]

Testing if root is external: o.k.

Asking for node which does not exist: o.k.

Using node which does not exist: o.k.

"""
