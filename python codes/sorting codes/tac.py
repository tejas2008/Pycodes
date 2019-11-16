board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
   
state = Running    
Mark = 'X'    
def Board():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
def Position(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
def Win():    
    global state    
        
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        state = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        state = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        state = Win    
        
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        state = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        state = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        state=Win    
       
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        state = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        state=Win    
        
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        state=Draw    
    else:            
        state=Running    
    
 
print("Player 1: [X]\n")    
print("Player 2: [O]\n") 
print()    
    
   
while(state == Running):    
       
    Board()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(Position(choice)):    
        board[choice] = Mark    
        player+=1    
        Win()    
    
    
Board()    
if(state==Draw):    
    print("Game Draw")    
elif(state==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won") 