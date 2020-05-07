from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["rope", "coins"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
player = Player("player1", room['outside'])
print(f'{player.current_room}')

while True:
    action = input("\nWhat would you like to do? ").split()
    if action[0] in ("n", "s", "e", "w"):
        if hasattr(player.current_room, f'{action[0]}_to'):
            player.set_location(getattr(player.current_room, f'{action[0]}_to'))
            # player.current_room = getattr(player.current_room, f'{action}_to')
            print(f'Moved to {player.current_room.name}\n\n')
            print(f'{player.current_room.description}')
            print(f'You see {player.current_room.items}')
        else:
            print("You find nothing interesting\n\n")
    # elif action[1] in player.current_room.items:
        # player.getitems(player.current_room.items)
    elif action[0] == "get":
        if action[1] in player.current_room.items:
            # player.getitems(action[1])
            for item in player.current_room.items:
                if item == action[1]:
                    player.getitem(item)
                    player.current_room.items.remove(item)
                    print(f"You see {player.current_room.items}")
    elif action[0] == "drop":
        if action[1] in player.inventory:
            for item in player.inventory:
                if item == action[1]:
                    player.dropitem(item)
                    player.current_room.items.append(item)
                    print(f'You drop {item} on the ground.')
                    print(f"You see {player.current_room.items}")



        
    if action[0] == "q":
        exit()


    # if action == "n":
    #     if player.room.n_to:
    #         print('Moved North')
    #         player.room = player.room.n_to
    #     else:
    #         print('Invalid Movement')
    # if action == "s":
    #     if player.room.s_to:
    #         print('Moved South')
    #         player.room = player.room.s_to
    #     else:
    #         print('Invalid Movement')
    # if action == "e":
    #     if player.room.e_to:
    #         print('Moved East')
    #         player.room = player.room.e_to
    #     else:
    #         print('Invalid Movement')
    # if action == "w":
    #     if player.room.w_to:
    #         print('Moved West')
    #         player.room = player.room.w_to
    #     else:
    #         print('Invalid Movement')


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
