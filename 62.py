from replit import db
import os, time, datetime

def mainMenu():
  menu = input("1: Add an entry\n2: View entries\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()

def add():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def view():
  keys = db.keys()
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"""{key}
    {db[key]}""")
    print()
    opt = input("Next or exit? > ")
    if(opt.lower()[0]=="e"):
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