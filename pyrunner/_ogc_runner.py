import pygame
import ogc
import _ogc_setup

print "stating up pygame"
pygame.init()
print "setting up rooms and objects"
_ogc_setup.setup()
ogc.game.set_current_room(ogc._ogc_start_room)
clock = pygame.time.Clock()
while True:
    print "frame"
    clock.tick(ogc.game.current_room.fps)
    

