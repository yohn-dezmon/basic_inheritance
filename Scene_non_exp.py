class Scene_(object):

  def __init__(self, solved=False):
    self.name = "wah"
    self.description = "description"
    self.examination = 'nothing'
    self.solved = False
  
  def enter(self):
    print(f"blah blah blah: {self.name}")
