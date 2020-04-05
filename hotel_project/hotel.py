from room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {
            'seaview': Room('Seaview', 1),
            'cityview': Room('Cityview', 1),
            'elite': Room('Elite', 1)
            }

    def is_room_exist(self, room):
        return room in self.rooms

    def check_in(self, room, occupant):
        if self.rooms[room].available_space() > 0:
            self.rooms[room].add_occupant(occupant)

    def has_vacancy(self, room='all'):
        if room == 'all':
            return not all([room.is_full() for room in self.rooms.values()])
        else:
            return not self.rooms[room].is_full()
            
    def list_rooms(self):
        for room in self.rooms.values():
            if room.available_space() < room.capacity:
                print(room.name, room.occupants)
            else:
                print(room.name, room.available_space())
