# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y
            
    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        if (self.point_1.x-self.point_2.x) != 0:
            self.k1=(self.point_1.y-self.point_2.y) / (self.point_1.x-self.point_2.x) 
        else:
            self.k1 = None
        if (self.point_2.x-self.point_3.x) != 0 :
            self.k2=(self.point_2.y-self.point_3.y) / (self.point_2.x-self.point_3.x)
        else:
            self.k2 = None
        if (self.point_1.x-self.point_3.x) != 0:
            self.k3= (self.point_1.y-self.point_3.y) / (self.point_1.x-self.point_3.x)
        else:
            self.k3 = None
            
        if self.k1 != self.k2 and self.k1 != self.k3 and self.k2 != self.k3:
            pass
        else:
            raise TriangleError('Incorrect input, triangle not created.')
    
        self.edge1 = sqrt((self.point_1.y-self.point_2.y)**2 + (self.point_1.x-self.point_2.x)**2)
        self.edge2 = sqrt((self.point_2.y-self.point_3.y)**2 + (self.point_2.x-self.point_3.x)**2)
        self.edge3 = sqrt((self.point_1.y-self.point_3.y)**2 + (self.point_1.x-self.point_3.x)**2)
        self.perimeter = self.edge1 + self.edge2 + self.edge3
        s = 0.5 * self.perimeter
        self.area = sqrt(s*(s-self.edge1)*(s-self.edge2)*(s-self.edge3))
    




        # Replace pass above with your code
    
    def change_point_or_points(self, *, point_1 = None,point_2 = None, point_3 = None):
        if point_1 == None:
            point_1 = self.point_1
        if point_2 == None:
            point_2 = self.point_2
        if point_3 == None:
            point_3 = self.point_3

        if (point_1.x-point_2.x) != 0:
            k1=(point_1.y-point_2.y) / (point_1.x-point_2.x) 
        else:
            k1 = None
        if (point_2.x-point_3.x) != 0 :
            k2=(point_2.y-point_3.y) / (point_2.x-point_3.x)
        else:
            k2 = None
        if (point_1.x-point_3.x) != 0:
            k3= (point_1.y-point_3.y) / (point_1.x-point_3.x)
        else:
            k3 = None


        
        if k1 != k2 and k1 != k3 and k2 != k3:
            self.point_1 = point_1
            self.point_2= point_2
            self.point_3 = point_3   

            self.edge1 = sqrt((self.point_1.y-self.point_2.y)**2 + (self.point_1.x-self.point_2.x)**2)
            self.edge2 = sqrt((self.point_2.y-self.point_3.y)**2 + (self.point_2.x-self.point_3.x)**2)
            self.edge3 = sqrt((self.point_1.y-self.point_3.y)**2 + (self.point_1.x-self.point_3.x)**2)
            self.perimeter = self.edge1 + self.edge2 + self.edge3
            s = 0.5 * self.perimeter
            self.area = sqrt(s*(s-self.edge1)*(s-self.edge2)*(s-self.edge3))
        else:
            print(TriangleError('Incorrect input, triangle not modified.').message) 
    
        
        


            
            
