#this script is responsible for setting up the game resources as defined 
#by the game files.
import ogc
import _ogc_rooms
import _ogc_objects

#setup() sets up all the game resources from the resource files
def setup():
    #add objects to ogc
    for object in _ogc_objects._ogc_objects:
        setattr(ogc, object, getattr(_ogc_objects, object))

    #add rooms to ogc
    for room in _ogc_rooms._ogc_rooms:
        setattr(ogc, room, getattr(_ogc_rooms, room))
    setattr(ogc, "_ogc_start_room", getattr(_ogc_rooms, _ogc_rooms._ogc_start_room))

