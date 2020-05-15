from classes.game import bcolors, Person
from classes.magic import Spell

# BLACK MAGIC spells
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 12, 120, "Black")
blizzard = Spell("Blizzard", 14, 140, "Black")
meteor = Spell("Meteor", 16, 160, "Black")
quake = Spell("Quake", 18, 180, "Black")

# WHITE MAGIC spells
cure = Spell("Cure", 12, 120, "White")
cura = Spell("Cura", 18, 200, "White")

# DECLARATION OF THE PLAYERS
player = Person(460, 65, 60, 39, [fire, thunder, blizzard, cure, cura])  # hp, mp, atk, df, magic
enemy = Person(1200, 50, 35, 25, [])

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
