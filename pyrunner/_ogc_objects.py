import ogc

class Box(ogc._ogc_Object):
    def create(self):
        print "I live"

    def step(self):
        print "step"

    def draw(self):
        print "draw"

_ogc_objects = ["Box"]

