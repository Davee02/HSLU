
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung06/al/aufgabe02
# Version: Mon Oct 23 19:05:11 CEST 2023

from binary_search_tree import BinarySearchTree
from tree_printer import TreePrinterAcc
from tree_printer import TreePrinter

if __name__ == '__main__':
  
  bst = BinarySearchTree()

  treePrinterAcc = TreePrinterAcc(bst)
  treePrinter = TreePrinter(treePrinterAcc)
  print("Height: " + str(bst.height()))
  bst.insert(5, "Fuenf")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  bst.insert(3, "Drei")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  bst.insert(6, "Sechs")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  bst.insert(1, "Eins")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  bst.insert(2, "Zwei:1")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  bst.insert(4, "Vier:1")
  treePrinter.print()
  print("MaxDepth: " + str(bst.height()))
  print("insert(4, \"Vier:2\")")
  bst.insert(4, "Vier:2")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  print("insert(2, \"Zwei:2\")")
  bst.insert(2, "Zwei:2")
  treePrinter.print()
  print("Height: " + str(bst.height()))
  
  # Some Tests:
  print("find(3): " + str(bst.find(3)))
  print("find(2): " + str(bst.find(2)))
  print("find(7): " + str(bst.find(7)))
    
  
""" Session-Log:

Height: -1
=== Tree: =========================
(5,Fuenf)
=== Tree. =========================
Height: 0
=== Tree: =========================
     (5,Fuenf)
(3,Drei)/
=== Tree. =========================
Height: 1
=== Tree: =========================
     (5,Fuenf)
(3,Drei)/ \(6,Sechs)
=== Tree. =========================
Height: 1
=== Tree: =========================
          (5,Fuenf)
     (3,Drei)/ \(6,Sechs)
(1,Eins)/
=== Tree. =========================
Height: 2
=== Tree: =========================
               (5,Fuenf)
          (3,Drei)/ \(6,Sechs)
(1,Eins)/
     \(2,Zwei:1)
=== Tree. =========================
Height: 3
=== Tree: =========================
                    (5,Fuenf)
          (3,Drei)/      \(6,Sechs)
(1,Eins)/      \(4,Vier:1)
     \(2,Zwei:1)
=== Tree. =========================
MaxDepth: 3
insert(4, "Vier:2")
=== Tree: =========================
                    (5,Fuenf)
          (3,Drei)/      \(6,Sechs)
(1,Eins)/      \(4,Vier:2)
     \(2,Zwei:1)
=== Tree. =========================
Height: 3
insert(2, "Zwei:2")
=== Tree: =========================
                    (5,Fuenf)
          (3,Drei)/      \(6,Sechs)
(1,Eins)/      \(4,Vier:2)
     \(2,Zwei:2)
=== Tree. =========================
Height: 3
find(3): Drei
find(2): Zwei:2
find(7): None

"""
