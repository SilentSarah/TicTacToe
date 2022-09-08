# Project name: TicTacToe
# Difficulty: low
# Developer: SSarah - Sarah Hicham Meftah

import time
import random

# Level Design, primitive i know.
a_block1 = ["1", "||","1","||","1"]
a_level1 = ["=","=","=","=","=","=","="]
a_block2 = [" ", "||"," ","||"," "]
a_block3 = [" ", "||"," ","||"," "]
#--------------------------------------

#Variables:
cells1 = 3
cells2 = 3
cells3 = 3

def PrintBoard():
    global a_block1
    global a_block2
    global a_block3
    global a_level1
    global a_level2

    print(a_block1[0] + a_block1[1] + a_block1[2] + a_block1[3] + a_block1[4])
    print(a_level1[0] + a_level1[1] + a_level1[2] + a_level1[3] + a_level1[4] + a_level1[5] + a_level1[6])
    print(a_block2[0] + a_block2[1] + a_block2[2] + a_block2[3] + a_block2[4])
    print(a_level1[0] + a_level1[1] + a_level1[2] + a_level1[3] + a_level1[4] + a_level1[5] + a_level1[6])
    print(a_block3[0] + a_block3[1] + a_block3[2] + a_block3[3] + a_block3[4])    

def InitiateGame():
    print("-------------------------------")
    print("|     Welcome to TicTacToe     |")
    print("-------------------------------")

    sgame = input("Press 'n' to start the game\n")
    if sgame == 'n': OnGameProccess()
    else: return InitiateGame()

