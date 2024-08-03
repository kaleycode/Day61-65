from replit import db
import os, time, datetime

def mainMenu():
  menu = input("1: Add an entry\n2: View entries\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()

def add():
  thought = input("Diary entry:\n> ")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = thought
  time.sleep(1)
  os.system("clear")

def view():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.3)
    counter+=1
    if(counter%1==0):
      carryOn = input("See next entry? (yes or no):\n> ")
      print()
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")

while True:
  print("🌟Login System🌟")
  print()
  password = input("Enter Password: \n> ")
  if password == "password":
    print()
    print("Welcome!")
    time.sleep(1)
    os.system("clear")
    mainMenu()
  else:
    print()
    print("Incorrect password")
    time.sleep(1)
    os.system("clear")