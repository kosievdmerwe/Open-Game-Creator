import pygame

class _ogc_Object:
    def _ogc_create(self):
        pass

    def _ogc_step(self):
        pass

    def _ogc_draw(self):
        pass

class _ogc_Room:
    def __init__(self):
        self.fps = 30
        self.objects = []


class _ogc_Graphics:
    pass

class _ogc_Game:
    def __init__(self):
        self.current_room = None
        

    def set_current_room(self, room):
        self.current_room = room()

graphics = _ogc_Graphics()
game = _ogc_Game()

