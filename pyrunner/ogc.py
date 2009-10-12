#this file contains all the base code for the running of the game

import sys
import pygame

#this object manages graphics
class _ogc_Graphics:
    def _ogc_init(self):
        self.screen = None
        self.render_target = None
        self._ogc_window_size = (1,1)
        self._ogc_resize_window((1,1))

    def _ogc_resize_window(self, size):
        flags = pygame.HWSURFACE | pygame.DOUBLEBUF
        self._ogc_window_size = size
        update_render_target = self.screen == self.render_target
        self.screen = pygame.display.set_mode(size, flags)
        if update_render_target:
            self.render_target = self.screen

    def clear_screen(self, color):
        rect = (0, 0, self._ogc_window_size[0], self._ogc_window_size[1])
        pygame.draw.rect(self.screen, color, rect)
    
    def draw_rect(self, color, rect, border=0):
        pygame.draw.rect(self.screen, color, rect, border)

    def flip_screen(self):
        pygame.display.flip()

#this object manages the game elements
class _ogc_Game:
    def __init__(self):
        self.current_room = None
        self.objects = []
        self._ogc_mouse_pos = (0,0)
        self._ogc_rooms = []

    def _ogc_process_events(self):
        self._ogc_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit()
            #TODO: process other events

    def get_mouse_pos(self):
        return self._ogc_mouse_pos

    def set_mouse_visible(self, visible):
        pygame.mouse.set_visible(visible)

    def register_room(self, room):
        if room not in self._ogc_rooms:
            self._ogc_rooms.append(room)
        
    def set_current_room(self, room):
        if room in self._ogc_rooms:
            self.current_room = room
            graphics._ogc_resize_window(self.current_room._ogc_window_size)
            self.current_room.make_active()

    def create_object(self, object, x, y, owner=None):
        if owner == None:
            owner = self.current_room
        owner.objects.append(object())
        owner.objects[-1].x = x
        owner.objects[-1].y = y
        owner.objects[-1]._ogc_create()

    def get_objects(self):
        return self.current_room.objects + self.objects

    def exit(self):
        sys.exit(0)

#instances of above objects used by user code
graphics = _ogc_Graphics()
game = _ogc_Game()

#base object for all objects
class _ogc_Object:
    def __init__(self):
        self.x = 0
        self.y = 0

    def _ogc_create(self):
        pass

    def _ogc_step(self):
        pass

    def _ogc_draw(self):
        pass

#base object for all rooms
class _ogc_Room:
    def __init__(self):
        self.fps = 30
        self.objects = []
        self._ogc_window_size = (640, 480)
        self.background_color = (255, 0, 0)

    def create_object(self, object, x, y):
        game.create_object(object, x, y, self)

    def reset(self):
        pass
    
    def make_active(self):
        pass

