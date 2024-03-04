class Room:
    def __init__(self, description="", north=0, east=0, south=0, west=0):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():

    room_list = []

    # rooms appended to room_list (this was hard)
    room = Room("You are in the Castle foyer. There is a door to the north.", 1, None, None, None)
    room_list.append(room)

    room = Room("You are in the hallway. It is full of portraits of the previous kings.There are doors to the north, east, and west.", 4, 3, 0, 2)
    room_list.append(room)

    room = Room("You are in the library and you see a weird guy reading a necronomicon. There are doors to the south and west.", None, None, 3, 4)
    room_list.append(room)

    room = Room("You are in the dining room but dinner is not done yet.There are doors to the north and east.", 2, 1, None, None)
    room_list.append(room)

    room = Room("You are in the kitchen, the chefs are cooking dinner and it smells nice. There are doors to the south, east ,and west.", None, 5, 1, 2)
    room_list.append(room)

    room = Room("You are in the bedroom. I hope it is yours. There are doors to the south and west.", None, None, 6, 4)
    room_list.append(room)

    room = Room("You are in the bathroom and an armor is holding the butt napkins. There are doors to the north and west.", 5, None, None, 1)
    room_list.append(room)

    # current room
    current_room = 0

    # current room description
    print(room_list[current_room].description)

    # loop
    done = False
    while not done:
        print()
        # user inputs
        action = input("Which path do you choose? (North/East/South/West/Quit): ").upper()

        if action == "N" and room_list[current_room].north is not None:
            next_room = room_list[current_room].north
            current_room = next_room
        elif action == "E" and room_list[current_room].east is not None:
            next_room = room_list[current_room].east
            current_room = next_room
        elif action == "S" and room_list[current_room].south is not None:
            next_room = room_list[current_room].south
            current_room = next_room
        elif action == "W" and room_list[current_room].west is not None:
            next_room = room_list[current_room].west
            current_room = next_room
        elif action == "Q":
            done = True
            print("Thanks for playing!")
            break
        else:
            print("Invalid input or there is no door to that way.")

        # current room description
        print(room_list[current_room].description)


main()
