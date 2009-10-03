import ogc

class Test(ogc._ogc_Room):
    def __init__(self):
        ogc._ogc_Room.__init__(self)

_ogc_rooms = ["Test"]
_ogc_start_room = "Test"
