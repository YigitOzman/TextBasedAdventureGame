import random

class Character:
    def __init__(self):
        self.hp = 25
        self.maxhp = 25
        self.dmg = 5
        self.money = 0
        self.pot = 0

class Weapons:
    def __init__(self):
        self.OldSword_dmg = 10
        self.SteelSword_dmg = 20
        self.SteelSword_value = 10
        self.BattleAxe_dmg = 30
        self.BattleAxe_value = 30
        self.Claymore_dmg = 50
        self.Claymore_value = 50
        self.MightyHammer_dmg = 70


class Orc:
    def __init__(self):
        self.hp = 70
        self.dmg = 30

class Dragon:
    def __init__(self):
        self.hp = 100
        self.dmg = 50

class Bandit:
    def __init__(self):
        self.hp = 15
        self.dmg = 3

class WoodElf:
    def __init__(self):    
        self.hp = 50
        self.dmg = 10

class BanditLeader:
    def __init__(self):
        self.hp = 25
        self.dmg = 12

yes = ["Yes", "yes", "Y", "y"]
no = ["No", "no", "N", "n"]
cheat_codes = ("Do you want to activate some cheat codes? Y/N")
cheat_codes2 = ("Do you want to activate another code? Y/N ")
codes = ["Money", "Damage", "Hp"]
Option_A = ["A", "a"]
Option_B = ["B", "b"]
Option_C = ["C", "c"]
Option_D = ["D","d"]
start_screen = ("Do you want to start? Y/N")
Exit = ["Exit","exit"]

Character = Character()
Weapons = Weapons()
MiniBoss3 = Orc()
FinalBoss = Dragon()
Bandit = Bandit()
Critical = WoodElf()
Leader = BanditLeader()


SteelSword = 0
BattleAxe = 0
Claymore = 0
Orc = 0
WoodElf = 0
BanditLeader = 0

def StartScreen():
    print("Do you want to start? Y/N")
    choice = input("> ")
    if choice in yes:
        print(cheat_codes)
        choice = input("> ")
        if choice in yes:
            CheatCodes()
        elif choice in no:
            Game()
        else:
            print("Unknown command. Try Again.")
            StartScreen()
    elif choice in no:
        print("Goodbye.")
        exit()
    else:
        print("Unknown command. Try Again.")
        StartScreen()


def CheatCodes():
    print("Cheat Codes Available: Hp, Damage, Money.\nIf you want to start the game write Exit.\nEnter your code below:")
    choice = input("> ")
    if choice in codes[0]:
            Character.money = Character.money + 1000000
            print(cheat_codes2)
            choice = input("> ")
            if choice in yes:
                CheatCodes()
            elif choice in no:
                Game()
            else:
                print("Unknown command. Try Again.")
                CheatCodes()
    elif choice in codes[1]:
            Character.dmg = Character.dmg + 100
            print(cheat_codes2)
            choice = input("> ")
            if choice in yes:
                CheatCodes()
            elif choice in no:
                Game()
            else:
                print("Unknown command. Try Again.")
                CheatCodes()
    elif choice in codes[2]:
            Character.maxhp = Character.maxhp + 1000000
            Character.hp = Character.hp + 1000000
            print(cheat_codes2)
            choice = input("> ")
            if choice in yes:
                CheatCodes()
            elif choice in no:
                Game()
            else:
                print("Unknown command. Try Again.")
                CheatCodes()
    elif choice in Exit:
        Game()
    else:
        print("Unknown command. Try Again.")
        CheatCodes()



