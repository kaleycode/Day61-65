class character:
    name = None
    health = None
    magicPoints = None
    def __init__(self, name, health, magicPoints):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints

class player(character):
    lives = 0
    def __init__(self, name, health, magicPoints, lives):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.lives = lives
    def alive(self):
        if self.lives > 0:
            print("Am I alive?: Yes")
        else:
            print("Am I alive: No")
class enemy(character):
    type = None
    strength = None
    def __init__(self, name, health, magicPoints, type, strength):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.type = type
        self.strength = strength
class orc(enemy):
    speed = None
    def __init__(self, name, health, magicPoints, type, strength, speed):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.type = type
        self.strength = strength
        self.speed = speed
class vampire(enemy):
    day = None
    night = None
    def __init__(self, name, health, magicPoints, type, strength, day, night):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints
        self.type = type
        self.strength = strength
        self.day = day
        self.night = night


player1 = player("David", 100, 50, 3)
vampire1 = vampire("Boris", 45, 70, "Vampire", 3, False, "night")
vampire2 = vampire("Rishi", 70, 10, "Vampire", 75, False, "night")
orc1 = orc("Bill", 60, 5, "Orc", 75, 90)
orc2 = orc("Ted", 75, 40, "Orc", 80, 45)
orc3 = orc("Blobby", 35, 40, "Orc", 49, 50)
print(f" {player1.name} \nHealth: {player1.health} \nMagic Points: {player1.magicPoints}")
player1.alive()
print()
print(f" {vampire1.name}\nHealth: {vampire1.health}\nMagic Points: {vampire1.magicPoints}\nType: {vampire1.type}\nStrength: {vampire1.strength}\nday/night: {vampire1.night}")
print()
print(f" {vampire2.name}\nHealth: {vampire2.health}\nMagic Points: {vampire2.magicPoints}\nType: {vampire2.type}\nStrength: {vampire2.strength}\nday/night: {vampire2.night}")
print()
print(f"{orc1.name}\nHealth: {orc1.health}\nSpeed: {orc1.speed}\nMagic Points: {orc1.magicPoints}\nType: {orc1.type}\nStrength: {orc1.strength}")
print()
print(f"{orc2.name}\nHealth: {orc2.health}\nSpeed: {orc2.speed}\nMagic Points: {orc2.magicPoints}\nType: {orc2.type}\nStrength: {orc2.strength}")
print()
print(f"{orc3.name}\nHealth: {orc3.health}\nSpeed: {orc3.speed}\nMagic Points: {orc3.magicPoints}\nType: {orc3.type}\nStrength: {orc3.strength}")