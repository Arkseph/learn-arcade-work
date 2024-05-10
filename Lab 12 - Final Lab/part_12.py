
import arcade
import random

# all sounds are from freesound.org
cell_door = arcade.load_sound("cell door.wav")
door_locked = arcade.load_sound("doorlocked.mp3")
cave_enter = arcade.load_sound("cave.mp3")
monster_sound = arcade.load_sound("monster1.wav")
monster_defeat = arcade.load_sound("dying monster.wav")
attack_sound = arcade.load_sound("slash.wav")
getting_hit = arcade.load_sound("getting hit.wav")
game_over_sound = arcade.load_sound("game over.wav")
torch_sound = arcade.load_sound("torch.wav")
room5_sound = arcade.load_sound("small room.wav")
room6_sound = arcade.load_sound("torture chamber.mp3")
win_sound = arcade.load_sound("win.wav")


class Room:
    def __init__(self, description="", north=None, east=None, south=None, west=None, up=None, down=None, has_torch=False):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.up = up
        self.down = down
        self.has_torch = has_torch


class Item:
    def __init__(self, room_num, description, short_name):
        self.room_num = room_num
        self.description = description
        self.short_name = short_name


class Player:
    def __init__(self, health):
        self.health = health


class Creature:
    def __init__(self, name, health, damage_range, hit_chance):
        self.name = name
        self.health = health
        self.damage_range = damage_range
        self.hit_chance = hit_chance

    def attack(self):
        return random.randint(self.damage_range[0], self.damage_range[1])

    def is_hit(self):
        return random.random() < self.hit_chance

    print("You wake up in a dungeon cell. Try to escape before the torchlight goes out")


