import csv
import random
import pandas as pd


# Game board is a list
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]

# Tells program if game is being played currently
playing = True

winner = None

# Current player X or O
player = "X"



#Sends a copy of board to a csv file
def record_board(board):
    row1 = board[0:3]
    row2 = board[3:6]
    row3 = board[6:9]
    return pd.DataFrame([[row1],[row2],[row3]])



#Cleans up output of csv file
def beautify():
    
    #Opens csv file and copies all the data into a list
    with open("Scoresheet.csv", 'r') as file:
    
        f = csv.reader(file)
        loaded_moves = [move for move in f][1:]
    
    #Iterates over the list and adds new lines to seperate boards and counts moves
    with open("Scoresheet.csv", 'w') as file:
        
        num = 0
        
        #i is the row number of file and v is the list of values at the particular row
        for i,v in enumerate(loaded_moves):
            
            if i%3 == 0:
                num += 1
                file.write('\n')
                file.write(f"Move {num}: \n")

            file.write(v[1])
            file.write('\n')      



# Displaying the game board stored as list
def show_board():
    print(board[0] + '|' + board[1] + '|'  + board[2])
    print(board[3] + '|' + board[4] + '|'  + board[5])
    print(board[6] + '|' + board[7] + '|'  + board[8])



#Game logic for player vs player
def playp():
    
    #Show game board
    show_board()

    moves_played = []
  
    #When the game is being played
    while playing == True:
        
        #Adds peices to game as per turn and input
        turn(player, playername1, playername2)

        #Checking for a winner or a tie
        check()
        
        #Change to next player
        change_player()

        moves_played.append(record_board(board))

    # Declaring winner
    if winner == 'X':
        print(playername1 + " Wins!")
    elif winner == 'O':
        print(playername2 + " Wins!")
    elif winner == None:
        print("Tie!")

    pd.concat(moves_played).to_csv("Scoresheet.csv")



#Game Logic for player vs computer
def playc():
        
    #Show game board
    show_board()

    moves_played = []
  
    #When the game is being played
    while playing == True:
        
        #Adds peices to game as per turn and input
        turn(player, playername1, playername2)

        #Checking for a winner or a tie
        check()
        
        #Change to next player
        change_player()


        moves_played.append(record_board(board))

    # Declaring winner
    if winner == 'X':
        print(playername1 + " Wins!")
    elif winner == 'O':
        print(playername2 + " Wins!")
    elif winner == None:
        print("Tie!")

    pd.concat(moves_played).to_csv("Scoresheet.csv")



#Checking if the current game board results in a win or a tie
def check():
    check_win()
    check_tie()



#Returning winner to the AI 
def isWinner(copy, p):

    #Checking for a win across a row
    winning_rows = [copy[6] == p and copy[7] == p and copy[8] == p,
    copy[3] == p and copy[4] == p and copy[5] == p,
    copy[0] == p and copy[1] == p and copy[2] == p]

    #Checking for a win across a column
    winning_columns = [copy[0] == p and copy[3] == p and copy[6] == p,
    copy[1] == p and copy[4] == p and copy[7] == p,
    copy[2] == p and copy[5] == p and copy[8] == p]

    #Checking for a win across a diagonal
    winning_diagonal = [copy[0] == p and copy[4] == p and copy[8] == p,
    copy[2] == p and copy[4] == p and copy[6] == p]

    #Returning a winner
    for i in winning_rows + winning_columns + winning_diagonal:
        if i:
            return i



#Checking if the current board results in a win 
def check_win():
    
    #Setting up a global variable to be used in a function
    global winner
    
    #Check each row of board
    row_winner = checkr()
    
    #Check each column of board
    col_winner = checkc()
    
    #Check each diagonal of board
    dia_winner = checkd()
    
    #Declaring winner based on the row column and diagonal of current board
    if row_winner:
        winner = row_winner
    elif col_winner:
        winner = col_winner
    elif dia_winner:
        winner = dia_winner
    else:
        winner = None
    return



#Check each row of board
def checkr():

    #Setting up a global variable to be used in a function
    global playing
    
    #Checking if a row has the same values in it 
    r1 = board[0] == board[1] == board[2] != " "
    r2 = board[3] == board[4] == board[5] != " "
    r3 = board[6] == board[7] == board[8] != " "

    #If there is a match one of the players has won the game
    if r1 or r2 or r3:
        playing = False
    
    #Return the winning character X or O
    if r1:
        return board[0]
    elif r2:
        return board[3]
    elif r3:
        return board[6]

    return



