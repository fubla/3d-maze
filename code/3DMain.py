from camera import Camera
from exception import *
from plane import Plane
from scene import Scene
from vector import Vector3D
from matrix import Matrix4x4
from pygame.locals import *
import math
import pygame.gfxdraw
import sys


def main():
    
    pygame.display.init()   #initialize pygame
    
    filename = raw_input('Input filename: ')
    scene = Scene()
    
    try:
        scene.load_scene(filename)  #load scene file 
    except CorruptFileError, exc:
        print exc
        sys.exit()
    camera = scene.get_camera()
    
    screen = pygame.display.set_mode((640, 480))    #set window resolution
    running = 1
    minim = 1
    maxim = 100
    def scale(number):  #scales number between 0 and 1
        
        return (number - minim) / (maxim - minim)
        
        
    
    
    while running:
        event = pygame.event.poll() #poll events
        if event.type == pygame.QUIT:
            running = 0
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = 0
            elif event.key == K_UP:
                camera.move_forwards()
            elif event.key == K_DOWN:
                camera.move_backwards()
            elif event.key == K_LEFT:
                camera.turn_left()
            elif event.key == K_RIGHT:
                camera.turn_right()
        screen.fill((0, 0, 0))
        renderOrder = {}
        
        for cp in scene.planes: #loop through all planes
            
            scene.planes[cp].perpendicular = False 
            normal = scene.planes[cp].get_normal() 
            normal_unit = normal/normal.get_length()
            
            dirX = camera.get_dirX()
                                       
            dirZ = camera.get_dirZ()
            
            
            if normal_unit.dot(camera.get_n()) == 1 or normal_unit.dot(camera.get_n()) == -1:   #is plane perpendicular to viewing direction?
                scene.planes[cp].perpendicular = True
            
            if dirX == 1:
                distance = (cp.x - camera.get_location().x) #distance parallel to viewing direction
                distance2 = abs(cp.z-camera.get_location().z) #distance perpendicular to viewing direction 
                
            elif dirX == -1:
                distance = (camera.get_location().x - cp.x)
                distance2 = abs(cp.z-camera.get_location().z)
            elif dirZ == 1: 
                distance = (cp.z - camera.get_location().z)
                distance2 = abs(cp.z-camera.get_location().z)
            elif dirZ == -1:
                distance = (camera.get_location().z - cp.z)
                distance2 = abs(cp.z-camera.get_location().z)
            else:
                return -1
            
            
            
            if distance < 0 and scene.planes[cp].perpendicular: #if plane is behind camera, hide it
                pass
            
            else: 
                
                if not scene.planes[cp].is_vertical():  #move horizontal planes top the end of the rendering queue
                    distance += 100
                
                
                    
                while distance in renderOrder: #if there is already a plane with the same distance, compare perpendicular distances
                    if scene.planes[cp].is_vertical():
                        if renderOrder[distance].is_vertical():
                            if dirX and distance2 < abs(camera.get_location().z - renderOrder[distance].get_cp().z):
                                distance -= 0.01
                            elif dirZ and distance2 < abs(camera.get_location().x - renderOrder[distance].get_cp().x):
                                distance -= 0.001
                            else:
                                distance += 0.02
                    else:
                        distance += 0.01
                
                renderOrder[distance] = scene.planes[cp]
            
        keylist = renderOrder.keys()
        keylist.sort()
        keylist = reversed(keylist)
        for i in keylist:
            toPlot = renderOrder[i]
            
            #camera transforms
            view1x = camera.world_to_camera(toPlot.get_nodes()[0])
            view1 = camera.project_point(view1x)
            view2x = camera.world_to_camera(toPlot.get_nodes()[1])
            view2 = camera.project_point(view2x)
            view3x = camera.world_to_camera(toPlot.get_nodes()[2])
            view3 = camera.project_point(view3x)
            view4x = camera.world_to_camera(toPlot.get_nodes()[3])
            view4 = camera.project_point(view4x)
            
            #define darkness of planes facing the camera
            if not toPlot.perpendicular:
                darkness = 1
            else:
                factor = scale(i)
                darkness = 1 - factor
                
            color1 = int(darkness*130), int(darkness*90), int(darkness*140) 
            color2 = int(darkness*160), int(darkness*120), int(darkness*110)
            color3 = int(darkness*60), int(darkness*60), int(darkness*60) 
            
            pointlist = [(view1.x, view1.y), (view2.x, view2.y), (view3.x, view3.y), (view4.x, view4.y)]
            if toPlot.get_texture() == 0:
                pygame.draw.polygon(screen, color1, pointlist)
            elif toPlot.get_texture() == 1:
                pygame.draw.polygon(screen, color2, pointlist)
            elif toPlot.get_texture() == 2:
                pygame.draw.polygon(screen, color3, pointlist)
                
            pygame.draw.line(screen, (0, 0, 0), (view1.x, view1.y),
                (view2.x, view2.y))
            pygame.draw.line(screen, (0, 0, 0), (view2.x, view2.y),
                (view3.x, view3.y))
            pygame.draw.line(screen, (0, 0, 0), (view3.x, view3.y),
                (view4.x, view4.y))
            pygame.draw.line(screen, (0, 0, 0), (view4.x, view4.y),
                (view1.x, view1.y))
               
        pygame.display.flip()    #update image on screen
        

            
if __name__ == '__main__':
   
    main()