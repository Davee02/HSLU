import functools

class TreePrinterNode:
  
  def __init__(self, bst_node):
    self._node = bst_node
    
  def get_key(self):
    return "(" + str(self._node.get_key()) + "," + self._node.get_value() + ")"
  
  def get_left(self):
    tp_node = None
    if not self._node.get_left().is_external():
      tp_node = TreePrinter.get_node_from_pool(self._node.get_left())
    return tp_node
  
  def get_right(self):
    tp_node = None
    if not self._node.get_right().is_external():
      tp_node = TreePrinter.get_node_from_pool(self._node.get_right())
    return tp_node
  
  
class TreePrinterAcc:
  
  def __init__(self, bst):
    self._bst = bst
    
  def get_root(self):
    tp_node = None
    if self._bst._root != None:
      tp_node = TreePrinter.get_node_from_pool(self._bst._root)
    return tp_node
      
    
    
    

class TreePrinter:
  """ A simple Tree-Displayer for stdout. """
  
  _nodes_pool = dict()
  
  @functools.total_ordering
  class _PrintPos:
    ROOT  = 0
    LEFT  = 1
    RIGHT = 2
    
    def __init__(self, key, x_pos, y_pos, kind):
      self._key = key
      self._x_pos = x_pos
      self._y_pos = y_pos
      self._kind = kind
      
    def __lt__(self, other):
      if self._y_pos < other._y_pos:
        return True
      else:
        return self._x_pos < other._x_pos
      
    def __eq__(self, other):
      return self._x_pos == other._x_pos and self._y_pos == other._y_pos
   
    def __str__(self):
      return str(self._key) + ":" + str(self._x_pos) + "/" + str(self._y_pos)
    
    # End of class _PrintPos
    
  def get_node_from_pool(cls, bst_node):  
    tp_node = TreePrinter._nodes_pool.get(bst_node)
    if tp_node == None:
      tp_node = TreePrinterNode(bst_node)
      TreePrinter._nodes_pool[bst_node] = tp_node
    return tp_node
  get_node_from_pool = classmethod(get_node_from_pool)

  def __init__(self, accessor):
    self._accessor = accessor
    self._step_size = 5
    self._mode = 1
    
  def set_step_size(self, step_size):     
    old_step_size = self._step_size
    self._step_size = step_size
    return old_step_size
 
  def set_mode(self, mode):
    self._mode = mode
  
  def print(self):
    """ Printing the Tree to stdout. """
    print_list = list()
    self.print_tree(self._accessor.get_root(), 0, 0, TreePrinter._PrintPos.ROOT, print_list)
    print_list.sort()
    print("=== Tree: =========================")
    last_y = 0
    current_x = 0
    for pos in print_list:
      if (pos._key == "NULL"):
        continue
      if pos._y_pos > last_y:
        print("\n", end = "")
        current_x = 0
      if self._mode == 1:
        x = pos._x_pos * self._step_size
        while current_x < x:
          print(" ", end = "")
          current_x += 1
        if pos._kind == TreePrinter._PrintPos.RIGHT:
          print("\\", end = "")
          current_x += 1
        print(pos._key, end = "")
        current_x += len(pos._key)
        if pos._kind == TreePrinter._PrintPos.LEFT:
          print("/", end = "")
          current_x += 1
      else:
        x = (pos._x_pos - 1) * self._step_size
        while current_x < x:
          print(" ", end = "")
          current_x += 1
        string = ""
        if pos._kind == TreePrinter._PrintPos.RIGHT:
          string = "\\(" + str(pos._key) + ")"
        else:
          if pos._kind == TreePrinter._PrintPos.LEFT:
            string = pos._key + "/"
          else:
            string = pos._key
        spaces = self._step_size // 2 - len(pos._key) // 2
        while spaces > 0:
          string = " " + string
          spaces -= 1
        while len(string) < self._step_size:
          string = string + " "
        length = (len(str) if self._step_size > len(string) else self._step_size)
        string = string[0, length] 
        print(string)
        current_x += len(string)
      last_y = pos._y_pos
    print("\n=== Tree. =========================")
    
  def print_tree(self, node, current_high, rank, kind, print_list):
    if node == None:
      return rank
    rank = self.print_tree(node.get_left(), current_high+1, rank, TreePrinter._PrintPos.LEFT, print_list)
    print_list.append(TreePrinter._PrintPos(str(node.get_key()), rank, current_high, kind))
    rank += 1
    rank = self.print_tree(node.get_right(), current_high+1, rank, TreePrinter._PrintPos.RIGHT, print_list)
    return rank
    
    