def main():
    room_list = []

    # Rooms
    room = Room("You are in a dimly lit dungeon cell. The iron bars are cold to the touch. There is a faint light coming from the south", south=1)
    arcade.play_sound(cell_door)
    room_list.append(room)

    room = Room("You are in a narrow hallway. There are passages to the north, east, and west.", north=0, east=2, west=3)
    room_list.append(room)

    room = Room("You are in a dusty chamber. Cold wind comes from the windows. There are passages to the east, west and south.", west=1, south=4, east=7)  # has_torch=True
    room_list.append(room)

    room = Room("You are in a small room. The air feels damp. There is a ladder leading up and a passage to the east.", east=1, up=5)
    room_list.append(room)

    room = Room("You are in a dark cave. Water drips from the ceiling. There is a passage to the north and west.", north=2, west=6)
    arcade.play_sound(cave_enter)
    room_list.append(room)

    room = Room("You are in a spacious cavern. There is a ladder going down.", down=3)
    room_list.append(room)

    room = Room("You are in a chamber with many torture instruments. There is a passage to the south and east.", south=8, east=4)
    room_list.append(room)

    room = Room("You are in a obscure dining room. There is a passage on the west.", west=2, has_torch=True)
    room_list.append(room)

    room = Room("You entered what appears to be the entrance to the dungeon. There is a passage to the north and there is a door to the west.", north=6)
    room_list.append(room)

    current_room = 0

    # Items
    item_list = []

    key = Item(1, "There is a rusty key lying on the ground.", "key")
    item_list.append(key)
    key_found = 0

    torch = Item(10, "There is a torch on the wall", "torch")
    item_list.append(torch)

    health = 20

    # Creatures
    monster = Creature("Cave Monster", 20, (3, 6), 0.7)  # monster with 20 health, damage range of 3-6, and 70% hit chance

    # Torchlight meter
    torchlight = 100

    # Game loop
    done = False
    while not done:
        print()
        print(room_list[current_room].description)

        # items in the current room
        for item in item_list:
            if item.room_num == current_room:
                print(item.description)

        # Check and update torchlight
        if room_list[current_room].has_torch:
            torchlight += 40  # Increase torchlight if the room has a torch
            print(f"You found a torch! Torchlight increased. Current torch:{torchlight}")
            arcade.play_sound(torch_sound)
        else:
            torchlight -= 10  # Decrease torchlight when moving to another room
            print(f"Torchlight decreased. Current torch:{torchlight}")

        if torchlight <= 0:
            print("Your torchlight has run out and the monsters devour you. Game Over.")
            arcade.play_sound(game_over_sound)
            action = input("Press q to quit ").lower()
            if action[0] == 'q':
                done = True
                print("Thanks for playing!")
            break

        action = input("What is your command? (North/East/South/West/Up/Down/Get/Drop/Inventory/Quit): ").lower().split(" ", 1)

        if action[0] == 'quit':
            done = True
            print("Thanks for playing!")
        elif action[0] in ["north", "east", "south", "west", "up", "down"]:
            next_room = getattr(room_list[current_room], action[0])
            if next_room is not None:
                current_room = next_room
            else:
                print("You cannot go that way.")
        elif action[0] == "get":
            if len(action) == 2:
                item_name = action[1]
                item_found = False
                for item in item_list:
                    if item.short_name == item_name and item.room_num == current_room:
                        item.room_num = -1
                        key_found = +1
                        print(f"You picked up the {item_name}.")
                        item_found = True
                        break
                if not item_found:
                    print("You don't see that item here.")
            else:
                print("Get what?")
        elif action[0] == "drop":
            if len(action) == 2:
                item_name = action[1]
                item_found = False
                for item in item_list:
                    if item.short_name == item_name and item.room_num == -1:
                        item.room_num = current_room
                        print(f"You dropped the {item_name}.")
                        item_found = True
                        break
                if not item_found:
                    print("You don't have that item.")
            else:
                print("Drop what?")
        elif action[0] == "inventory":
            print("Inventory:")
            for item in item_list:
                if item.room_num == -1:
                    print(item.description)
        else:
            print("Invalid command.")

        # rooms sound
        if current_room == 2:
            arcade.play_sound(room5_sound)
        if current_room == 4:
            arcade.play_sound(cave_enter)
        if current_room == 6:
            arcade.play_sound(room6_sound)

        # win condition
        if current_room == 8 and action[0] == 'west':
            for item in item_list:
                if key_found == 0:
                    print("The door is locked, you need a key.")
                    arcade.play_sound(door_locked)
                    current_room = 8
                    break
            else:
                arcade.play_sound(win_sound)
                print("You used the key to open the door and escaped the dungeon")
                action = input("Press q to quit ").lower()
                if action[0] == 'q':
                    done = True
                    print("Thanks for playing!")
                break

        # Combat with a monster
        if current_room == 5:  # room with a monster
            print()
            print(f"You encounter a {monster.name}!")
            arcade.play_sound(monster_sound)
            while monster.health > 0:
                player_attack = input("Do you want to attack? (Yes/No): ").lower()
                if player_attack == "yes":
                    arcade.play_sound(attack_sound)
                    if monster.is_hit():
                        damage = monster.attack()
                        print(f"You hit the {monster.name} for {damage} damage!")
                        monster.health -= damage
                        if monster.health <= 0:
                            print(f"You defeated the {monster.name}!")
                            arcade.play_sound(monster_defeat)
                            break
                    else:
                        print("You missed!")
                elif player_attack == "no":
                    damaged = monster.attack()
                    arcade.play_sound(getting_hit)
                    health -= damaged
                    print(f"You decide not to attack and you got hit by the {monster.name} for {damaged} damage! You have {health} health left.")
                    if health <= 0:
                        arcade.play_sound(game_over_sound)
                        print(f"You were defeated by the {monster.name}!")
                        action = input("Press q to quit ").lower()
                        if action[0] == 'q':
                            done = True
                            print("Thanks for playing!")
                        break
                else:
                    print("Invalid command.")


if __name__ == "__main__":
    main()
