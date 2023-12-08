
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung12/al/aufgabe02
# Version: Fri Dec  1 17:48:30 CET 2023

import sys

from graphs.graph import Graph
from directed_dfs import DirectedDFS


if __name__ == '__main__':
  
  print("Example this exercise 12, task 1c:\n")
  
  graph = Graph()

  v_01 = graph.insert_vertex("01")
  v_02 = graph.insert_vertex("02")
  v_03 = graph.insert_vertex("03")
  v_04 = graph.insert_vertex("04")
  v_05 = graph.insert_vertex("05")
  v_06 = graph.insert_vertex("06")
  v_07 = graph.insert_vertex("07")
  v_08 = graph.insert_vertex("08")
  v_09 = graph.insert_vertex("09")
  v_10 = graph.insert_vertex("10")

  graph.insert_edge(v_01, v_08)
  graph.insert_edge(v_01, v_10)
  graph.insert_edge(v_02, v_06)
  graph.insert_edge(v_03, v_01)
  graph.insert_edge(v_03, v_07)
  graph.insert_edge(v_03, v_06)
  graph.insert_edge(v_04, v_10)
  graph.insert_edge(v_04, v_05)
  graph.insert_edge(v_05, v_10)
  graph.insert_edge(v_06, v_07)
  graph.insert_edge(v_07, v_08)
  graph.insert_edge(v_07, v_02)
  graph.insert_edge(v_08, v_09)
  graph.insert_edge(v_09, v_08)
  graph.insert_edge(v_10, v_03)
  
  directed_dfs = DirectedDFS()
  directed_dfs.search(graph)
  
  directed_dfs.print_maps()
  
  if len(directed_dfs._edge_map) != 15:
    print("\nERROR: DirectedDFS.edgeMap should have a size of 15 !")
    sys.exit(11)

  
""" Session-Log:

Example this exercise 12, task 1c:

DirectedDFS.search() : 01
Testing              : 01-08: DISCOVERY
DirectedDFS.search() : 08
Testing              : 08-09: DISCOVERY
DirectedDFS.search() : 09
Testing              : 09-08: BACK
Testing              : 01-10: DISCOVERY
DirectedDFS.search() : 10
Testing              : 10-03: DISCOVERY
DirectedDFS.search() : 03
Testing              : 03-01: BACK
Testing              : 03-06: DISCOVERY
DirectedDFS.search() : 06
Testing              : 06-07: DISCOVERY
DirectedDFS.search() : 07
Testing              : 07-02: DISCOVERY
DirectedDFS.search() : 02
Testing              : 02-06: BACK
Testing              : 07-08: CROSS
Testing              : 03-07: FORWARD
DirectedDFS.search() : 04
Testing              : 04-05: DISCOVERY
DirectedDFS.search() : 05
Testing              : 05-10: CROSS
Testing              : 04-10: CROSS

DirectedDFS.print_maps():
Vertex-Map : {01=VISITED, 02=VISITED, 03=VISITED, 04=VISITED, 05=VISITED, 06=VISITED, 07=VISITED, 08=VISITED, 09=VISITED, 10=VISITED}
Edge-Map   : {01-08=DISCOVERY, 01-10=DISCOVERY, 02-06=BACK, 03-01=BACK, 03-06=DISCOVERY, 03-07=FORWARD, 04-05=DISCOVERY, 04-10=CROSS, 05-10=CROSS, 06-07=DISCOVERY, 07-02=DISCOVERY, 07-08=CROSS, 08-09=DISCOVERY, 09-08=BACK, 10-03=DISCOVERY}

"""
