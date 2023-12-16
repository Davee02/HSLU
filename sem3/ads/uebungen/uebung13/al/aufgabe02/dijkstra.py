
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung13/al/aufgabe02
# Version: Fri Dec  8 18:48:12 CET 2023

import sys

from graphs.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from graphs.graph import Graph


class Dijkstra:

  def __init__(self):
    self._graph = None
    self._distances = self._get_distance_map()
    self._vertex_refs = self._get_locators_map()
    self._parents = self._get_parents_map()
    
  def distances(self, graph: Graph, source):
    self._graph = graph
    self._apq = self._get_adaptable_priority_queue()

    for vertex in graph.vertices():
      self._parents[vertex] = None
      distance = 0 if vertex == source else sys.maxsize
      self._distances[vertex] = distance
      vertex_reference_in_queue = self._apq.insert(distance, vertex)
      self._vertex_refs[vertex] = vertex_reference_in_queue

    while not self._apq.is_empty():
      (_, current_vertex) = self._apq.remove_min()

      for edge in graph.incident_edges(current_vertex):
        opposite_vertex = graph.opposite(current_vertex, edge)
        new_distance = self._distances[current_vertex] + edge.element()

        if new_distance < self._distances[opposite_vertex]:
          self._distances[opposite_vertex] = new_distance
          self._parents[opposite_vertex] = edge
          self._apq.replace_key(self._vertex_refs[opposite_vertex], new_distance)

  def get_graph(self):    
    return Graph()
  
  def _get_adaptable_priority_queue(self):    
    return AdaptableHeapPriorityQueue()
    
  def _get_distance_map(self):    
    return dict()

  def _get_locators_map(self):    
    return dict()

  def _get_parents_map(self):    
    return dict()
  
  def print_distances(self):
    print("\nDistances:")
    for v in self._graph.vertices():
      print(str(v) + ": " + str(self._distances.get(v)))
      