def Game():
    if Character.hp > 0:
        if Character.hp > Character.maxhp:
            Character.hp = Character.maxhp
    print("Hp:", Character.hp)
    print("Damage:" , Character.dmg)
    print("Money:" , Character.money)
    print("You wake up in a cave with a headache and you can't remember anything. But there is a hole that you can barely fit in and you are determined to get out of this place.\nWhat are you going to do?\nA) Look Around.\nB) Go through the hole.")
    choice = input("> ")
    if choice in Option_A:
        print("You look around and see an old chest. Open it? Y/N")
        choice = input("> ")
        if choice in yes:
            chance = random.randint(0,100)
            if chance >= 50:
                print("You managed to open the chest.\nYou have found an old sword, some gold and a health potion. You took them and try to go through the hole.")
                Character.money = Character.money + random.randint(10,25)
                Character.dmg = Character.dmg - Character.dmg + Weapons.OldSword_dmg
                Character.pot = Character.pot + 1
                print("Now you have",Character.money,"gold, your damage is",Character.dmg, "and you have",Character.pot,"health potion.")
            elif chance < 50:
                print("You failed to open the chest and continue your journey.")
        elif choice in no:
            print("You decided not to try open the chest and try to go through the hole.")
        else:
            print("Unknown Command. Try again.")
            Game()
    elif choice in Option_B:
        print("You try to go through the hole.")
    else:
        print("Unknown Command. Try again.")
        Game()
    print("You managed to go through that hole and you are in a larger area of the cave now. You look around and see a bandit by himself. What will you do?\nA) Attack\nB) Sneak Attack\nC) Try to pass him sneakily.")
    choice = input("> ")
    if choice in Option_A:
        AttackBandit()
    elif choice in Option_B:
        SneakAttackBandit()
    elif choice in Option_C:
        SneakyBandit()
    else:
        print("Unknwon Command. Try again.")
        Game()
    print("You dealt with the bandit.\nYou don't see any other bandit they probably left the area and this one stayed here to guard you.\nYou see a weak light. You think that it should be the exit.\nWhat will you do?\nA)Look around.\nB)Go to the light.")
    choice = input("> ")
    if choice in Option_A:
        print("You can't see anything else because its too dark. You decided to follow the light.")
    elif choice in Option_B:
        print("You decided to follow the light.")
    else:
        print("Unknown Command. Try Again.")
        Game()
    print("You finally got out of the cave but it's getting dark. You can see a small town near. You decided to go there.\nAfter a little walk you arrived to the town. It's a really small town but it looks like it has everything you need. You decided to stay in town for a while and see what you can do.\nYou went to the town tavern and told bartender what happened to you.\nHe said you can stay in the tavern tonight for free. You thank him and go to your room to sleep.")
    Character.hp = Character.maxhp
    print("After sleeping you hp is now",Character.hp)
    TownMorning()



def AttackBandit():
    while Bandit.hp > 0 and Character.hp > 0:
        print("What will you do?\nPress A to attack.\nPress B to drink potion.\nPress C to flee.")
        choice = input("> ")
        if choice in Option_A:
            chance = random.randint(0,100)
            if chance >= 50:
                Bandit.hp = Bandit.hp - Character.dmg
                if Bandit.hp < 0:
                    Bandit.hp=0
                print("You managed to hit the bandit.\nBandit hp:", Bandit.hp)
                if Bandit.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - Bandit.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Bandit managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Bandit missed the attack.")
            elif chance < 50:
                print("You missed the bandit.")
                chance = random.randint(0,100)
                if chance > 50:
                    Character.hp=Character.hp - Bandit.dmg
                    if Character.hp < 0:
                        Character.hp=0
                    print("Bandit managed to hit you.\nYour hp: ",Character.hp)
                elif chance < 50:
                    print("Bandit missed the attack.")
        elif choice in Option_B:
            if Character.pot > 0:
                Character.pot = Character.pot -1
                Character.hp = Character.maxhp
                print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
                AttackBandit()
            elif Character.pot == 0:
                print("You don't have a healing potion.")
                AttackBandit()
        elif choice in Option_C:
            print("You look around but dont see any option to run away.")
            AttackBandit()
        else:
            print("Unknown comman. Try again.")
            AttackBandit()
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        elif choice in no:
            print("Goodbye.")
            exit()
        else:
            print("Unknwon Command. Goodbye.")
            exit()
    elif Bandit.hp == 0:
            Character.money = Character.money + random.randint(0,10)
            Character.maxhp = Character.maxhp + 10
            Character.hp = Character.maxhp
            print("You killed the bandit and you feel that you can resist more damage now. New Max Hp:",Character.maxhp,"\nYou looked on his body for loot.\nYou have found some gold.\nYou have ",Character.money,"gold.")


