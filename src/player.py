# Write a class to hold player information, e.g. what room they are in
# currently.
class Player: 
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name}'

    def set_location(self, current_room):
        self.current_room = current_room

    def getitem(self, item):
        self.inventory.append(item)
        print(f'You put {self.inventory} in your inventory.')
    
    def dropitem(self, item):
        self.inventory.remove(item)
        
