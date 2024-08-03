from replit import db
import datetime, os, time

def add():
  thought = input("Speak your mind!\n> ")
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
    if(counter%4==0):
      carryOn = input("Next thoughts? yes or no:\n> ")
      if(carryOn.lower()=="no"):
        break
  time.sleep(1)
  os.system("clear")
while True:
  print("Day 61: Your Thought Diary")
  print()
  menu = input("1: Add a thought\n2: View Your thoughts\n> ")
  if menu == "1":
    add()
  else:
    view()