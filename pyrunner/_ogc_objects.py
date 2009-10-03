#this file contains user defined objects.
#objects are the things that inhabit levels.
import ogc

class Box(ogc._ogc_Object):
    def __init__(self):
        ogc._ogc_Object.__init__(self)

    def _ogc_create(self):
        pass

    def _ogc_step(self):
        self.x = (self.x+1) % 120
        self.y = (self.y+1) % 120

    def _ogc_draw(self):
        ogc.graphics.draw_rect((255,128,0), (self.x, self.y, 30,30))

class Cursor(ogc._ogc_Object):
    def __init__(self):
        ogc._ogc_Object.__init__(self)

    def _ogc_create(self):
        pass

    def _ogc_step(self):
        self.x, self.y = ogc.game.get_mouse_pos()

    def _ogc_draw(self):
        ogc.graphics.draw_rect((255,255,255), (self.x, self.y, 3,3))

#list of user defined objects
_ogc_objects = ["Box", "Cursor"]

