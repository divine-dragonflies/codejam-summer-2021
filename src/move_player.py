
board = [['.', '.', '.', '.', '.', '.', '.', '.'],
         ['.', '.', '.', '.', '.', '.', '.', 'd'], 
         ['.', '.', '.', '.', '.', '.', '.', '.'], 
         ['w', 'w', 'w', 'w', ' ', 'w', 'w', 'w'], 
         ['.', '.', '.', '.', '.', '.', '.', '.'], 
         ['.', '.', '.', '.', '.', '.', '.', '.'], 
         ['.', '.', '.', '.', '.', 'p', '.', '.']]

def move_player(board,direction):
    
    for i in range(len(board)):
        if 'p' in board[i]:
            y=i
            x=board[i].index('p')
            coordinates_index=[x,y]
            break
    
    if direction == "u":
        if coordinates_index[1]!=0 and board[x][y-1]!="w":
            board[x][y-1]="p"
            board[x][y]="."
            return True
        else :
            return False

    elif direction == "d":
        if coordinates_index[1]!=len(board)-1 and board[x][y+1]!="w":
            board[x][y+1]="p"
            board[x][y]="."
            return True
        else :
            return False 

    elif direction == "l":
        if coordinates_index[0]!=0 and board[x-1][y]!="w":
            board[x-1][y]="p"
            board[x][y]="."
            return True
        else :
            return False

    elif direction == "r":
        if coordinates_index[0]!=len(board[0])-1 and board[x+1][y]!="w":
            board[x+1][y]="p"
            board[x][y]="."
            return True
        else :
            return False     
             


print(move_player(board,"d"))    