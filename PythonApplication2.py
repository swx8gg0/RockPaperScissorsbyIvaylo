import random
rock = 'rock'
paper = 'paper'
scissors = 'scissors'

your_score = 0
computer_score = 0

while True:
 player_move = input("choose [r]ock, [p]aper, [s]cissors: ").strip().lower()

 if player_move == "r":
    player_move = rock
 elif player_move == "p":
    player_move = paper
 elif player_move == "s":
    player_move = scissors
 else:
    print("Invalid input. Try again...")
    continue

 computer = random.choice([rock, paper, scissors])
 print(f"the computer chose: {computer}")

 if player_move == computer:
    print("Draw")
 elif (player_move == rock and computer == scissors) or \
    (player_move == paper and computer == rock) or \
    (player_move == scissors and computer == paper):
    print("You Win!")
    your_score += 1
 else:
    print("You Lose!")
    computer_score = +1
 
  
 play_again = input("Do you want to play again (yes/no): ").strip().lower()
 if play_again == "no":
    print(f"Score: You {your_score}| Computer {computer_score}")
    if your_score < computer_score:
      print("Computer wins the game!")
    elif your_score > computer_score:
        print("You have beaten the computer!")
    elif your_score == computer_score:
        print("You are as smart as the computer!")
    print("thanks for playing!")
    break
