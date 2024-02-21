import random
class Postava():

    def __init__ (self, name, attack, defence, health):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
   
    inventory = []

    def fightt(self,enemy):
        print(f"{self.name} attack = {self.attack}")
        print(f"{self.name} defence = {self.attack}")
        a = random.randint(0,2)
        print("======================")
        if a == 0:
            enemy.health -= (self.attack - enemy.defence)
            print(f"{enemy.name} health = {enemy.health}")
        elif a == 1:
            enemy.health -= (self.attack + self.attack - enemy.defence)
            print(f"{enemy.name} health = {enemy.health}")
        else:
            self.health -= (enemy.attack - self.defence)
            print(f"{self.name} health = {self.health}")

class Enemy():
    
    def __init__ (self, attack, defence, health):
        self.name = "Monster"
        self.attack = attack
        self.defence = defence
        self.health = health

    def fightt(self,enemy):
        print(f"{self.name} attack = {self.attack}")
        print(f"{self.name} defence = {self.attack}")
        a = random.randint(0,2)
        print("======================")
        if a == 0:
            enemy.health -= (self.attack - enemy.defence)
            print(f"{enemy.name} health = {enemy.health}")
        elif a == 1:
            enemy.health -= (self.attack + self.attack - enemy.defence)
            print(f"{enemy.name} health = {enemy.health}")
        else:
            self.health -= (enemy.attack - self.defence)
            print(f"{self.name} health = {self.health}")

def map():
    print("Where do you want to go? ")
    try:
        x = int(input("x: "))
        y = int(input("y: "))
    except ValueError:
        map()
    if x == 1 or x == 2:
        if x == 1:
            if y == 1:
                oneone()
            elif y == 2:
                onetwo()
            elif y == 3:
                onethree()
            elif y == 4:
                onefour()
            elif y == 5:
                onefive()
            else:
                print("Wrong coordinates, try again.")
            map()
        elif x == 2:
            if y == 1:
                twoone()
            elif y ==2:
                twotwo()
            elif y ==3:
                twothree()
            elif y ==4:
                twofour()
            elif y == 5:
                twofive()
            else:
                print("Wrong coordinates, try again.")
            map()
    else:
        print("Wrong coordinates, try again.")
        map()

CharacterName = input("What's your name?")
Character = Postava(CharacterName, 10, 15, 70)
Monster = Enemy(15, 20, 100)

def MStats():
    return f"These are the Monster stats - attack = {Monster.attack}, defence = {Monster.defence}, health = {Monster.health }"
def CharStats():
    return (f"These are your stats - attack = {Character.attack},defence = {Character.defence},health = {Character.health }")

def game():
    print(f"Your name is {CharacterName}. When you open your eyes, you find yourself before a small village.")
    print("You see a person. 'Hello good traveler, you are here just in time. Help us stop this monster in our village.' ")
    print("'The moster is quite far away. Its on coordinates [2, 5].Please help us defeat it. But it would be better for you to level up before.'" )
    print(MStats())
    print(CharStats())
    print(f"Your inventory contains - {Postava.inventory}")
    map()

def oneone():
    print("'Hello, I can help you get some medicine but it wont be for free. Get some berries for me.'")
    print("'Berries are in forest on [2,3]'")
    print(f"Your inventory contains - {Postava.inventory}")
    a = input("'Do you have them?'") 
    if a.lower()== "yes":
        if "berries" in Postava.inventory:
            Postava.inventory.remove("berries")
            Character.health += 20
            print(CharStats())
            map()
        else:
            print("'You dont have them. Come back when you have them.'")
            map()
    elif a.lower() == "no":
        print("'If you want medicine, get some berries for me.'")
        map()
    else:
        print("Please answer yes or no.")
        oneone()

def onetwo():
    print("'Hello traveler, I can get you some armor but i need some leather.'")
    a = input("'Do you have it?'") 
    print(Postava.inventory)
    if a.lower() == "yes":
        if "leather" in Postava.inventory:
            Postava.inventory.remove("leather")
            print(f"Your inventory contains - {Postava.inventory}")
            print("'Thank you, here you have an armor.'")
            Character.defence += 15
            print(CharStats())
            map()

        elif "leather" not in Postava.inventory:
            print("'Come back when you have it. Mariane [1,4] should have some.'")
            print("'She also really likes pretty things, make sure to get her something.'")
            map()
    elif a.lower() == "no":
        print("'If you want armor, get some leather for me. Mariane [1,4] should have some.'")
        print("'She also really likes pretty things, make sure to get her something.'")
        map()
    else:
        print("Please answer yes or no.")
        onetwo()

