class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

class Rectangle:
    def __init__(self, twoPoints, color, x, y):
        self.two = twoPoints
        self.color = color
        self.x = x
        self.y = y

    def get_bottom_left(self, x, y):
        self.x = x
        return x

    def get_top_right(self):
        self.y = y
        return y

    def get_color(self, color):
        self.color = color
        return color
    
    def reset_color(self):
        color = input("Enter new color")
        return color

    def get_perimeter(self, x, y):
        perimeter = (self.x + self.y) * 4
        return perimeter

    def get_area(self, x, y):
        area = (self.x * self.y)
        return area

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        Point.move(dx, dy)

    def intersects(self, x, y):
        if (dx == self.x or dy == self.y):
            return True
        else: 
            return False

    def contains(self, x, y):
        # insert
        if (dx <= self.x and dx >= self.y and dy <= self.y and dy >= self.y):
            return True
        else: 
            return False

class Canvas:
    def __init__(self):
        self.self = self

    def add_one_rectangle():
        # insert

    def count_same_color():
        # insert

    def total_perimeter():
        totalPerimeter = get_perimeter(0) + get_perimeter(1) + get_perimeter(2) + get_perimeter(3) + get_perimeter(4)
        return totalPerimeter

    def min_enclosing_rectangle():
        for i in xcoord:
            minCoor = xcoord[i]
        for i in ycoord:
            maxCoor = ycoord[i]

    def common_point():
        for i in xcoord:
            minCoor = xcoord[i]
        for i in ycoord:
            maxCoor = ycoord[i]