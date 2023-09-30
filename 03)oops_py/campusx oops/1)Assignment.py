'''
Write OOP classes to handle the following scenerios:
1)A user can create and view 2D coordinates.
2)A user can find out the distance between 2 Coordinates.
3)A user can find the distance of a coordinate from origin.
4)A user can check if a point lies on a given line.
5)A user can find the distance between a given 2D point and a given line 

''' 

class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5
        
    def distance_from_origin(self):
        #return (self.x_cod**2 + self.y_cod**2)**o.5
        return self.euclidean_distance(Point(0,0))

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return "{}x +{}y +{} = 0".format(self.A,self.B,self.C)

'''p1=Point(5,5)
p2=Point(10,10)
#print(p1.euclidean_distance(p2))
print(p1.distance_from_origin())'''

li =Line(4,5,6)
print(li)