#Check each column of board
def checkc():    
    
    #Setting up a global variable to be used in a function
    global playing
    
    #Checking if a row has the same values in it 
    c1 = board[0] == board[3] == board[6] != " "
    c2 = board[1] == board[4] == board[7] != " "
    c3 = board[2] == board[5] == board[8] != " "

    #If there is a match one of the players has won the game
    if c1 or c2 or c3:
        playing = False

    #Return the winning character X or O
    if c1:
        return board[0]
    elif c2:
        return board[1]
    elif c3:
        return board[2]

    return



#Check each diagonal of board
def checkd():
        
    #Setting up a global variable to be used in a function
    global playing
    
    #Checking if a row has the same values in it 
    d1 = board[0] == board[4] == board[8] != " "
    d2 = board[2] == board[4] == board[6] != " "

    #If there is a match one of the players has won the game
    if d1 or d2:
        playing = False
    
    #Return the winning character X or O
    if d1:
        return board[0]
    elif d2:
        return board[2]

    return



#Checking if the current board position is a tie
def check_tie():
    
    #Setting up a global variable to be used in a function
    global playing
    
    if " " not in board:
        playing = False
    
    return



#Handing over turn to the next player
def change_player():
    
    #Setting up a global variable to be used in a function
    global player
    
    #Changing of player depending on game mode
    if game_mode in "Pp":
        
        #Hands turn over to the next player
        if player == "X":
            player = "O"
        elif player == "O":
            player = "X"
        return
    
    else: 

        #Hands turn over to the next player
        if player == "X":
            player = "C"
        elif player == "C":
            player = "X"



#Placing pieces accoridng to input of each player
def turn(player, playername1, playername2):
    
    if game_mode in "Pp":
        
        #2 player game
        if player == "X":
            print(playername1 + " 's turn.")
        else:
            print(playername2 + " 's turn.")
        
        place = input("Choose a place 1-9: ")
        
        #We assume that the user input is invalid
        valid = False

        while not valid:
            
            #Checking validity of the users input 
            while place not in ["1","2","3","4","5","6","7","8","9"]:
                place = input("Choose a place 1-9: ")
            
            #Changing the string provided by user to list index
            place = int(place)
            place = place - 1

            #Checking for overwrites on board
            if board[place] == " ":
                valid = True
            else:
                print("Cannot overwrite, choose different place.")

        board[place] = player
        
        show_board() 
    
    else: 

        if game_mode in "Cc":
            
            if player == 'X':
                
                place = input("Choose a place 1-9: ")
                
                #We assume that the user input is invalid
                valid = False

                while not valid:
                    
                    #Checking validity of the users input 
                    while place not in ["1","2","3","4","5","6","7","8","9"]:
                        place = input("Choose a place 1-9: ")
                    
                    #Changing the string provided by user to list index
                    place = int(place)
                    place = place - 1

                    #Checking for overwrites on board
                    if board[place] == " ":
                        valid = True
                    else:
                        print("Cannot overwrite, choose different place.")

                board[place] = player
                
                show_board() 
            
            #Computer selects a place and places O there
            elif player == 'C':

                print(playername2 + " 's turn.")
            
                board[computer_move()] = 'O'
                
                if not check():

                    show_board()
                    
                    if playing == True:
                        print(playername1 + " 's turn.")



#AI that determines the computer's next move
def computer_move():

    #Checkinf for empty spaces in the board
    possibilities = [x for x,pl in enumerate(board) if pl == ' ']

    #Checking which move will be the winning move
    for p in ['O','X']:
        for i in possibilities:
            copy = board[:]
            copy[i] = p
            if isWinner(copy, p):
                move = i
                return move

    #Checking the corners of the board
    corners = []
    for i in possibilities:
        if i in [1,3,7,9]:
            corners.append(i)

    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    if 5 in possibilities:
        move = 5
        return move

    #Checking the edges of the board
    edges = []
    for i in possibilities:
        if i in [2,4,6,8]:
            edges.append(i)

    if len(edges) > 0:
        move = selectRandom(edges)
        return move

    move = random.choice(possibilities)
    return move



#Selecting a place to mark as O if there are many spaces within a row or column
def selectRandom(lst):
    length = len(lst)
    r = random.randrange(0,length)
    return lst[r]



print("Welcome to XO game!!\n")

#Getting game mode from the user
game_mode = input("Do you want to play against computer(C) or against another player(P): ")
while game_mode not in "CcPp":
    game_mode = input("Do you want to play against computer(C) or against another player(P): ")
 

if game_mode == 'P' or game_mode == 'p':

    #Getting player's names to display in the game
    playername1 = input("Name of player playing X: ")
    playername2 = input("Name of player playing O: ")

    playp()

else:

    #Getting player's names to display in the game
    playername1 = input("Name of player playing X: ")
    playername2 = "Computer"
    
    playc()


beautify()