def SneakAttackBandit():
    chance = random.randint(0,100)
    if chance >= 75:
        Bandit.hp = Bandit.hp - (Character.dmg*2)
        if Bandit.hp < 0:
            Bandit.hp =0
        print("You caught bandit by suprise and landed a strike. Bandit hp:", Bandit.hp)
    elif chance < 75:
        Character.hp = Character.hp - (Bandit.dmg*2)
        print("Bandit saw you and landed a counter attack. Your Hp:", Character.hp)
    AttackBandit()


def SneakyBandit():
    chance = random.randint(0,100)
    if chance >= 60:
        print("You managed sneak past the bandit.")
    elif chance < 60:
        Character.hp = Character.hp - Bandit.dmg
        print("Bandit saw you and landed a strike. Your Hp:", Character.hp)
        AttackBandit()



def TownMorning():
    print("What will you do?\nA)Go to Blacksmith.\nB)Go to potion seller.\nC)Go work for some gold.\nD)Check the town hall for bounties.")
    choice = input("> ")
    if choice in Option_A:
        Blacksmith()
    elif choice in Option_B:
        PotionSeller()
    elif choice in Option_C:
        Work()
    elif choice in Option_D:
        Bounty()
    else:
        print("Unknown Command. Try Again.")
        TownMorning()

def Blacksmith():
    global OldSword
    global SteelSword
    global BattleAxe
    global Claymore
    global Orc
    global WoodElf
    global BanditLeader
    if  SteelSword == 0:
        print("You go inside the blacksmith's shop. He welcomes you inside and tells you that he has a Steel Sword that would fit you nicely. It will cost you 10 gold. Are you going to buy it? You have",Character.money,"gold. Y/N")
        choice = input("> ")
        if choice in yes:
            if Character.money >= Weapons.SteelSword_value:
                Character.money = Character.money - Weapons.SteelSword_value
                Character.dmg = Weapons.SteelSword_dmg
                SteelSword = SteelSword + 1
                print("You Bought the Steel Sword. Your damage is now",Character.dmg,"and you have",Character.money,"gold.\nYou go back to the Town Center.")
                TownMorning()
            elif Character.money < Weapons.SteelSword_value:
                print("You don't have enough money.\nYou go back to the town center.")
                TownMorning()
        elif choice in no:
            print("Blacksmith says that if you change your mind his wares are available to you anytime you want.")
            TownMorning()
        else:
            print("Unknwon Command. Try again.")
            Blacksmith()
    elif SteelSword == 1 and BanditLeader == 1 and BattleAxe == 0:
        print("You go inside the blacksmith's shop. He welcomes you inside and says that after slaying that Bandit Leader you are worthy for his latest craft the Battle Axe. It will cost you 30 gold. Are you going to buy it? You have",Character.money,"gold. Y/N")
        choice = input("> ")
        if choice in yes:
            if Character.money >= Weapons.BattleAxe_value:
                Character.money = Character.money - Weapons.BattleAxe_value 
                Character.dmg = Character.dmg - Weapons.SteelSword_dmg + Weapons.BattleAxe_dmg
                BattleAxe = BattleAxe + 1 
                print("You Bought the BattleAxe. Your damage is now",Character.dmg, "and you have",Character.money,"gold.\nYou go back to the Town Center.")
                TownMorning()
            elif Character.money < Weapons.BattleAxe_value:
                print("You don't have enough money.\nYou go back to the town center.")
                TownMorning()
        elif choice in no:
            print("Blacksmith says that if you change your mind his wares are available to you anytime you want.")
            TownMorning()  
        else:
            print("Unknwon Command. Try again.")
            Blacksmith()      
    elif Claymore == 0 and BattleAxe == 1 and WoodElf == 1 :
        print("You go inside the blacksmith's shop. He welcomes you inside and says that you are finally worthy for the claymore. He says it will cost you 50 gold. Are you going to buy it? Y/N")
        choice = input("> ")
        if choice in yes: 
            if Character.money >= Weapons.SteelSword_value:
                Character.money = Character.money - Weapons.SteelSword_value           
                Character.dmg = Weapons.Claymore_dmg
                Claymore = Claymore + 1 
                print("You took the Claymore. Your damage is now",Character.dmg,"\nYou thank him and go back to the Town Center.")
                TownMorning()
            elif Character.money < Weapons.Claymore_value:
                print("You don't have enough money.\nYou go back to the town center.")
                TownMorning()
        elif choice in no:
            print("Blacksmith says that if you change your mind his wares are available to you anytime you want.")
            TownMorning() 
        else:
            print("Unknwon Command. Try again.")
            Blacksmith()   
    elif Claymore == 1:
        print("Blacksmith says that you already have his second best craft and you are not worthy enough to get his best craft.\nYou go back to the town center.")
        TownMorning()    
    else:
        print("The Blacksmith says that he doesn't have anything else to give you right now. You go back to the Town Center.")
        TownMorning()



