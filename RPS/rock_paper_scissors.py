import random

#print rock paper scissors to the console 
print("Rock ...")
print("Paper ...")
print("Scissors ...")

#prompt the user for input
player1 = input("Player 1, make your move: ")
player2 = ""
#randomly generate a number between 0 and 2 and assign rock, paper or scissors to a number
rand_num = random.randint(0,2)
if rand_num == 0:
    player2 = "rock"
if rand_num == 1:
    player2 = "paper"
if rand_num == 2:
    player2 == "scissors"
print("Computer, make your move: " + str(player2))

#logic to solve the outcome of each choice
if player1 == "rock" and player2 == "scissors":
    print("player1 wins")
elif player1 == "rock" and player2 == "paper":
    print("Computer wins")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins")
elif player1 == "paper" and player2 == "scissors":
    print("player1 wins")
elif player1 == "scissors" and player2 == "rock":
    print("Computer wins")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins")

#if both players pick the same it's a tie
elif player1 == player2:
    print("It's a tie")

#if the input was not rock, paper or scissors, output "Something went wrong"
else:
    print("Something went wrong")