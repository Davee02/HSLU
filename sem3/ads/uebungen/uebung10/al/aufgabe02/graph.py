
# HSLU / ICS/AIML : Modul ADS : Algorithmen & Datenstrukturen
# Path   : uebung10/al/aufgabe02
# Version: Fri Nov 17 16:52:43 CET 2023

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
    
    inc_v = self.incident_edges(v)
    if e not in inc_v:
      raise ValueError("edge is not incident to vertex")
    
    (vertice1, vertice2) = self.end_vertices(e)
    return vertice1 if vertice2 == v else vertice2
    
  def are_adjacent(self, v, w):
    self._validate_vertex(v)
    self._validate_vertex(w)
    inc_v = self.incident_edges(v)
    inc_w = self.incident_edges(w)
    
    for edgeFromV in inc_v:
      if edgeFromV in inc_w:
        return True

    return False

  def insert_vertex(self, element):
    v = self._graph.insert_vertex(element)
    return v
  
  def insert_edge(self, v, w, element):
    self._validate_vertex(v)
    self._validate_vertex(w)
    e = self._graph.insert_edge(v, w, element)
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
      
      
