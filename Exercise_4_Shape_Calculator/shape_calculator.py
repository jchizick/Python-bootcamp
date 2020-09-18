class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  
  def set_width(self,width):
    self.width = width
  
  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*self.width+2*self.height
    
  def get_diagonal(self):
    return (self.width**2+self.height**2)**.5

  def get_picture(self):
    if self.width>50 or self.height>50:
      return "Too big for picture."
    picture = ''    
    for i in range(self.height):
      picture += '*'*self.width + '\n'
    return picture

  def get_amount_inside(self,shape):
    return (self.width // shape.width)*(self.height//shape.height)
    
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  
  def __init__(self,length):
    self.width = length
    self.height = length
  
  def set_side(self,length):
    self.width = length
    self.height = length
  
  def __str__(self):
    return f"Square(side={self.width})"