def onethree():
    print ("You see an empty house.")
    a = input("What do you do?")
    if a.lower() == "inspect":
        print("You step into the old house. You don't find any people inside. When you enter the room on the right, you find a chest.")
        b = input("What do you do?")
        if b.lower() == "go away":
            print("You make your way back outside.")
            map()
        elif b.lower() == "inspect":
            print("You open the chest. In there is a knife and a helmet. ")
            Character.attack += 20
            Character.defence += 20
            print(CharStats())
            map()
        else:
            print("Choose one of the available responces in rules.")
            onethree()

    elif a.lower() == "go away":
        print("You go back outside.")
        map()
    else:
        print("Choose one of the available responces in rules.")
        onethree()

def onefour():
    print ("'Hello traveler, welcome to my clothing shop.'")
    a = input("'What do you need?'") 
    if a.lower() == "leather":
        print(f"Your inventory contains - {Postava.inventory}")
        b = input("'Oh, yes certainly. What can you give me in return?'")
        if b.lower()== "pretty stone":
            if "pretty stone" in Postava.inventory:
                print("Oh yes, thank you.")
                Postava.inventory.remove("pretty stone")
                Postava.inventory.append("leather")
                print(f" Your inventory contains - {Postava.inventory}")
            else:
                print("'Please, come back when you have it.'")

        else:
            print("'Come back when you have something for me in return.'")
            map() 

    else:
        print("Choose one of the available responces in rules")
        onefour()

def onefive():
    a = input ("'You find yourself on a meadow, you see cows not far away.'")
    if a.lower() == "inspect":
        print("'You get closer to the cows. They seem frindly.'")
        b = input ("Want to pet them?")
        if b.lower() == "yes":
            print("You pet the cows. They were really sweet and you feel a bit happier.")
            Postava.inventory.append("kindness to cows")
            print(f" Your inventory contains - {Postava.inventory}")
        elif b.lower() == "no":
            print("You turn around and leave.")
            map()
        else:
            print("Choose one of the available responces in rules.")
            onefive()
    elif a.lower() == "go away":
        map()  
    else:
        print("Choose one of the available responces in rules.")
        onefive()

def twoone():
    a = input("'I am a restaurant owner. Would you care for something to eat?'")
    if a.lower() == "yes":
        print("You enter the establishment. The owner seems to like you. They give you a nice warm soup.")
        Character.health += 5
        print(CharStats())
        map()
    elif a.lower() == "no":
        print("You greet the owner a goodbye and go away")
        map()
    else:
        print("Choose one of the available responces in rules.")
        twoone()

def twotwo():
    print ("A nice house. It looks like a friendly family lives there.")
    a = input("What do you do?")
    if a.lower() == "go away":
        print(" You turn around and leave.")
        map()
    elif a.lower() == "inspect":
        if "kindness to cows" not in Postava.inventory:
            print("The family greets you. A small girl starts talking to you. ")
            print("'Hello traveler, yould you be so kind and go pet our cows? They can get quite lonely.'")
            print("'They are at [1,5]. Come back when youre done.'")
        else:
            Postava.inventory.remove("kindness to cows")
            print("'Hello, thank you so much for petting our cows. They can bet a bit lonely sometimes.'")
            print("'Here have some pie we made as a thank you.'")
            Character.health += 20
            print(CharStats())
    else:
        print("Choose one of the available responces in rules")
        twotwo()

def twothree():
    print("You find yourself surrounded by trees. You see the berries in the distance.")
    a = input("What do you do?")
    if a.lower() == "inspect":
        print("You go take the berries.")
        Postava.inventory.append ("berries")
        print(f" Your inventory contains - {Postava.inventory}")
    elif a.lower() == "go away":
        print("You turn around and go away")
        map()
    else:
        print("Choose one of the available responces in rules")
        twothree()

def twofour():
    print ("You see a creek with water")
    a = input("What do you do?")
    if a.lower() == "go away":
        print("You go away")
        map()
    elif a.lower() == "inspect":
        print("You go inspect the creek. The water is clean and there are a lot of pretty stones.")
        b = input("Do you want try to take some?")
        if b.lower() == "yes":
            print("You manage to get a nice looking stone.")
            Postava.inventory.append("pretty stone")
            print(f" Your inventory contains - {Postava.inventory}")
        elif b.lower() == "no":
            print("You dont try to get any stones and just go away.")
            map()
        else:
            print("Choose one of the available responces in rules")
            twofour()
    else:
        print("Choose one of the available responces in rules")
        twofour()

def fight():
    while Character.health > 0 and Monster.health >0:
        Character.fightt(Monster)
        if Monster.health > 0:
            Monster.fightt(Character)
    if Character.health> 0:
        print(f"{CharacterName} has killed the monster. You accomplished your mission. ")
    else:
        print(f"{CharacterName} had been killed by the monster. You lose..." )

def twofive():
    print("This is the lair of the monster.")
    print(CharStats())
    print(MStats())
    a = input ("Do you wish to enter?")
    if a.lower() == "no":
        print(" You go away.")
        map()
    elif a.lower() == "yes":
        print(f"Good luck, {CharacterName}")
        fight()
        exit()

game()