def PotionSeller():
    print("Potion Seller welcomes you inside and asks if you would like to buy a health potion for 10 gold. Y/N You have",Character.pot,"Health Potions and", Character.money,"gold.")
    choice = input("> ")
    if choice in yes:
        print("Potion Seller asks how many potions would you like to buy.")
        amount = input("> ")
        amount = int(amount)
        if Character.money < amount*10:
            print("You don't have enough money.")
            PotionSeller()
        elif Character.money >= amount:
            Character.money = Character.money - amount*10
            Character.pot = Character.pot +  amount
            print("You now have",Character.pot,"Health Potions and you have",Character.money,"gold.")
            TownMorning()
    elif choice in no:
        print("Potion Seller says that if you change your mind his potions are available to you anytime.\nYou go back to town center.")
        TownMorning()
    else:
        print("Unknwon Command. Try again.")
        PotionSeller()



def Work():
    salary = 0
    salary = salary + random.randint(1,10)
    print("Do you want to work for",salary,"gold? Y/N")
    choice = input("> ")
    if choice in yes:
        Character.money = Character.money + salary
        print("You worked all day and earned",salary,"gold. You now have",Character.money,"gold.")
        Tavern()
    if choice in no:
        print("You decided not to work and returned to town center.")
        TownMorning()
    else:
        print("Unknwon Command. Try again.")
        Work()


def Bounty():
    
    global BanditLeader
    global WoodElf
    global Orc
    
    if BanditLeader == 0:
        print("You see a bounty about a Bandit Leader that has his hideout near the cave you escaped. The bounty is 30 gold. Do you accept? Y/N ")
        choice = input("> ")
        if choice in yes:
            BountyBanditLeader()
        elif choice in no:
            print("You decided to not take that bounty for now. You went back to town center.")
            TownMorning()
        else:
            print("Unknwon Command. Try again.")
            Bounty()
    elif WoodElf == 0:
        print("You see a bounty about a Wood Elf that is harassing people in a road near the village The bounty is 50 gold. Do you accept? Y/N")
        choice = input("> ")
        if choice in yes:
            BountyWoodElf()
        elif choice in no:
            print("You decided to not take that bounty for now. You went back to town center.")
            TownMorning()   
        else:
            print("Unknwon Command. Try again.")
            Bounty()     
    elif Orc == 0:
        print("You see a bounty about an Orc that destroyed a near village and rumors say that he is still in that village. The bounty is 100 gold. Do you accept? Y/N")
        choice = input("> ")
        if choice in yes:
            BountyOrc()
        elif choice in no:
            print("You decided to not take that bounty for now. You went back to town center.")
            TownMorning()
        else:
            print("Unknwon Command. Try again.")
            Bounty()


def BountyBanditLeader():
    print("You took the bounty and went to the location that the bandit leader was last seen. You see the bandit leader. What will you do?\nA)Attack\nB)Sneak Attack")
    choice = input("> ")
    if choice in Option_A:
        AttackPhaseBanditLeader()
    elif choice in Option_B:
        SneakBanditLeader()
    else:
        print("Unknwon Command. Try again.")
        BountyBanditLeader()



