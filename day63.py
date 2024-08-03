import test1 as t1


t1.colorText("red", "Hello")
t1.colorText("orange", " Human")
t1.colorText("green", "!")
print()

count = 0
print("If you choose the correct randomized number, you win!")
t1.colorText("yellow", "Let's play!\n")
print()
correctNum = t1.rand()
while True:
  t1.colorText("blue", "Guess a number between 1 and 100! \n")

  t1.colorText("red", "")
  userguess = int(input("> "))
  t1.colorText("purple", "")
  if userguess == correctNum:
    print()
    print("You win!")
    t1.colorText("yellow", "")
    print(f"It took you {count} rounds to win!")
    t1.clear()
    
  elif userguess > correctNum:
    print()
    print("That's too high!")
    count += 1
    print()
    t1.clear()
    continue
  elif userguess < correctNum:
    print()
    print("That's too low!")
    count +=1
    print()
    t1.clear()
    continue
  else:
    print("Nope, pick a number between 1 and 100")
    print()
    count +=1
    continue