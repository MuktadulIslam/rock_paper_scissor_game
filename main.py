# Author Name: Mukadul Islam
# Author Email: bsse1215@iit.du.ac.bd
# Date: 02-12-2022
# Game Name: This is a Rock-Paper-Scissor game with sound effect

import constant
import random
import playsound
from playsound import playsound


def game(player, computer):
    if (player == constant.rock and computer == constant.rock
            or player == constant.paper and computer == constant.paper
            or player == constant.scissor and computer == constant.scissor):
        print("Draw")
        playsound("draw-sound.wav")
    elif (player == constant.paper and computer == constant.rock
          or player == constant.rock and computer == constant.scissor
          or player == constant.scissor and computer == constant.paper):
        print("You Win!!!")
        playsound("wining-sound.mp3")


    else:
        print("You Lost :)")
        playsound("losing-sound.wav")


print('For quit, enter "quit"')
while True:
    user = input("Rock(R) / Paper(P) / Scissor(S): ")
    user = user.lower()
    if user == "quit" or user == "exit":
        break;
    value = random.randint(1,3)
    if value == 1:
        comp = constant.rock
    elif value == 2:
        comp = constant.paper
    else:
        comp = constant.scissor
    game(user, comp)
