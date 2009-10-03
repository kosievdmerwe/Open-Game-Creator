#this file contains user defined objects.
#objects are the things that inhabit levels.
import ogc

class Box(ogc._ogc_Object):
    def __init__(self):
        ogc._ogc_Object.__init__(self)
        print ogc.pygame

    def _ogc_create(self):
        print "I live"

    def _ogc_step(self):
        print "step"

    def _ogc_draw(self):
        print "draw"

#list of user defined objects
_ogc_objects = ["Box"]

