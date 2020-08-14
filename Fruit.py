class apple:
   #class attribute
   typeofapple="Fruit"
   #instance attribute
   def __init__(self,color,taste):
    self.color=color;
    self.taste=taste;
#instance of fruit
a1=apple("Red","sweet")
print("Apple is  a  : {}".format(a1.__class__.typeofapple))
print("Color of Apple : {} and Taste of Apple {}".format(a1.color,a1.taste))
