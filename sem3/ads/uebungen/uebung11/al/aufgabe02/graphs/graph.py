
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung11/graphs
# Version: Sun Nov 28 17:43:55 CET 2021

from graphs.graph_impl import GraphImpl

class Graph:
  
  def __init__(self):
    self._graph = GraphImpl()
    
  def num_vertices(self):
    return self._graph.vertex_count()
    
  def num_edges(self):
    return self._graph.edge_count()
  
  def vertices(self):
    return self._graph.vertices()
  
  def edges(self):
    return self._graph.edges()
  
  def replace_in_vertex(self, v, element):
    self._validate_vertex(v)
    return v.replace(element)
  
  def replace_in_edge(self, e, element):
    self._validate_edge(e)
    return e.replace(element)
  
  def incident_edges(self, v):
    self._validate_vertex(v)
    return self._graph.incident_edges(v)
  
  def end_vertices(self, e):
    self._validate_edge(e)
    end_vertices = e.endpoints() 
    return (end_vertices[0], end_vertices[1])
  
  def opposite(self, v, e):
    """
    Raises a ValueError if edge is not incident to vertex. 
    """
    self._validate_vertex(v)
    self._validate_edge(e)
    vertices = self.end_vertices(e)
    if v is vertices[0]:
      return vertices[1]
    elif v is vertices[1]:
      return vertices[0]
    else:
      raise ValueError("Edge is not incident to vertex")
    
  def are_adjacent(self, v, w):
    self._validate_vertex(v)
    self._validate_vertex(w)
    inc_v = self.incident_edges(v)
    inc_w = self.incident_edges(w)
    if len(inc_v) < len(inc_w):
      inc = inc_v
    else:
      inc = inc_w
    for e in inc:
      end_vertices = self.end_vertices(e)
      if (end_vertices[0] is v and end_vertices[1] is w) \
      or (end_vertices[0] is w and end_vertices[1] is v):
        return True 
    return False 
  
  def insert_vertex(self, element):
    v = self._graph.insert_vertex(element)
    return v
  
  def insert_edge(self, v, w):
    self._validate_vertex(v)
    self._validate_vertex(w)
    e = self._graph.insert_edge(v, w, "")
    return e
  
  def remove_vertex(self, v):
    edges = list(self.incident_edges(v))
    for e in edges:
      self.remove_edge(e)
    del self._graph._outgoing[v]
    return v.element()
  
  def remove_edge(self, e):
    self._validate_edge(e)
    end_vertices = self.end_vertices(e)
    del self._graph._outgoing[end_vertices[0]][end_vertices[1]]
    del self._graph._outgoing[end_vertices[1]][end_vertices[0]]
    return e.element()
  
  def get_dfs_vertex_map(self):
    return dict()
  
  def get_dfs_edge_map(self):
    return dict()
    
  def _validate_vertex(self, v):
    return self._graph._validate_vertex(v)
  
  def _validate_edge(self, e):
    return self._graph._validate_edge(e)
  
  def print_graph(self):
    print("Graph:")
    for v in self._graph.vertices():
      print(str(v), end = " -> ") 
      for e in self.incident_edges(v):
        w = self.opposite(v, e)
        print("(" + str(w) + ",", end = "")
        print(str(e.element()) + ")", end = "")
      print("")
    print("")
    
  def printing_maps(self, printing):
    pass
      
      
      
