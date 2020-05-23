import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[36m'
    MAGENTA = '\033[35m'
    ORANGE = '\033[33m'


class Person:  # class for the player as well as for the enemy
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp                             # hp = health points
        self.hp = hp
        self.maxmp = mp                             # mp = magic points
        self.mp = mp
        self.atkh = atk + 10                        # atk = attack l/h = low/high
        self.atkl = atk -10
        self.df = df                                # df = defence
        self.magic = magic
        self.items = items
        self.actions = ['Attack', 'Magic', 'Items']
        self.name = name

    def generate_damage(self):     # this generates the damage from the attack
        return random.randrange(self.atkl, self.atkh)


    def take_damage(self, dmg):    # this subtracts the damage from the health points
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):        # this function will heal the player
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):         # gives us the health points that we are left with
        return self.hp

    def get_maxhp(self):       # gives us the max health points that we had
        return self.maxhp

    def get_mp(self):           # gives us the magic points that we are left with
        return self.mp

    def get_maxmp(self):        # gives us the magic points that we initially had
        return self.maxmp

    def reduce_mp(self, cost):   # subtracts the cost from the magic points
        self.mp -= cost

    def choose_target(self, enemies):
        i = 1
        print("\n" + bcolors.FAIL + bcolors.BOLD + "\tTRAGET" + bcolors.ENDC)

        for devil in enemies:
            if devil.get_hp() != 0:
                print("\t\t" + str(i) + ":" + devil.name)
                i += 1
        ans = int(input("\t" + bcolors.CYAN + "Choose your target: " + bcolors.ENDC)) - 1
        return ans

    def choose_action(self):        # allows us to choose what to perform attack or magic spell
        i = 1
        print("\n\t\t" + bcolors.BOLD + bcolors.WARNING + self.name + "'s turn" + bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + "\tACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("\t\t" + str(i) + ":" + item)
            i += 1

    def choose_magic(self):             # allows us to choose which spell or magic to buy and gives their corresponding statistics
        i = 1
        print("\n\t\t" + bcolors.BOLD + bcolors.WARNING + self.name + "'s turn" + bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + "\tMAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("\t\t" + str(i) + ":" + spell.name + "(cost:" + str(spell.cost) + ")")
            i += 1

    def choose_item(self):           # allows us to choose which item to buy and gives their corresponding statistics
        i = 1
        print("\n\t\t" + bcolors.BOLD + bcolors.WARNING + self.name+ "'s turn" + bcolors.ENDC)
        print(bcolors.HEADER + bcolors.BOLD + "\tITEMS" + bcolors.ENDC)
        for item in self.items:
            print("\t\t" + str(i) + " : " + item["item"].name + " -> " + item["item"].description + " (x" + str(item["qty"]) + ")")
            i += 1

    def get_enemy_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 2

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 50:
            hp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 11:
            decreased = 11 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        print("                             __________________________________________________")
        print(self.name + ":        " + current_hp + " |" + bcolors.ORANGE + hp_bar + bcolors.ENDC + "|")

    def get_status(self):
        hp_bar = ""
        bar_ticks = (self.hp / self.maxhp) * 100 / 4

        mp_bar = ""
        mp_ticks = (self.mp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1
        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1
        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.hp) + "/" + str(self.maxhp)
        current_hp = ""

        if len(hp_string) < 9:
            decreased = 9 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp = hp_string

        mp_string = str(self.mp) + "/" + str(self.maxmp)
        current_mp = ""

        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -= 1
            current_mp += mp_string
        else:
            current_mp = mp_string


        print("                          _________________________                        __________")
        print(self.name + ":        " + current_hp + " |" + bcolors.CYAN + hp_bar + bcolors.ENDC + "|              " + current_mp + " |" + bcolors.MAGENTA + mp_bar + bcolors.ENDC + "|")



