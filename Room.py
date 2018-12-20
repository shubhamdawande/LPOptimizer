## Class for room details

class Room:
    _area = 0
    _type = ""

    def __init__(self, room_area, room_type):
        self._area = room_area
        self._type = room_type