def AttackPhaseBanditLeader():
    global BanditLeader
    while Leader.hp > 0 and Character.hp > 0:
        print("What will you do?\nA)Attack\nB)Drink Potion\nC)Escape")
        choice = input("> ")
        if choice in Option_A:
            chance = random.randint(0,100)
            if chance >= 50:
                Leader.hp = Leader.hp - Character.dmg
                if Leader.hp < 0:
                    Leader.hp=0
                print("You managed to hit the bandit leader.\nBandit Leader hp:", Leader.hp)
                if Leader.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - Leader.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Bandit leader managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Bandit leader missed the attack.")
            elif chance < 50:
                print("You missed the bandit leader.")
                chance = random.randint(0,100)
                if chance > 50:
                    Character.hp=Character.hp - Leader.dmg
                    if Character.hp < 0:
                        Character.hp=0
                    print("Bandit leader managed to hit you.\nYour hp: ",Character.hp)
                elif chance < 50:
                    print("Bandit leader missed the attack.")
        elif choice in Option_B:
            if Character.pot > 0:
                Character.pot = Character.pot -1
                Character.hp = Character.maxhp
                print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
                if Leader.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - Leader.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Bandit leader managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Bandit leader missed the attack.")                
                AttackPhaseBanditLeader()
            elif Character.pot == 0:
                print("You don't have a healing potion.")
                if Leader.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - Leader.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Bandit leader managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Bandit leader missed the attack.")                
                AttackPhaseBanditLeader()
        elif choice in Option_C:
            chance =random.randint(0,100)
            if chance < 50:
                print("You look around but dont see any option to run away.")
                if Leader.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - Leader.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Bandit leader managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Bandit leader missed the attack.")
                AttackPhaseBanditLeader()
            elif chance >= 50:
                print("You escaped.")
                Tavern()
        else:
            print("Unknwon Command. Try again.")
            AttackPhaseBanditLeader()
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        elif choice in no:
            print("Goodbye.")
        else:
            print("Unknwon Command. Goodbye.")
            exit()
    elif Leader.hp == 0:
            Character.money = Character.money + random.randint(10,20)
            Character.maxhp = Character.maxhp + 20
            Character.hp = Character.maxhp
            print("You killed the bandit leader and you feel that you can resist more damage now. New Max Hp:",Character.maxhp,"\nYou looked on his body for loot.\nYou have found some gold.\nYou have ",Character.money,"gold.")                    
            Character.money = Character.money + 30
            print("You went back to the town and got the bounty money. You have",Character.money,"gold.")
            BanditLeader = 1
            Tavern()

def SneakBanditLeader():
    chance = random.randint(0,100)
    if chance >= 75:
        Leader.hp = Leader.hp - (Character.dmg*2)
        if Leader.hp < 0:
            Leader.hp =0
        print("You caught bandit leader by suprise and landed a strike. Bandit hp:", Leader.hp)
    elif chance < 75:
        Character.hp = Character.hp - (Leader.dmg*2)
        print("Bandit Leader saw you and landed a counter attack. Your Hp:", Character.hp)
    AttackPhaseBanditLeader()



def BountyWoodElf():
    print("You took the bounty and went to the location that the Wood Elf was last seen. Wood Elf Saw you and he is ready to attack.")
    AttackPhaseWoodElf()


