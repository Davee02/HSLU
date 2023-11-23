
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung10/al/aufgabe02
# Version: Fri Nov 17 16:52:43 CET 2023

import sys
from graph import Graph


if __name__ == '__main__':
  
  graph = Graph()
  u = graph.insert_vertex("U")
  v = graph.insert_vertex("V")
  w = graph.insert_vertex("W")
  a = graph.insert_edge(u, v, "a")
  b = graph.insert_edge(v, w, "b")
  graph.print_graph()
  
  if graph.opposite(u, a) is not v:
    print("ERROR: v is not opposite of u!")
    sys.exit(11)
  if not graph.are_adjacent(v, w):
    print("ERROR: v is not adjacent of w!")
    sys.exit(22)
  

""" Session-Log:

Graph:
U -> (V,a)
V -> (U,a)(W,b)
W -> (V,b)

"""
