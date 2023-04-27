'''
Created on 10.3.2013

@author: Niksu
'''

from vector import Vector3D

class Plane(object):
    
    def __init__(self, texture):
        
        self.nodes = []            #points of the plane
        self.texture = texture     #reference number of the color of the plane (name 'texture' misleading)
        self.perpendicular = False #is the plane perpendicular to the camera?
        
    def is_vertical(self):          #is the plane oriented vertically?
        if abs(self.get_normal().y ) < 0.5:
            return True
        else:
            return False
    
    def get_nodes(self):
        
        return self.nodes
    
    def add_node(self, node):       #adds a point to the plane
        
        self.nodes.append(node)
        
    
    def get_texture(self):
        
        return self.texture
        
    def get_cp(self):           #get the center point of the plane
        
        xAvg = float(self.nodes[0].x + self.nodes[2].x) / 2
        yAvg = float(self.nodes[0].y + self.nodes[2].y) / 2
        zAvg = float(self.nodes[0].z + self.nodes[2].z) / 2
        
        cp = Vector3D(xAvg, yAvg, zAvg)
        return cp

    def get_xz(self):           #get all the x,z -points belonging to the plane
        points = []
        dx = self.nodes[2].x - self.nodes[0].x
        if dx < 0:
            sgnx = -1
        else:
            sgnx = 1
        dz = self.nodes[2].z - self.nodes[0].z
        if dz < 0:
            sgnz = -1
        else:
            sgnz = 1
        
        if dz == 0:
            for i in range(int(self.nodes[0].x), int(self.nodes[2].x), sgnx):
                deez = i, self.nodes[0].z
                points.append(deez)
        elif dx == 0:
            for j in range(int(self.nodes[0].z), int(self.nodes[2].z), sgnz):
                deez = self.nodes[0].x, j
                points.append(deez)
        else: 
            return None
        
        return points
    
    def get_normal(self): #get plane normal vector
        
        a = self.nodes[1] - self.nodes[0]
        b = self.nodes[3] - self.nodes[0]
        
        return a.cross(b)