def AttackPhaseWoodElf():
    global WoodElf
    while Critical.hp > 0 and Character.hp > 0:
        print("What will you do?\nA)Attack\nB)Drink Potion\nC)Escape")
        choice = input("> ")
        if choice in Option_A:
            chance = random.randint(0,100)
            if chance >= 50:
                Critical.hp = Critical.hp - Character.dmg
                if Critical.hp < 0:
                    Critical.hp=0
                print("You managed to hit the Wood Elf.\nWood Elf hp:", Critical.hp)
                if Critical.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 80:
                        Character.hp = Character.hp - Critical.dmg * 3
                        if Character.hp < 0:
                            Character.hp=0
                        print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)                    
                    elif chance > 30 and chance <= 80:
                        Character.hp = Character.hp - Critical.dmg
                        if Character.hp < 0:
                            Character.hp = 0
                        print("Wood Elf managed to hit you.\nYour hp: ",Character.hp)
                    elif chance <= 30:
                        print("Wood Elf missed the attack.")
            elif chance < 50:
                print("You missed the Wood Elf.")
                chance = random.randint(0,100)
                if chance > 80:
                    Character.hp = Character.hp - Critical.dmg * 3
                    if Character.hp < 0:
                        Character.hp=0
                    print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)   
                elif chance > 30 and chance <=80:
                    Character.hp=Character.hp - Critical.dmg
                    if Character.hp < 0:
                        Character.hp=0
                    print("Wood Elf managed to hit you.\nYour hp: ",Character.hp)
                elif chance <= 30:
                    print("Wood Elf missed the attack.")
        elif choice in Option_B:
            if Character.pot > 0:
                Character.pot = Character.pot -1
                Character.hp = Character.maxhp
                print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
                if Critical.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 80:
                        Character.hp = Character.hp - Critical.dmg * 3
                        if Character.hp < 0:
                            Character.hp=0
                        print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)                    
                    elif chance > 30 and chance <= 80:
                        Character.hp = Character.hp - Critical.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("WoodElf managed to hit you.\nYour hp: ",Character.hp)
                    elif chance <= 30:
                        print("WoodElf missed the attack.")                
                AttackPhaseWoodElf()
            elif Character.pot == 0:
                print("You don't have a healing potion.")
                if Critical.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 80:
                        Character.hp = Character.hp - Critical.dmg * 3
                        if Character.hp < 0:
                            Character.hp=0
                        print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)                    
                    elif chance > 30 and chance <= 80:
                        Character.hp = Character.hp - Critical.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("WoodElf managed to hit you.\nYour hp: ",Character.hp)
                    elif chance <= 30:
                        print("WoodElf missed the attack.")                
                AttackPhaseWoodElf()                
                if Critical.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 80:
                        Character.hp = Character.hp - Critical.dmg * 3
                        if Character.hp < 0:
                            Character.hp=0
                        print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)                    
                    elif chance > 30 and chance <= 80:
                        Character.hp = Character.hp - Critical.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("WoodElf managed to hit you.\nYour hp: ",Character.hp)
                    elif chance <= 30:
                        print("WoodElf missed the attack.")                
                AttackPhaseWoodElf()
        elif choice in Option_C:
            chance =random.randint(0,100)
            if chance <= 50:
                print("You look around but dont see any option to run away.")
                if Critical.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 80:
                        Character.hp = Character.hp - Critical.dmg*3
                        if Character.hp < 0:
                            Character.hp=0   
                        print("Wood Elf managed to hit you critically.\nYour hp: ",Character.hp)
                    elif chance > 30 and chance <=80:
                        Character.hp = Character.hp - Critical.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Wood Elf managed to hit you.\nYour hp: ",Character.hp)
                    elif chance <= 30:
                        print("Wood Elf missed the attack.")
                AttackPhaseWoodElf()
            elif chance >= 50:
                print("You escaped.")
                Tavern()
        else:
            print("Unknwon Command. Try again.")
            AttackPhaseWoodElf()
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        elif choice in no:
            print("Goodbye.")
            exit()
        else:
            print("Unknwon Command. Goodbye.")
            exit()
    elif Critical.hp == 0:
        Character.money = Character.money + random.randint(10,20)
        Character.maxhp = Character.maxhp + 30
        Character.hp = Character.maxhp
        print("You killed the Wood Elf and you feel that you can resist more damage now. New Max Hp:",Character.maxhp,"\nYou looked on his body for loot.\nYou have found some gold.\nYou have ",Character.money,"gold.")                    
        Character.money = Character.money + 50
        print("You went back to the town and got the bounty money. You have",Character.money,"gold.")
        WoodElf = 1
        Tavern()


def BountyOrc():
    print("You took the bounty and went to the village that the Orc was last seen. The Orc is sitting between the tower of fleshes he created. The Orc sees you and gets up he is ready to attack.")
    AttackPhaseOrc()


