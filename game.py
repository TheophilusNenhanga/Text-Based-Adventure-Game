"""This file will have the game loop. will reference the other modules as it will not have its own classes"""
from player import Player
import world
from collections import OrderedDict


def play():
    print("""
    				Almus: Cave of Pillars 
    	""")
    world.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())

        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print("""
            Your journey has come to an early end
                     ---GAME OVER---
            """)


def get_player_command():
    return input("Action: ")


def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Print Inventory")
    if isinstance(room, world.TraderTile):
        action_adder(actions, "t", player.trade, "Trade")
    if isinstance(room, world.EnchanterTile):
        action_adder(actions, "e", player.enchant, "Enchant")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    if isinstance(room, world.GeoEnemy) or isinstance(room, world.GeoBoss) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    if isinstance(room, world.HydroEnemy) or isinstance(room, world.HydroBoss) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    if isinstance(room, world.PyroEnemy) or isinstance(room, world.PyroBoss) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    if isinstance(room, world.AeroEnemy) or isinstance(room, world.AeroBoss) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            try:
                if room.enemy.fight() is False:
                    action_adder(actions, "n", player.move_north, "Go North")
            except AttributeError:
                action_adder(actions, "n", player.move_north, "Go North")

        if world.tile_at(room.x, room.y + 1):
            try:
                if room.enemy.fight() is False:
                    action_adder(actions, "s", player.move_south, "Go South")
            except AttributeError:
                action_adder(actions, "s", player.move_south, "Go South")

        if world.tile_at(room.x + 1, room.y):
            try:
                if room.enemy.fight() is False:
                    action_adder(actions, "e", player.move_east, "Go East")
            except AttributeError:
                action_adder(actions, "e", player.move_east, "Go East")

        if world.tile_at(room.x - 1, room.y):
            try:
                if room.enemy.fight() is False:
                    action_adder(actions, "w", player.move_west, "Go West")
            except AttributeError:
                action_adder(actions, "w", player.move_west, "Go West")

    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")

    return actions


def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print(f"{hotkey}: {name}")


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid Action\n")


play()
