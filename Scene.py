class Scene_(object):
  
  def __init__(self, name, description,
               examination, solved=False):
    self.name = name
    self.description = description
    self.examination = examination
    self.solved = False
  
  def enter(self):
    print(f"blah blah blah: {self.name}")
