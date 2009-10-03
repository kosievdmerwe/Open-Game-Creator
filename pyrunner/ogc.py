#this file contains all the base code for the running of the game
import pygame

#this object manages graphics
class _ogc_Graphics:
    pass

#this object manages the game elements
class _ogc_Game:
    def __init__(self):
        self.current_room = None
        self.objects = []
        
    def set_current_room(self, room):
        self.current_room = room()

    def create_object(self, object, x, y, owner=None):
        if owner == None:
            owner = self.current_room
        owner.objects.append(object())
        owner.objects[-1].x = x
        owner.objects[-1].y = y
        owner.objects[-1]._ogc_create()

#instances of above objects used by user code
graphics = _ogc_Graphics()
game = _ogc_Game()

#base object for all objects
class _ogc_Object:
    def __init__(self):
        self.x = 0
        self.y = 0

    def _ogc_create(self):
        print "parent create"

    def _ogc_step(self):
        pass

    def _ogc_draw(self):
        pass

#base object for all rooms
class _ogc_Room:
    def __init__(self):
        self.fps = 30
        self.objects = []

    def create_object(self, object, x, y):
        game.create_object(object, x, y, self)

