import os
import time
import random


# Default Settings
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False
maxHP_limit = 300
maxATK_limit = 100


# NPC Names
shopkeeper = "Bro"
wizard_name = "Ozz"
boss_name = "Fat Guy"


# Player Status
HP = 100
max_HP = HP
ATK = 3
pot = 1
elix = 0
gold = 0
x = 0
y = 0


# Map
map = [
    ["plains", "plains", "plains", "plains", "forest", "mountain", "cave"],  # Y 0 - 4
    ["forest", "forest", "forest", "forest", "forest", "hills", "mountain"],
    ["forest", "fields", "bridge", "plains", "hills", "forest", "hills"],
    ["plains", "shop", "town", "wizard", "plains", "hills", "mountain"],
    ["plains", "fields", "fields", "plains", "hills", "mountain", "mountain"],
]  # X 0 - 6

y_len = len(map) - 1
x_len = len(map[0]) - 1

biom = {
    "plains": {"t": "PLAINS", "e": True},
    "forest": {"t": "FOREST", "e": True},
    "mountain": {"t": "MOUNTAIN", "e": True},
    "cave": {"t": "CAVE", "e": True},
    "hills": {"t": "HILLS", "e": True},
    "fields": {"t": "FIELDS", "e": True},
    "bridge": {"t": "BRIDGE", "e": False},
    "shop": {"t": "SHOP", "e": False},
    "town": {"t": "TOWN", "e": False},
    "wizard": {"t": "WIZARD", "e": False}
}


# Mobs
e_list = ["Slime", "Goblin", "Spider", "Golem"]

mobs = {
    "Slime": {"HP": 30, "ATK": 3, "gold": 2},
    "Goblin": {"HP": 35, "ATK": 10, "gold": 5},
    "Spider": {"HP": 25, "ATK": 10, "gold": 3},
    "Golem": {"HP": 50, "ATK": 15, "gold": 20},
    boss_name: {"HP": 500, "ATK": 35, "gold": 100},
}


# Clear Screen
def clear():
    os.system("cls")


# Line
def line():
    print("<=>----------------------------------------<=>")


# Save Game
def save():
    list = [
        name,
        str(HP),
        str(ATK),
        str(pot),
        str(elix),
        str(gold),
        str(x),
        str(y),
        str(key),
    ]

    f = open("load.txt", "w")

    for item in list:
        f.write(item + "\n")


# Heal with Potions or Elixir
def heal(amount, heal_type):
    global HP, pot, elix
    if HP < max_HP:
        if heal_type == "pot":
            pot -= 1
        elif heal_type == "elix":
            elix -= 1
        HP += amount
        print(f"{name} used a potion. Healed {amount} HP.")
    elif HP == max_HP:
        print("You can't heal when your HP is full.")


# Battle
def battle():
    global fight, play, run, HP, pot, elix, gold, menu, standing, boss

    if not boss:
        enemy = random.choice(e_list)

    else:
        enemy = boss_name
    
    # Enemy Status Data
    eHP = mobs[enemy]["HP"]
    eHPmax = eHP
    eATK = mobs[enemy]["ATK"]
    eGOLD = mobs[enemy]["gold"]

    # Enemy Name Vowel
    vowelList = ["A", "E", "I", "O", "U"]
    first_letter = enemy[0].upper()
    if enemy != boss_name:
        the = " the "
        if first_letter in vowelList:
            a_an = " an "
        else:
            a_an = " a "
    else:
        a_an = " "
        the = " "

    while fight:
        clear()
        line()
        print(f"{name} encountered{a_an}{enemy}\n")
        print("<=> Enemy Status <=>")
        print(f"[{enemy}] HP {eHP}/{eHPmax} | ATK {eATK}")
        print("<=> Player Status <=>")
        print(f"[{name}] HP {HP}/{max_HP} | ATK {ATK}")
        print(f"Potions: {pot} | Elixir: {elix} | Gold: {gold}")
        line()
        print("[1] Attack")
        if pot > 0:
            print("[2] Use Potion (+30HP)")
        if elix > 0:
            print("[3] Use Elixir (+50HP)")
        line()

        choice = input("> ")

        # Attack
        if choice == "1":
            eHP -= ATK
            print(f"{name} dealt {ATK} damage to{the}{enemy}.")
            if eHP > 0:
                HP -= eATK
                print(f"{enemy} dealt {ATK} damage to {name}.")
                input("> ")

        # Use Potion
        elif choice == "2":
            if pot > 0:
                heal(30, "pot")
                HP -= eATK
                print(f"{enemy} dealt {ATK} damage to {name}.")
            else:
                print("No potions.")
            input("> ")
        
        # Use Elixir
        elif choice == "3":
            if elix > 0:
                heal(50, "elix")
                HP -= eATK
                print(f"{enemy} dealt {ATK} damage to {name}.")
            else:
                print("No elixirs.")
            input("> ")
        
        # Idle
        else:
            standing = True

        # Player Dies
        if HP <= 0:
            print(f"{name} has been vapourised by the {enemy}.")
            fight = False
            play = False
            run = False
            print("GAME OVER")
            input("> ")
        
        # Enemy Dies
        if eHP <=0:
            print(f"{name} destroyed{the}{enemy}.")
            fight = False
            gold += eGOLD
            print(f"You've found {eGOLD} gold.")
            if random.randint(0, 100) < 30:
                pot += 1
                print("You've found a potion")
            if enemy == boss_name:
                print(f"You have slain the {boss_name} and brought peace to humanity.")
                boss = False
                play = False
                run = False
            input("> ")
            clear()


