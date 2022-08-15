import csv


# Game board is a list
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]

# Tells program if game is being played currently
playing = True

winner = None

# Current player X or O
player = "X"

# Sending a record of current position to a csv
def record_board():
    with open("Scoresheet.csv", 'w') as Scoresheet:
        writer = csv.writer(Scoresheet)
        for i in range(len(board)):
            writer.writerow(board[i])

# Displaying the game board stored as list
def show_board():
    print(board[0] + '|' + board[1] + '|'  + board[2])
    print(board[3] + '|' + board[4] + '|'  + board[5])
    print(board[6] + '|' + board[7] + '|'  + board[8])



#Game logic
def play():
    
    #Show game board
    show_board()
  
    #When the game is being played
    while playing == True:
        
        #Adds peices to game as per turn and input
        turn(player)

        #Checking for a winner or a tie
        check()
        
        #Change to next player
        change_player()

        record_board()


    # Declaring winner
    if winner == 'X' or winner == 'O':
        print(winner + " Wins!")
    elif winner == None:
        print("Tie!")



#Checking if the current game board results in a win or a tie
def check():
    check_win()
    check_tie()



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
    
    #Hands turn over to the next player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return



#Placing pieces accoridng to input of each player
def turn(player):
    
    print(player + " 's turn.")
    
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

play()