
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung07/al/aufgabe01
# Version: Mon Oct 30 17:59:50 CET 2023

from binary_search_tree import BinarySearchTree
from tree_printer import TreePrinterAcc
from tree_printer import TreePrinter

if __name__ == '__main__':
  
  bst = BinarySearchTree()

  treePrinterAcc = TreePrinterAcc(bst)
  treePrinter = TreePrinter(treePrinterAcc)
  
  bst.insert(6, "Sechs")
  print("Inorder: " + bst.inorder())
  bst.insert(2, "Zwei")
  print("Inorder: " + bst.inorder())
  bst.insert(9, "Neun")
  print("Inorder: " + bst.inorder())
  bst.insert(1, "Eins")
  print("Inorder: " + bst.inorder())
  bst.insert(4, "Vier")
  print("Inorder: " + bst.inorder())
  bst.insert(8, "Acht")
  print("Inorder: " + bst.inorder())
  bst.insert(5, "Fuenf")
  print("Inorder: " + bst.inorder())
  treePrinter.print()
  print("remove(1): " + bst.remove(1))
  treePrinter.print()
  print("remove(4): " + bst.remove(4))
  treePrinter.print()
  print("remove(5): " + bst.remove(5))
  treePrinter.print()
  bst.insert(1, "Eins")
  bst.insert(4, "Vier")
  bst.insert(5, "Fuenf")
  treePrinter.print()
  print("remove(6): " + bst.remove(6))
  treePrinter.print()
  
  
""" Session-Log:

Inorder: (6/Sechs) 
Inorder: (2/Zwei) (6/Sechs) 
Inorder: (2/Zwei) (6/Sechs) (9/Neun) 
Inorder: (1/Eins) (2/Zwei) (6/Sechs) (9/Neun) 
Inorder: (1/Eins) (2/Zwei) (4/Vier) (6/Sechs) (9/Neun) 
Inorder: (1/Eins) (2/Zwei) (4/Vier) (6/Sechs) (8/Acht) (9/Neun) 
Inorder: (1/Eins) (2/Zwei) (4/Vier) (5/Fuenf) (6/Sechs) (8/Acht) (9/Neun) 
=== Tree: =========================
                    (6,Sechs)
     (2,Zwei)/                \(9,Neun)
(1,Eins)/ \(4,Vier)      (8,Acht)/
               \(5,Fuenf)
=== Tree. =========================
remove(1): Eins
=== Tree: =========================
               (6,Sechs)
(2,Zwei)/                \(9,Neun)
     \(4,Vier)      (8,Acht)/
          \(5,Fuenf)
=== Tree. =========================
remove(4): Vier
=== Tree: =========================
          (6,Sechs)
(2,Zwei)/           \(9,Neun)
     \(5,Fuenf)(8,Acht)/
=== Tree. =========================
remove(5): Fuenf
=== Tree: =========================
     (6,Sechs)
(2,Zwei)/      \(9,Neun)
          (8,Acht)/
=== Tree. =========================
=== Tree: =========================
                    (6,Sechs)
     (2,Zwei)/                \(9,Neun)
(1,Eins)/ \(4,Vier)      (8,Acht)/
               \(5,Fuenf)
=== Tree. =========================
remove(6): Sechs
=== Tree: =========================
               (5,Fuenf)
     (2,Zwei)/           \(9,Neun)
(1,Eins)/ \(4,Vier) (8,Acht)/
=== Tree. =========================

"""
