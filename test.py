import random

def guess_number():
  randomNumber = random.randint(1, 100)
  chances = 15
  score = (chances / 15) * 100
  
  while chances > 0:
    userinput = input("Guess the number: ")
    if userinput == randomNumber:
      print("Your guess is correct :)")
    else:
      if userinput < randomNumber:
        print("Your guess is lower")
      else:
        print("Your guess is higher")
    chances -= 1

  print("Your score is {}".format(score))

guess_number()
  
