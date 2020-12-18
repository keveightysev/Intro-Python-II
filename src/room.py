# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __repr__(self):
        str = f'********************\n{self.name}\n{self.description}\n********************'
        str += f'\nAvailable travel options: \n[{self.get_travel_options()}]\n'
        return str
    
    def get_travel_options(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.s_to is not None:
            exits.append('s')
        if self.e_to is not None:
            exits.append('e')
        if self.w_to is not None:
            exits.append('w')
        return ', '.join(exits)
    
    def get_room(self, direction):
        switch = {
            'n': self.n_to,
            's': self.s_to,
            'e': self.e_to,
            'w': self.w_to,
        }
        return switch.get(direction, None)