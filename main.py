from classes.game import bcolors, Person
from classes.magic import Spell
from classes.inventory import Item

# BLACK MAGIC spells
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 12, 120, "Black")
blizzard = Spell("Blizzard", 14, 140, "Black")
meteor = Spell("Meteor", 16, 160, "Black")
quake = Spell("Quake", 18, 180, "Black")

# WHITE MAGIC spells
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# CREATE SOME ITEMS
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
superpotin = Item("Super-Potion", "potion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hielixir = Item("Mega-Elixir", "elixir", "Fully restores part'HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)


# DECLARATION OF THE PLAYERS
player_spells = [fire, thunder, blizzard, cure, cura]

player_items = [{"item": potion, "qty": 15},
                {"item": hipotion, "qty": 5},
                {"item": superpotin, "qty": 5},
                {"item": elixir, "qty": 5},
                {"item": hielixir, "qty": 2},
                {"item": grenade, "qty": 5}]

player = Person(460, 65, 60, 39, player_spells, player_items)  # hp, mp, atk, df, magic, items

enemy = Person(1200, 50, 35, 25, [], [])

running = True
i = 0

print()

print(bcolors.BOLD + bcolors.WARNING + "AN ENEMY ATTACKED !!" + bcolors.ENDC)

while running:
    print("================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print()
        print("You attacked enemy for " + bcolors.BOLD + bcolors.FAIL + str(dmg) + bcolors.ENDC + " points of damage.")
        print()

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic spell: ")) - 1

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
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    elif index == 2:
        player.choose_item()
        item_choice = int(input("Choose item: ")) - 1

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
            player.hp = player.maxhp
            player.mp = player.maxmp
            print("\n" + bcolors.OKGREEN + item.name + "Fully restores HP/MP" + bcolors.ENDC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print("\n" + bcolors.FAIL + item.name + " deals " + str(item.prop) + " points of damage." + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy has attacked you for " + bcolors.BOLD + bcolors.FAIL + str(enemy_dmg) + bcolors.ENDC + " points of damage.")
    print()

    print("========================")
    print("Enemy HP: " + bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_maxhp()) + bcolors.ENDC)
    print("\nYour HP: " + bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_maxhp()) + bcolors.ENDC)
    print("\nYour MP: " + bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_maxmp()) + bcolors.ENDC)


    if enemy.get_hp() == 0:
        print()
        print(bcolors.OKGREEN + bcolors.BOLD + "YOU WIN!!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print()
        print(bcolors.FAIL + bcolors.BOLD + "YOUR ENEMY HAS DEFEATED YOU!!" + bcolors.ENDC)
        running = False
