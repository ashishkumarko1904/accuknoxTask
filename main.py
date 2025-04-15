class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_dimensions(self):
        return {'length': self.length},{'width': self.width}
    
r1 = Rectangle(10, 5)
r2 = Rectangle(20, 10)
r3 = Rectangle(30, 15)
r4 = Rectangle(40, 20)
for r in [r1, r2, r3, r4]:
    print(r.get_dimensions())
#or we can store the object in  a list and iterate through the list
list_rect = []
list_rect.append(r1)
list_rect.append(r2)    
list_rect.append(r3)
list_rect.append(r4)
for r in list_rect:
    print(r.get_dimensions())