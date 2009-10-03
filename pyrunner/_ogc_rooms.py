#this file describes user defined rooms.
#rooms are the levels the game plays off in
import ogc

class Test(ogc._ogc_Room):
    def __init__(self):
        ogc._ogc_Room.__init__(self)
        self.create_object(ogc.Box, 0, 0)

#list of user defined rooms
_ogc_rooms = ["Test"]
#room to start the game from
_ogc_start_room = "Test"
