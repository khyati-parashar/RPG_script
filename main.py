from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item
import random


# BLACK MAGIC spells
fire = Spell("Fire", 25, 600, "Black")
thunder = Spell("Thunder", 25, 620, "Black")
blizzard = Spell("Blizzard", 25, 640, "Black")
meteor = Spell("Meteor", 30, 760, "Black")
quake = Spell("Quake", 38, 780, "Black")

# WHITE MAGIC spells
cure = Spell("Cure", 25, 1200, "White")
cura = Spell("Cura", 40, 2000, "White")

# CREATE SOME ITEMS
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotin = Item("Super-Potion", "potion", "Heals 500 HP", 1000)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Mega-Elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


# DECLARATION OF THE PLAYERS
player_spells = [fire, thunder, blizzard, cure, cura]

player_items = [{"item": potion, "qty": 15},
                {"item": hipotion, "qty": 5},
                {"item": superpotin, "qty": 5},
                {"item": elixir, "qty": 5},
                {"item": hielixir, "qty": 2},
                {"item": grenade, "qty": 5}]

# MULTI-PLAYER DECLARATION
player1 = Person("Khyati", 3260, 132, 300, 39, player_spells, player_items)  # hp, mp, atk, df, magic, items
player2 = Person("Himani", 4160, 188, 311, 39, player_spells, player_items)
player3 = Person("Saumya", 3089, 174, 288, 39, player_spells, player_items)

players = [player1, player2, player3]

enemy1 = Person("Witcher", 18200, 701, 525, 25, [], [])
enemy2 = Person("Magus  ", 1250, 130, 560, 325, [], [])
enemy3 = Person("Serpent", 1550, 251, 525, 425, [], [])

enemies = [enemy2, enemy1, enemy3]

running = True
i = 0

print()

print(bcolors.BOLD + bcolors.WARNING + "ENEMIES ATTACKED !!" + bcolors.ENDC)

while running:
    print("================")
    print()
    print(bcolors.BOLD + bcolors.OKBLUE + "Names:                    HP                                               MP" + bcolors.ENDC)
    for player in players:
        player.get_status()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_status()

    for player in players:
        print("\n")
        player.choose_action()
        choice = input("\t" + bcolors.CYAN + "Choose action: " + bcolors.ENDC)
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print()
            print("You attacked " + enemies[enemy].name.replace("  ", "") + " for " + bcolors.BOLD + bcolors.FAIL + str(dmg) + bcolors.ENDC + " points of damage.")

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " is dead now.")
                del enemies[enemy]

            print()

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("\t" + bcolors.CYAN + "Choose magic spell: " + bcolors.ENDC)) - 1

            if magic_choice == -1:
                continue

            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if current_mp < spell.cost:
                print(bcolors.FAIL + "\nYou do not have enough magic points" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "White":
                player.heal(magic_dmg)
                print(bcolors.OKGREEN + "\n" + spell.name + " heals for " + str(magic_dmg) + " health pints." + bcolors.ENDC)
            elif spell.type == "Black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to " + enemies[enemy].name.replace("  ", "") + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " is dead now.")
                del enemies[enemy]

        elif index == 2:
            player.choose_item()
            item_choice = int(input("\t" + bcolors.CYAN + "Choose item: " + bcolors.ENDC)) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]

            if player.items[item_choice]["qty"] == 0:
                print(bcolors.FAIL + "\nNone left......" + bcolors.ENDC)
                continue

            player.items[item_choice]["qty"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print("\n" + bcolors.OKGREEN + item.name + " heals for " + str(item.prop) + " HP" + bcolors.ENDC)
            elif item.type == "elixir":
                if item.name == "Mega-Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp
                print("\n" + bcolors.OKGREEN + item.name + "Fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)
                print("\n" + bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage to " + enemies[enemy].name.replace("  ", "") + bcolors.ENDC)

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name.replace("  ", "") + " is dead now.")
                del enemies[enemy]

    enemy_choice = 1   # this shows that the enemy can just attack as of now as its choice is 1 = attack

    target = random.randrange(0, 3)

    enemy_dmg = enemies[enemy].generate_damage()
    players[target].take_damage(enemy_dmg)
    print(enemies[enemy].name + " has attacked you for " + bcolors.BOLD + bcolors.FAIL + str(enemy_dmg) + bcolors.ENDC + " points of damage.")
    print()

    defeated_enemy = 0
    defeated_player = 0

    for enemy in enemies:
        if enemy.get_hp == 0:
            defeated_enemy += 1


    for player in players:
        if player.get_hp == 0:
            defeated_player += 1

    if defeated_enemy == 2:
        print()
        print(bcolors.OKGREEN + bcolors.BOLD + "YOU WIN!!" + bcolors.ENDC)
        running = False

    elif defeated_player == 2:
        print()
        print(bcolors.FAIL + bcolors.BOLD + "YOUR ENEMIES HAVE DEFEATED YOU!!" + bcolors.ENDC)
        running = False
