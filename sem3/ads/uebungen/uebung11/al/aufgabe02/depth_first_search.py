
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung11/al/aufgabe02
# Version: Mon Nov 27 19:10:12 CET 2023

import enum


class DepthFirstSearch:
  
  class _VertexLabelDFS(enum.Enum):
    UNEXPLORED = enum.auto()
    VISITED = enum.auto()
    
  class _EdgeLabelDFS(enum.Enum):
    UNEXPLORED = enum.auto()
    DISCOVERY = enum.auto()
    BACK = enum.auto()
  
  def __init__(self): 
    self._vertex_map = dict()
    self._edge_map = dict()
    self._graph = None
    
  def search(self, graph):
    self._graph = graph
    self._vertex_map = graph.get_dfs_vertex_map()
    self._edge_map = graph.get_dfs_edge_map()
    
    for u in graph.vertices():
      self._vertex_map[u] = DepthFirstSearch._VertexLabelDFS.UNEXPLORED
    for e in graph.edges():
      self._edge_map[e] = DepthFirstSearch._EdgeLabelDFS.UNEXPLORED
    for v in graph.vertices():
      if self._vertex_map.get(v) is DepthFirstSearch._VertexLabelDFS.UNEXPLORED:
        self._search(graph, v)
      
  def _search(self, graph, v):
    print("DepthFirstSearch._search(): v = " + str(v))
    self._vertex_map[v] = DepthFirstSearch._VertexLabelDFS.VISITED

    for e in graph.incident_edges(v):
      print(f'  e = {e}')
      if self._edge_map.get(e) is DepthFirstSearch._EdgeLabelDFS.UNEXPLORED:
        w = graph.opposite(v, e)
        print(f'    w = {w}')
        if self._vertex_map.get(w) is DepthFirstSearch._VertexLabelDFS.UNEXPLORED:
          self._edge_map[e] = DepthFirstSearch._EdgeLabelDFS.DISCOVERY
          self._search(graph, w)
        else:
          self._edge_map[e] = DepthFirstSearch._EdgeLabelDFS.BACK

  def print_maps(self):
    self._graph.printing_maps(True)
    print("\nDepthFirstSearch.print_maps():")
    print("Vertex-Map : {", end = "")
    mappings = list()
    for v in self._vertex_map:
      mappings.append(v.__str__() + "=" + self._get_enum_name(self._vertex_map[v]))
    print(", ".join(mappings), end = "")
    print("}")
    print("Edge-Map   : {", end = "")
    mappings = list()
    for e in self._edge_map:
      mappings.append(e.__str__() + "=" + self._get_enum_name(self._edge_map[e]))
    mappings.sort()
    print(", ".join(mappings), end = "")
    print("}")
    self._graph.printing_maps(False)
    
  def _get_enum_name(self, enum_value):
    return enum_value.__str__().split(".")[1]
    
    
