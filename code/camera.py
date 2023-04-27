'''
Created on 10.3.2013

@author: Niksu
'''

from vector import Vector3D
from vector import Vector2D
from matrix import Matrix4x4

class Camera(object):
    
    def __init__(self, scene, location):
        
        self.location = location    #coordinates of camera    
        self.n = Vector3D(1, 0, 0)  #camera direction vector
        self.v = Vector3D(0, 1, 0)  #camera up-vector
        self.zprp = 40        #projection reference point
        self.scene = scene      
    
    
    def get_dirX(self): #get direction vectors x-component
        
        return self.n.x
    def get_dirZ(self): #get direction vectors z-component
        
        return self.n.z
        
    def get_n(self):    #return direction vector
        
        return self.n
    
    def get_v(self):    #return up vector
        return self.v
    
    def get_u(self):    #return u-vector(perpendicular to both n- and v-vectors)
        
        return self.n.cross(self.v)
    
    def set_n(self, newn):  #set n-vector to new value
        
        self.n = newn
        
    def get_heading(self):  #return direction of camera
        
        if self.n.x == 1:
            return 1
        elif self.n.x == -1:
            return 2
        elif self.n.z == 1:
            return 3
        elif self.n.z == -1:
            return 4
        
    
    def get_location(self): #return location of camera
        
        return self.location
    
            
    def move_forwards(self):    #move camera forward
        
        if self.get_n().x == 1: 
            new_location = Vector3D(self.location.x + 2, self.location.y, self.location.z) 
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.x = self.location.x + 2
                return True
        elif self.get_n().x == -1:
            new_location = Vector3D(self.location.x - 2, self.location.y, self.location.z)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.x = self.location.x - 2
                return True
        elif self.get_n().z == 1:
            new_location = Vector3D(self.location.x, self.location.y, self.location.z + 2)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.z = self.location.z + 2
                return True
        elif self.get_n().z == -1:
            new_location = Vector3D(self.location.x, self.location.y, self.location.z - 2)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.z = self.location.z - 2
                return True
        else:
            return False
        
    def move_backwards(self):   #move camera backward
        
        if self.get_n().x == 1:
            new_location = Vector3D(self.location.x - 2, self.location.y, self.location.z)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.x = self.location.x - 2
                return True
        elif self.get_n().x == -1:
            new_location = Vector3D(self.location.x + 2, self.location.y, self.location.z)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.x = self.location.x + 2
                return True
        elif self.get_n().z == 1:
            new_location = Vector3D(self.location.x, self.location.y, self.location.z - 2)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.z = self.location.z - 2
                return True
        elif self.get_n().z == -1:
            new_location = Vector3D(self.location.x, self.location.y, self.location.z + 2)
            if self.scene.is_wall(new_location):
                del new_location
                return False
            else:
                del new_location
                self.location.z = self.location.z + 2
                return True
        else:
            return False
        
    def turn_left(self): #turn view left
        
        if self.get_n().x == 1:
            self.set_n(Vector3D(0, 0, -1))
        elif self.get_n().x == -1:
            self.set_n(Vector3D(0, 0, 1))
        elif self.get_n().z == 1:
            self.set_n(Vector3D(1, 0, 0))
        elif self.get_n().z == -1:
            self.set_n(Vector3D(-1, 0, 0))
        else:
            return False
        
    def turn_right(self):   #turn view right
        
        if self.get_n().x == 1:
            self.set_n(Vector3D(0, 0, 1))
        elif self.get_n().x == -1:
            self.set_n(Vector3D(0, 0, -1))
        elif self.get_n().z == 1:
            self.set_n(Vector3D(-1, 0, 0))
        elif self.get_n().z == -1:
            self.set_n(Vector3D(1, 0, 0))
        else:
            return False
        
    def world_to_camera(self, Q):   #convert world coordinates to image space
        
        
        R = Matrix4x4(self.get_u().x, -self.get_u().y, self.get_u().z, 0, 
                      self.get_v().x, -self.get_v().y, self.get_v().z, 0,
                      self.get_n().x, -self.get_n().y, self.get_n().z, 0,
                      0,              0,              0,              1)
        
        T = Matrix4x4(1,    0,     0,     -self.get_location().x,
                      0,    1,     0,     -self.get_location().y,
                      0,    0,     1,     -self.get_location().z,
                      0,    0,     0,               1)
        
        
        Qv = R*T*Q
        return Qv 
    
    def project_point(self, Q): #project points in image space to screen space
        
        Q.z -= 40 #takes the camera closer to the scene
        if Q.z < -39.9: #prevents strange artifacts which appear from Q.z nearing perspection reference point
            Q.z = -39.9
              
        xp = Q.x*abs(1/(1 - float(Q.z/(-self.zprp))))*10 +320   #projection from image space to screen space
        yp = Q.y*abs(1/(1 - float(Q.z/(-self.zprp))))*10 +240
        
        return Vector2D(xp, yp)