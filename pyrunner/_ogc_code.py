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

class Test(ogc._ogc_Room):
    def __init__(self):
        ogc._ogc_Room.__init__(self)
        self.reset()
    
    def reset(self):
        self.create_object(Box, 0, 0)
        self.create_object(Cursor, 0, 0)

    def make_active(self):
        ogc.game.set_mouse_visible(False)
Test = Test()
ogc.game.register_room(Test)
ogc.game.set_current_room(Test)

