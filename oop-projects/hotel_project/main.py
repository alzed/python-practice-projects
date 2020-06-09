from hotel import Hotel

print("Enter the name of the hotel:", end="  ")

hotel = Hotel(input())
hotel.list_rooms()

while hotel.has_vacancy():
    occupant_name = input("Enter name of guest to check in:  ")
    room_name = input("Enter the room name:  ")
    retry = True
    while retry:
        if hotel.is_room_exist(room_name):
            if hotel.has_vacancy(room_name):
                hotel.check_in(room_name, occupant_name)
                retry = False
            else:
                room_name = input("Room is full, Try another room  ")
        else:
            room_name = input("Room doesn't exist, Try another room   ")
    hotel.list_rooms()

print(f"All rooms in hotel {hotel.name} are full")