def OnStateCheck(): # Checks if one of the combinations has been achieved
    global a_block1
    global a_block2
    global a_block3

    if (a_block1[0] == 'x' and a_block1[2] == 'x' and a_block1[4] == 'x') or (a_block2[0] == 'x' and a_block2[2] == 'x' and a_block2[4] == 'x') or (a_block3[0] == 'x' and a_block3[2] == 'x' and a_block3[4] == 'x'):
        print("-------------------------------")
        print("|         player Wins!         |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()
    elif (a_block1[0] == 'o' and a_block1[2] == 'o' and a_block1[4] == 'o') or (a_block2[0] == 'o' and a_block2[2] == 'o' and a_block2[4] == 'o') or (a_block3[0] == 'o' and a_block3[2] == 'o' and a_block3[4] == 'o'):
        print("-------------------------------")
        print("|        Computer Wins!        |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()

    if (a_block1[0] == 'x' and a_block2[0] == 'x' and a_block3[0] == 'x') or (a_block1[2] == 'x' and a_block2[2] == 'x' and a_block3[2] == 'x') or (a_block1[4] == 'x' and a_block2[4] == 'x' and a_block3[4] == 'x'):
        print("-------------------------------")
        print("|         player Wins!         |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()
    elif (a_block1[0] == 'o' and a_block2[0] == 'o' and a_block3[0] == 'o') or (a_block1[2] == 'o' and a_block2[2] == 'o' and a_block3[2] == 'o') or (a_block1[4] == 'o' and a_block2[4] == 'o' and a_block3[4] == 'o'):
        print("-------------------------------")
        print("|        Computer Wins!        |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()

    if (a_block1[0] == 'x' and a_block2[2] == 'x' and a_block3[4] == 'x') or (a_block1[4] == 'x' and a_block2[2] == 'x' and a_block3[0] == 'x'):
        print("-------------------------------")
        print("|         player Wins!         |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()
    elif (a_block1[0] == 'o' and a_block2[2] == 'o' and a_block3[4] == 'o') or (a_block1[4] == 'o' and a_block2[2] == 'o' and a_block3[0] == 'o'):
        print("-------------------------------")
        print("|        Computer Wins!        |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()

    if (a_block1[0] != ' ' and a_block1[2] != ' ' and a_block1[4] != ' ') and (a_block2[0] != ' ' and a_block2[2] != ' ' and a_block2[4] != ' ') and (a_block3[0] != ' ' and a_block3[2] != ' ' and a_block3[4] != ' '):
        print("-------------------------------")
        print("|            DRAW!            |")
        print("-------------------------------")
        PrintBoard()
        time.sleep(2)
        InitiateGame()
    return 0


def BotAction():
    global a_block1
    global a_block2
    global a_block3

    global cells1
    global cells2
    global cells3

    randline = random.randint(0, 2)
    randact = random.randint(0,2)
    i = randact
    match randline:
        case 0:
            if cells1 == 0: return BotAction()
            for i in range(len(a_block1)):
                if a_block1[i] == " ":
                    a_block1[i] = "o"; cells1 -= 1; break
                elif a_block1[i] != " ":
                    continue
                else: return BotAction()
                
        case 1:
            if cells2 == 0: return BotAction()
            for i in range(len(a_block2)):
                if a_block2[i] == " ":
                    a_block2[i] = "o"; cells2 -= 1; break
                elif a_block2[i] != " ":
                    continue
                else: return BotAction()
        case 2:
            if cells3 == 0: return BotAction()
            for i in range(len(a_block3)):
                if a_block3[i] == " ":
                    a_block3[i] = "o"; cells3 -= 1; break
                elif a_block3[i] != " ":
                    continue
                else: return BotAction()
 
    OnStateCheck()
    InGameSetup()


def BotThought():
    global a_block1
    global a_block2
    global a_block3

    print("The Computer is thinking of a move...")
    time.sleep(1)
    BotAction()
    PrintBoard()

def InGameSetup():
    global a_block1
    global a_block2
    global a_block3

    global cells1
    global cells2
    global cells3

    PrintBoard()
    game = input("Type the number corresponding to the empty tile (from 1 to 9)\n")
    if game < '1' or game > '9': return InGameSetup()
    else:
        if game >= '1' and game <= '3':
            if game == '1': 
                if a_block1[0] == " ":
                    a_block1[0] = "x"
                    cells1 -= 1
                else: InGameSetup()
            elif game == '3':
                if a_block1[4] == " ": 
                    a_block1[4] = "x"
                    cells1 -= 1
                else: InGameSetup()
            elif game == '2':
                if a_block1[2] == " ": 
                    a_block1[2] = "x"
                    cells1 -= 1
                else: InGameSetup()
            else: return InGameSetup()

        if game >= '4' and game <= '6':
            line = int(game)
            if game == '4': 
                if a_block2[0] == " ":
                   a_block2[0] = "x"
                   cells2 -= 1
                else: InGameSetup()
            elif game == '6':
                if a_block2[4] == " ":
                    a_block2[4] = "x"
                    cells2 -= 1
                else: InGameSetup()
            elif game == '5':
                if a_block2[2] == " ":
                    a_block2[2] = "x"
                    cells2 -= 1
                else: InGameSetup()
            else: return InGameSetup()

        if game >= '7' and game <= '9':
            line = int(game)
            if game == '7': 
                if a_block3[0] == " ":
                    a_block3[0] = "x"
                    cells3 -= 1
                else: InGameSetup()
            elif game == '9':
                if a_block3[4] == " ":
                    a_block3[4] = "x"
                    cells3 -= 1
                else: InGameSetup()
            elif game == '8':
                if a_block3[2] == " ":
                    a_block3[2] = "x"
                    cells3 -= 1
                else: InGameSetup()
            else: return InGameSetup()
    PrintBoard()
    OnStateCheck()
    BotThought()

def OnGameProccess():
    global a_block1
    global a_block2
    global a_block3

    global cells1
    global cells2
    global cells3

    print("Loading Game")
    time.sleep(1)
    for i in range(len(a_block1)):
        if i % 2 == 0: a_block1[i] = " "
    for i in range(len(a_block2)):
        if i % 2 == 0: a_block2[i] = " "
    for i in range(len(a_block3)):
        if i % 2 == 0: a_block3[i] = " "
    cells1 = 3; cells2 = 3; cells3 = 3
    print("Game has loaded")
    time.sleep(1)
    InGameSetup()
    

InitiateGame()