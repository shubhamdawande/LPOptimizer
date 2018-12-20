# Class for customer details
from Room import Room

class Customer:

    _name = ""
    _persona = ""
    _budget = 0
    _room = None

    def __init__(self, customer_name, customer_persona, customer_budget, customer_room_obj):#, customer_room_area, customer_room_category):
        self._name = customer_name
        self._persona = customer_persona
        self._budget = customer_budget
        self._room = customer_room_obj