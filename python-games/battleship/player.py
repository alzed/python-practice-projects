class Player:
    def __init__(self):
        pass

    def get_move(self):
        print("Enter the position (space separated):", end="  ")
        coordinates = input()
        pos = tuple(map(lambda p: int(p)-1, coordinates.split()))
        if not len(pos) == 2:
            print("Invalid position")
            return self.get_move()
        return pos
    