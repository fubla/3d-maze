'''
Created on 10.3.2013

@author: Niksu
'''
from plane import Plane
from camera import Camera
from vector import Vector3D
from exception import CorruptFileError



class Scene(object):
    
    def __init__(self):
        self.planes = {}    #contains all planes in scene
        self.camera = None 
        self.walls = {}     #contains all points which contain walls
        
    def add_camera(self, location):
        self.camera = Camera(self, location)
        
    def get_camera(self):
        return self.camera
    
    def add_plane(self, plane):
        
        self.planes[plane.get_cp()] = plane 
        xz = plane.get_xz()
        if xz != None:
            for i in range(0, len(xz)): #add wall points to dict
                self.walls[xz[i]] = 1
        
        
        
    def get_plane(self, cp):
        
        return self.planes[cp]
    
    def is_wall(self, location):    #is there a wall in these coordinates?
        loc = location.x, location.z
        if loc in self.walls:
            return True
        return False
 
    def load_scene(self, filename): #loads a scene file and fills data structures with plane and camera data
        
        with open(filename, 'r') as f:
            
            x = y = z = 0
            temp =  f.readline().strip('\r\n')
            if temp != 'scenefile': #there must be descriptor to indicate a scene file
                raise CorruptFileError
            
            temp = f.readline().strip('\r\n')
            temp = temp.split()
            if temp[0] == 'cam':    #cam indicates that camera data follows
                x = float(temp[1])
                y = float(temp[2])
                z = float(temp[3])
                location = Vector3D(x, y, z)
                self.add_camera(location)
            else:
                raise CorruptFileError
            
            while temp:
                temp = f.readline()
                temp = temp.split()
                if temp[0] == 'poly': #indicates that plane data follows
                    if temp[1] == 'tex': #reference number of color(texture) to use
                        texture = int(temp[2])
                    else:
                        texture = None
                    poly = Plane(texture)
                    i = 3
                    while temp[i] != '\n':
                        if temp[i] == 'n':
                            i += 1
                            x = float(temp[i])
                            i += 1
                            y = float(temp[i])
                            i += 1
                            z = float(temp[i])
                            i += 1
                            node = Vector3D(x, y, z)
                            poly.add_node(node)
                        elif temp[i] == 'end': #indicates end of plane data(comments may follow)
                            break
                        else:
                            raise CorruptFileError
                    self.add_plane(poly)
                elif temp[0] == 'endfile': #indicates end of scene flle data
                    break
            
                else:
                    raise CorruptFileError