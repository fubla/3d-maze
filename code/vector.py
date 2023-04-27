import math


class Vector2D(object): #definition of 2D vectors
    
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.h = 1
        
        
    def __add__(self, other): #vector addition
        
        return Vector2D(self.x+other.x, self.y+other.y)
    
    
    def __sub__(self, other): #vector substraction
        
        return Vector2D(self, self.x-other.x, self.y-other.y)
    
    def __mul__(self, other): #vector multiplication
        
        return Vector2D(self.x*other, self.y*other)
    
    def __div__(self, other): #vector division
        
        return Vector2D(self.x/other, self.y/other)
    
    def dot(self, vector): #dot product
        
        return self.x*vector.x + self.y*vector.y
    
    
class Vector3D(object): #definition of 3D vectors
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.h = 1
        
    def __str__(self):
        return str(self.x)+ ' ' + str(self.y)+ ' '  + str(self.z)
        
    def __add__(self, other):
        
        return Vector3D(self.x+other.x, self.y+other.y, self.z+other.z)
    
    
    def __sub__(self, other):
        
        return Vector3D(self.x-other.x, self.y-other.y, self.z-other.z)
    
    def __mul__(self, other):
        
        return Vector3D(self.x*other, self.y*other, self.z*other)
    
    def __div__(self, other):
        
        return Vector3D(self.x/other, self.y/other, self.z/other)
    
    def dot(self, vector):
        
        return self.x*vector.x + self.y*vector.y + self.z*vector.z
    
    def cross(self, vector): #cross product
        
        x = self.y*vector.z - self.z*vector.y
        y = self.z*vector.x - self.x*vector.z
        z = self.x*vector.y - self.y*vector.x
        
        return Vector3D(x, y, z)
    def get_length(self):
        
        return math.sqrt(self.x*self.x + self.y*self.y + self.z*self.z)