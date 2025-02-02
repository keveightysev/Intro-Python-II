# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def travel(self, direction):
        next_room = self.current_room.get_room(direction)
        if next_room is not None:
            self.current_room = next_room
        else:
            print('That direction is not an option')