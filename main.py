from random import randint
t = [rock, paper, scissors]
computer = t[randint(0,2)]
player = False
while player==False:
  player = input("Rock, Paper, Scissor?").lower()
  if player == computer:
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
      print("You lose!, Computer wins.")
    else:
      print("Congrats! You win.")
  elif player == "paper":
    if computer == "scissor":
      print("You lose!, Computer wins.")
    else:
      print("Congrats! You win.")
  elif player == "scissor":
    if computer == "rock":
      print("You lose!, Computer wins.")
    else:
      print("Congrats! You win.")
  else:
    print("Wrong input! Check spellings.")
  player = False
    computer = t[randint(0,2)]
