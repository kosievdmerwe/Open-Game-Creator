#this file is responsible for running the game

import pygame
import ogc
import _ogc_setup

print "stating up pygame"
pygame.init()

print "setting up rooms and objects"
_ogc_setup.setup()

print "starting main room"
ogc.game.set_current_room(ogc._ogc_start_room)

#main game loop
clock = pygame.time.Clock()
while True:
    print "frame"
    #run step event
    for object in ogc.game.current_room.objects + ogc.game.objects:
        object._ogc_step()

    #run draw event
    for object in ogc.game.current_room.objects + ogc.game.objects:
        object._ogc_draw()
    clock.tick(ogc.game.current_room.fps)
    
