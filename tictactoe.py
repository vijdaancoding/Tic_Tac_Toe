import turtle 

wn = turtle.Screen()
wn.title("Tic Tac Toe")
t = turtle.Turtle()
t.speed(0)

# Drawing Grid Lines

# _|_|_
# _|_|_
#  | |
def board_grid(): 
    t.penup()
    t.goto(-50,150)
    t.pendown()
    t.goto(-50,-150)
    t.penup() 
    t.goto(50,150)
    t.pendown()
    t.goto(50,-150)
    t.penup()
    t.goto(-150,50)
    t.pendown()
    t.goto(150,50)
    t.penup()
    t.goto(-150,-50)
    t.pendown()
    t.goto(150,-50)
    t.penup()

# Creating Board as List
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_turn = "X" 

# Function to check win
def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False

# Function to check tie
def check_tie(): 
    if " " not in board: 
        print("Its a tie!")
        turtle.done() 

 
# Function to handle player's move
def make_move(x, y):
    global player_turn
    global mx
    global my 
    
    # 1
    if -150 < x < -50 and 50 < y < 150 and board[0] == " " and not check_win(): 
        mx = -100 
        my = 100
        board[0] = player_turn 
        draw_symbol(player_turn, mx, my)

        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 2
    if -50 < x < 50 and 50 < y < 150 and board[1] == " " and not check_win(): 
        mx = 0 
        my = 100
        board[1] = player_turn 
        draw_symbol(player_turn, mx, my)

        check_tie()

        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"
    # 3
    if 50 < x < 150 and 50 < y < 150 and board[2] == " " and not check_win(): 
        mx = 100 
        my = 100
        board[2] = player_turn 
        draw_symbol(player_turn, mx, my)

        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 4
    if -150 < x < -50 and -50 < y < 50 and board[3] == " " and not check_win(): 
        mx = -100 
        my = 0
        board[3] = player_turn 
        draw_symbol(player_turn, mx, my)

        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 5
    if -50 < x < 50 and -50 < y < 50 and board[4] == " " and not check_win(): 
        mx = 0 
        my = 0
        board[4] = player_turn 
        draw_symbol(player_turn, mx, my)
        
        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 6
    if 50 < x < 150 and -50 < y < 50 and board[5] == " " and not check_win(): 
        mx = 100 
        my = 0
        board[5] = player_turn 
        draw_symbol(player_turn, mx, my)
        
        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 7
    if (-150 < x < -50) and (-150 < y < -50) and board[6] == " " and not check_win(): 
        mx = -100 
        my = -100
        board[6] = player_turn 
        draw_symbol(player_turn, mx, my)
        
        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 8
    if (-50 < x < 50) and (-150 < y < -50) and board[7] == " " and not check_win(): 
        mx = 0
        my = -100
        board[7] = player_turn 
        draw_symbol(player_turn, mx, my)
        
        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"

    # 9
    if (50 < x < 150) and (-150 < y < -50) and board[8] == " " and not check_win(): 
        mx = 100 
        my = -100
        board[8] = player_turn 
        draw_symbol(player_turn, mx, my)
        
        check_tie()
        if check_win():
            print(f"Player {player_turn} wins!")
        else:
            player_turn = "X" if player_turn == "O" else "O"
     
 
# Function to draw X or O symbol
def draw_symbol(symbol, mx, my):
    t.penup()
    t.goto(mx, my)
    t.pendown()
    if symbol == "X":
        t.left(45)
        t.forward(20)
        t.backward(40)
        t.goto(mx,my)
        t.right(90)
        t.forward(20)
        t.backward(40)
        t.left(45)

    else:
        t.penup()
        t.right(180)
        t.forward(20)
        t.left(90)
        t.pendown()
        t.circle(20)
    
    t.penup()
    t.goto(0, 0)
    t.pendown()


# Initial setup
board_grid()
wn.onscreenclick(make_move)
wn.listen()

wn.mainloop()