def AttackPhaseOrc():
    global Orc
    while MiniBoss3.hp > 0 and Character.hp > 0:
        print("What will you do?\nA)Attack\nB)Drink Potion\nC)Escape")
        choice = input("> ")
        if choice in Option_A:
            chance = random.randint(0,100)
            if chance >= 50:
                Character.hp = Character.hp - MiniBoss3.dmg
                if Character.hp < 0:
                    Character.hp=0
                print("The strike of the Orc was so strong that you could not move.\nYour hp:", Character.hp)
            elif chance < 50:
                print("Orc missed the attack.")
                chance = random.randint(0,100)
                if chance >= 50:
                    MiniBoss3.hp = MiniBoss3.hp - Character.dmg
                    if MiniBoss3.hp < 0:
                        MiniBoss3.hp=0
                    print("You managed to hit The Orc.\nOrc hp: ",MiniBoss3.hp)   
                elif chance < 50:
                    print("You missed the attack.")
        elif choice in Option_B:
            chance = random.randint(0,100)
            if chance >= 50:
                Character.hp = Character.hp - MiniBoss3.dmg
                if Character.hp < 0:
                    Character.hp=0
                print("The strike of the Orc was so strong that you could not move.\nYour hp:", Character.hp)                               
            elif chance < 50:
                if Character.pot > 0:
                    Character.pot = Character.pot -1
                    Character.hp = Character.maxhp
                    print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
                    AttackPhaseOrc()
                elif Character.pot == 0:
                    print("Orc missed the attack.\nYou don't have a healing potion.")
                    AttackPhaseOrc()
        elif choice in Option_C:
            chance =random.randint(0,100)
            if chance >= 50:
                Character.hp = Character.hp - MiniBoss3.dmg
                if Character.hp < 0:
                    Character.hp=0
                print("The strike of the Orc was so strong that you could not move.\nYour hp:", Character.hp)
            elif chance < 50:
                chance = random.randint(0,100)
                if chance >=50:    
                    print("You escaped.")
                    Tavern()
                elif chance < 50:
                    print("Orc missed the attack\nYou look around but don't see any option to run away.")
        else:
            print("Unknwon Command. Try again.")
            AttackPhaseOrc()       
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        if choice in no:
            print("Goodbye.")
            exit()
        else:
            print("Unknown Command. Goodbye.")
            exit()
    elif MiniBoss3.hp == 0:
        Orc = 1
        Character.money = Character.money + random.randint(10,20)
        Character.maxhp = Character.maxhp + 50
        Character.hp = Character.maxhp
        Character.dmg = Weapons.MightyHammer_dmg
        print("You killed the Orc and you feel that you can resist more damage now. New Max Hp:",Character.maxhp,"\nYou looked on his body for loot.\nYou have found some gold.\nYou have ",Character.money,"gold.\nYou went back to the town to get your bounty but when you get near to the town you see a dragon is attacking the town. People beg you to help and the blacksmith gives you his ultimate craft The Mighty Hammer. Your damage is",Character.dmg,"You are ready for your final battle.")                    
        FinalBattlePhase1()    
    
def FinalBattlePhase1():
    while FinalBoss.hp > 0 and Character.hp > 0:
        print("What will you do?\nPress A to attack.\nPress B to drink potion.\nPress C to flee.")
        choice = input("> ")
        if choice in Option_A:
            chance = random.randint(0,100)
            if chance >= 20:
                FinalBoss.hp = FinalBoss.hp - Character.dmg
                if FinalBoss.hp < 0:
                    FinalBoss.hp=0
                print("You managed to hit the Dragon.\nDragon hp:", FinalBoss.hp)
                if FinalBoss.hp > 0:
                    chance = random.randint(0,100)
                    if chance > 50:
                        Character.hp = Character.hp - FinalBoss.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Dragon managed to hit you.\nYour hp: ",Character.hp)
                    elif chance < 50:
                        print("Dragon missed the attack.")
                if Character.hp == 0:
                    print("You Died. Do you wish to try again? Y/N")
                    choice = input("> ")
                    if choice in yes:
                        StartScreen()
                    elif choice in no:
                        print("Goodbye.")
                        exit()
                    else:
                        print("Unknwon Command. Goodbye.")
                        exit()
                elif FinalBoss.hp == 0:
                    print("You slained the dragon. Every single person in the village thanks you and calls you the hero.")
                    EndScreen() 
            elif chance < 20:
                print("You missed the Dragon.")
                chance = random.randint(0,100)
                if chance > 50:
                    Character.hp=Character.hp - FinalBoss.dmg
                    if Character.hp < 0:
                        Character.hp=0
                    print("Dragon managed to hit you.\nYour hp: ",Character.hp)
                elif chance < 50:
                    print("Dragon missed the attack.") 
        elif choice in Option_B:
            if Character.pot > 0:
                Character.pot = Character.pot -1
                Character.hp = Character.maxhp
                print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
                if FinalBoss.hp > 0:
                    chance = random.randint(0,100)
                    if chance >= 50:
                        Character.hp = Character.hp - FinalBoss.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Dragon managed to hit you.\nYour hp: ",Character.hp)                    
                    elif chance < 50:
                        print("Dragon missed the attack.")                
                FinalBattlePhase2()
            elif Character.pot == 0:
                print("You don't have a healing potion.")
                if FinalBoss.hp > 0:
                    chance = random.randint(0,100)
                    if chance >= 50:
                        Character.hp = Character.hp - FinalBoss.dmg
                        if Character.hp < 0:
                            Character.hp=0
                        print("Dragon managed to hit you.\nYour hp: ",Character.hp)                    
                    elif chance < 50:
                        print("Dragon missed the attack.")
        elif choice in Option_C:
            print("You can't run away.")
            FinalBattlePhase2()
        else:
            print("Unknwon Command. Try again.")
            FinalBattlePhase1()
        FinalBattlePhase2()
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        elif choice in no:
            print("Goodbye.")
            exit()
        else:
            print("Unknwon Command. Goodbye.")
            exit()
    elif FinalBoss.hp == 0:
        print("You slained the dragon. Every single person in the village thanks you and calls you the hero.")
        EndScreen()

