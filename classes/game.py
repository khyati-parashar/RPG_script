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


class Person:  # class for the player as well as for the enemy
    def __init__(self, hp, mp, atk, df, magic, items):
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

    def choose_action(self):        # allows us to choose what to perform attack or magic spell
        i = 1
        print(bcolors.HEADER + bcolors.BOLD + "ACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("   " + str(i) + ":" + item)
            i += 1

    def choose_magic(self):             # allows us to choose which spell or magic to buy and gives their corresponding statistics
        i = 1
        print("\n" + bcolors.HEADER + bcolors.BOLD + "MAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("   " + str(i) + ":" + spell.name + "(cost:" + str(spell.cost) + ")")
            i += 1

    def choose_item(self):           # allows us to choose which item to buy and gives their corresponding statistics
        i = 1
        print("\n" + bcolors.HEADER + bcolors.BOLD + "ITEMS" + bcolors.ENDC)
        for item in self.items:
            print("   " + str(i) + " : " + item["item"].name + " -> " + item["item"].description + " (x" + str(item["qty"]) + ")")
            i += 1