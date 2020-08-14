class Circle (object):
  def __init__ (self,radius,color):
    self.radius=radius;
    self.color=color;
  def add_radius(self,r):
      self.radius=self.radius +r
      return(self.radius)
class Rectangle (object):
  def __init__ (self,color,height,width):
    self.color=color;
    self.height=height;
    self.width=width;

RedCircle=Circle(10,"red")
print("Circle ","\n" ,"Radius:",RedCircle.radius,"\n","Color :",RedCircle.color)
BlueRectangle=Rectangle("Blue",5,8)
print("Rectangle\n Color:",BlueRectangle.color,'\n Height and width :',BlueRectangle.height, ",",BlueRectangle.width)
c1=RedCircle.add_radius(8)
print("Radius of Red Circle After add_radius :",c1)