# Shop
def shop():
    global buy, gold, pot, elix, ATK, shopkeeper, maxATK_limit, maxHP_limit

    while buy:
        line()
        print(f"Gold: {gold}\nPotions: {pot}\nElixirs: {elix}\nATK: {ATK}")
        line()
        print("<=> r/itemshop <=>")
        print(f"[1] Buy Potion (+30HP) - 5 Gold")
        print(f"[2] Buy Elixir (MAXHP) - 8 Gold")
        print(f"[3] Upgrade Weapon (+5ATK) - 10 Gold")
        print(f"[4] Buy Herb (+10MAXHP) - 20 Gold")
        print(f"[5] Leave r/itemshop")
        line()
        print(f"{shopkeeper}: Welcome to r/itemshop! We have items you might need on your journey.")

        choice = input("> ")

        if choice == "1":
            clear()
            if gold >= 5:
                pot += 1
                gold -= 5
                print(f"{shopkeeper}: Oh a Health Potion eh? Quite useful for adventures.")
            else:
                print("You don't have enough gold.")
        elif choice == "2":
            clear()
            if gold >= 8:
                elix += 1
                gold -= 8
                print(f"{shopkeeper}: Ah...Elixirs. Crafted by our best alchemist.")
            else:
                print("You don't have enough gold.")
        elif choice == "3":
            clear()
            if gold >= 10:
                if ATK < maxATK_limit:
                    if ATK + 5 >= maxATK_limit:
                        ATK = maxATK_limit
                    else:
                        ATK += 5
                    gold -= 10
                    print(f"{shopkeeper}: I'll upgrade it for ya.")
                    print("*anvil dings* *water vapourises*")
                    print(f"{shopkeeper}: Here ya go mate. That'll be 10 Gold.")
                else:
                    print(f"{shopkeeper}: Your weapon is too strong. It will break if I try to upgrade it further.")
            else:
                print("You don't have enough gold.")
        elif choice == "4":
            clear()
            if gold >= 20:
                if HP < maxHP_limit:
                    if HP + 10 >= maxHP_limit:
                        HP = maxHP_limit
                    else:
                        HP += 10
                    gold -= 20
                    print(f"{shopkeeper}: Here. Eat this.")
                    print("You feel a something flowing inside your body.")
                    print(f"{shopkeeper}: It is a herb that increases your maximum HP.")
                else:
                    print(f"{shopkeeper}: You ate too much herbs. You will die if you keep eating it.")
            else:
                print("You don't have enough gold.")
        elif choice == "5":
            clear()
            buy = False


