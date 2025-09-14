#RPS.py
#Name: Salsabiel Khair Allah
#Date: Sep.14
#Assignment: Lab 3
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

  play_again = "Y"
  while play_again.upper() == "Y": 
    computer = random.choice(list(choices.key()))
    player = input("Select Rock, Paper, or Scissors (R, P, S): ").upper()
    if player not in choices:
      print("Invalid choice. Try again.")
      continue
    print(f"Player chose: {choices[player]}")
    print(f"Computer chose: {choices[computer]}")
    if player == computer:
      print("It's a tie!")
      ties += 1
    elif (player == "R" and computer == "S") or \
    
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  #Prompt the user for their RPS selection
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
