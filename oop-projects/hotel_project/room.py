class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.occupants = []

    def is_full(self):
        return len(self.occupants) >= self.capacity

    def available_space(self):
        return self.capacity - len(self.occupants)

    def add_occupant(self, occupant):
        self.occupants.append(occupant)
        return True
