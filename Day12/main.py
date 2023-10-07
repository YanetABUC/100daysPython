#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def check_answer(guess, answer): 
  if guess == answer:
    print(f"You got it! The answer was {answer}.")
    return True
  elif guess > answer:
    print("Too high.")     
    return False 
  else:
    print("Too low.")
    return False 
  
    
def play_game():
  end_game = False
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  selected_number = random.randint(1, 100)
  attemps = set_difficulty()
  
  while not end_game:
    if attemps > 0:
      print(f"You have {attemps} ramaining to guess the number.")
      guess_number = int(input("Make a guess: "))
      end_game = check_answer(guess_number, selected_number)
      attemps -= 1
      if attemps > 0:
        print("Guess again")
    else:
      end_game = True
      print("You've run out of guesses, you lose.")

play_game()