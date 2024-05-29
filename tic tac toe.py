# Game "tic tac toe"

board = list(range(1, 10))    


def territory(board):                           
    print("—" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")      
        print("—" * 13)


def take_input(player_token):
    flag = False
    while not flag:                  
        enter_num = input("Enter the number where we will place " + player_token + ":  ")
        try:
            enter_num = int(enter_num)            
        except ValueError:
            print("Invalid input. You must enter a number.")
            continue
        if 1 <= enter_num <= 9:
            if str(board[enter_num - 1]) not in "XO":        
                board[enter_num - 1] = player_token      
                flag = True
            else:
                print("Cell is occupied.")
        else:
            print("Invalid input. You must enter a number from 1 to 9.")


def bingo(board):                           
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for j in win:
        if board[j[0]] == board[j[1]] == board[j[2]]:
            return board[j[0]]
    return False


def final(board):
    counter = 0
    flg = False
    while not flg:
        territory(board)        
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        x_o = bingo(board)
        if x_o:
            print(f" ★ ☆ ★  {x_o} won!!! ★ ☆ ★ ")
            flg = True
            break
        if counter == 9:
            print("Draw in the game!")
            break
    territory(board)


final(board)


input("To exit, press the button Enter!")