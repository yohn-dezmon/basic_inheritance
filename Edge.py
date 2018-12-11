import Scene

class Edge_(Scene.Scene_):
  """ Testing how to import attributes and methods 
      from a Parent class, in this case Scene_
      """
  
  def __init__(self, name, description, examination):
    super(Edge_, self).__init__(name, description, examination)
   
  def enter(self):
    super(Edge_, self).enter()
    
    