def FinalBattlePhase2():
    print("Dragon started to fly. Do you want to drink a Health Potion? Y/N")
    choice = input("> ")
    if choice in yes:
        if Character.pot > 0:
            Character.pot = Character.pot -1
            Character.hp = Character.maxhp
            print("You drank a healing potion and successfully restored your hp. Your hp:", Character.hp)
        elif Character.pot == 0:
            print("You don't have any Health Potion.")
    elif choice in no:
        print("You decided to not drink a Health Potion.")
    else:
        print("Unknown Command. Try again.")
        FinalBattlePhase2()
    chance = random.randint(0,100)
    if chance >= 50:
        Character.hp = Character.hp - FinalBoss.dmg
        if Character.hp < 0:
            Character.hp=0
        print("You can't attack because the dragon is flying.\nThe Dragon striked with a fire ball.\nYour hp:", Character.hp)
    elif chance < 50:
        print("You can't attack because the dragon is flying.\nDragon missed the attack.")  
    if Character.hp == 0:
        print("You Died. Do you wish to try again? Y/N")
        choice = input("> ")
        if choice in yes:
            StartScreen()
        if choice in no:
            print("Goodbye.")
            exit()
        else:
            print("Unknwon Command. Try again.")
            exit()
    print("Dragon goes down.")
    FinalBattlePhase1()


def Tavern():
    print("The night falls down and you are tired you decided to go to tavern to get some rest.\nThe Barkeeper welcomes you and says that its 5 gold. Do you accept? Y/N")
    choice = input("> ")
    if choice in yes:
        if Character.money >= 5:
            Character.hp = Character.maxhp
            Character.money = Character.money - 5
            print("You slept in the tavern peacefully your hp is restored. Your Hp is",Character.maxhp,"and you have",Character.money,"gold.")
            TownMorning()
        elif Character.money < 5:
            chance = random.randint(0,100)
            if chance >= 30:
                print("You slept on the streets because you didn't have enough money. You did not restore your hp.")
                TownMorning()
            elif chance < 30:
                Character.money = 0
                print("You slept on the streets because you didn't have enough money. You did not restore your hp and all of your money is stolen by a thief. You have",Character.money,"gold.")
                TownMorning()
    elif choice in no:
        chance = random.randint(0,100)
        if chance >= 30:
            print("You slept on the streets. You did not restore your hp.")
            TownMorning()
        elif chance < 30:
            Character.money = 0
            print("You decided to sleep on the streets. You did not restore your hp and all of your money is stolen by a thief. You have",Character.money,"gold.")
            TownMorning()
    else:
        print("Unknwon Command. Try again.")
        Tavern()

def EndScreen():
    print("Thank you for playing!")
    exit()

StartScreen()