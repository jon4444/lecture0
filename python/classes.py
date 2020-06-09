class Point: 
    def __init__(self, x, y):
        self.x = x #accesses the x value of self 
        self.y = y #accesses the y value of self

p = Point(3, 5)
print(p.x)
print(p.y)