# Wizard
def wizard():
    global speak, key, wizard_name

    while speak:
        clear()
        line()
        print(f"{wizard_name}: Greetings, {name}.")
        if ATK < 10:
            print(f"{wizard_name}: You are not strong enough to face the dragon. Come back later.")
            key = False
        elif ATK > 10:
            if key:
                print(f"{wizard_name}: You had the key. Slay the dragon and bring peace.")
            else:
                print(f"{wizard_name}: You are strong enough to fight the dragon now. You shall have the key.")
                key = True
                print(f"{name} obtained a key.")
        line()
        print("[1] Leave")
        line()

        choice = input("> ")

        if choice == "1":
            speak = False


# Boss
def cave():
    global boss, key, fight

    while boss:
        line()
        print(f"{name}: There's a sign saying hic sunt dracones.")
        line()
        if key:
            print("[1] Enter the cave")
        print("[2] Leave")
        line()

        choice = input("# ")

        if choice == "1":
            if key:
                fight = True
                battle()
        elif choice == "2":
            boss = False

while run:
    # Menu
    while menu:
        line()
        print("[1] NEW GAME")
        print("[2] LOAD GAME")
        print("[3] RULES")
        print("[4] QUIT GAME")
        line()

        if rules:
            print("RULESSSSSS")
            line()
            rules = False
            choice = ""

        choice = input("> ")

        if choice == "1":  # New Game
            clear()
            line()
            name = input("Greetings...what should I call you?\n> ")
            print(f"Greetings, {name}.")
            menu = False
            play = True

        elif choice == "2":  # Load Game
            clear()
            try:
                # load data from save file
                f = open("load.txt", "r")
                load_list = f.readlines()
                if len(load_list) == 9:
                    name = load_list[0][:-1]
                    HP = int(load_list[1][:-1])
                    ATK = int(load_list[2][:-1])
                    pot = int(load_list[3][:-1])
                    elix = int(load_list[4][:-1])
                    gold = int(load_list[5][:-1])
                    x = int(load_list[6][:-1])
                    y = int(load_list[7][:-1])
                    key = bool(load_list[8][:-1])
                    print(f"Welcome back, {name}.")
                    menu = False
                    play = True
                else:
                    print("Saved game corrupted.")
            except OSError:
                print("No saved game found.")
                input("> ")

        elif choice == "3":  # Rules
            clear()
            rules = True

        elif choice == "4":  # Quit Game
            clear()
            print("Quiting game...")
            time.sleep(3)
            quit()

    # Play
    while play:
        if not standing:
            if biom[map[y][x]]["e"]:
                if random.randint(0, 100) <= 30:
                    fight = True
                    battle()
        if play:
            line()
            # Player Status Info
            print("<=> Player Status <=>")
            print(f"[{name}] HP {HP}/{max_HP} | ATK {ATK}")
            print(f"Potions: {pot} | Elixir: {elix} | Gold: {gold}")
            # Player Location Info
            current_tile = map[y][x]
            name_of_tile = biom[current_tile]["t"]
            enemy_tile = biom[current_tile]["e"]
            print("<=> Player Location <=>")
            print(f"{name_of_tile} #{current_tile}\nEnemy Spawnable: {enemy_tile}")
            print(f"Coordinates: x {x}, y {y}")
            line()

            # Controls
            print("[0] - Save and Quit")
            print("[W] - North    [A] - West\n[S] - South    [D] - East")

            if map[y][x] == "shop" or map[y][x] == "wizard" or map[y][x] == "cave":
                print("[E] ENTER")

            dest = input("> ")

        if dest == "0":
            play = False
            menu = True
            clear()
            save()
            line()
            print("Saving game...")
            print("Quiting to menu...")
            line()
            time.sleep(2)
            clear()
        elif dest == "W":
            clear()
            if y > 0:
                y -= 1
                standing = False
        elif dest == "D":
            clear()
            if x < x_len:
                x += 1
                standing = False
        elif dest == "S":
            clear()
            if y < y_len:
                y += 1
                standing = False
        elif dest == "A":
            clear()
            if x > 0:
                x -= 1
                standing = False
        elif dest == "E":
            if map[y][x] == "shop":
                buy = True
                clear()
                shop()
            if map[y][x] == "wizard":
                speak = True
                clear()
                wizard()
            if map[y][x] == "cave":
                boss = True
                clear()
                cave()
        else: #Idle
            clear()
            standing = True
