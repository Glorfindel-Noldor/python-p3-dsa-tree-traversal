
class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):

    grabbed = [self.root]

    while grabbed:
      currently_grabbing = grabbed.pop()
      if currently_grabbing.get('id') == id:
          return currently_grabbing
      
      grabbed.extend(currently_grabbing.get('children', [] )) 
    
    return None
