from classes.game import bcolors, Person

magic = [{"name": "Fire", "cost": 10, "damage": 140},
         {"name": "Thunder", "cost": 12, "damage": 150},
         {"name": "Blizzard", "cost": 14, "damage": 160},
         {"name": "Blast", "cost": 20, "damage": 195}]

player = Person(460, 65, 60, 39, magic)  # hp, mp, atk, df, magic
enemy = Person(1200, 50, 35, 25, magic)

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
        print("You attacked enemy for " + bcolors.BOLD + bcolors.FAIL + str(
            dmg) + bcolors.ENDC + " points of damage.\nEnemy HEALTH POINTS: " + bcolors.BOLD + bcolors.FAIL + str(
            enemy.get_hp()) + bcolors.ENDC)
        print()

    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic spell: ")) - 1
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mpcost(magic_choice)

        current_mp = player.get_mp()

        if current_mp < cost:
            print(bcolors.FAIL + "\nYou do not have enough magic points" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy has attacked you for " + bcolors.BOLD + bcolors.FAIL + str(
        enemy_dmg) + bcolors.ENDC + " points of damage.\nYour HEALTH POINTS: " + bcolors.BOLD + bcolors.FAIL + str(
        player.get_hp()) + bcolors.ENDC)
    print()

    if enemy.get_hp() == 0:
        print()
        print(bcolors.OKGREEN + bcolors.BOLD + "YOU WIN!!" + bcolors.ENDC)
        running = False

    elif player.get_hp() == 0:
        print()
        print(bcolors.FAIL + bcolors.BOLD + "YOUR ENEMY HAS DEFEATED YOU!!" + bcolors.ENDC)
        running = False