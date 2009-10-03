#this file is responsible for running the game

import pygame
import ogc
import _ogc_setup

print "stating up pygame"
pygame.init()

print "starting up sub systems"
ogc.graphics._ogc_init()

print "setting up rooms and objects"
_ogc_setup.setup()


print "starting main room"
ogc.game.set_current_room(ogc._ogc_start_room)

#main game loop
clock = pygame.time.Clock()
i = 0
while True:
    ogc.graphics.clear_screen(ogc.game.current_room.background_color)
    print "frame", i
    i+=1
    #run step event
    for object in ogc.game.get_objects():
        object._ogc_step()

    #run draw event
    for object in ogc.game.get_objects():
        object._ogc_draw()
    clock.tick(ogc.game.current_room.fps)
    ogc.graphics.flip_screen()
    
