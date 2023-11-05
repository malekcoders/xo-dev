from tkinter import *


def button(frame):          
    choice=Button(frame,padx=1,bg="white",width=3,text="   ",
             font=('arial',60,'bold'),relief="sunken",bd=10)
    return choice

def playerChoice():
    global player
    # Challenge 01 medium: in playerChoice() method write a code to choice between X and O            
    player = 'O' # remove this line when you implement your code

def reset():
    # Challenge 02 hard: write implementation of reset() method 
    # Challenge 03 easy: show pop-up message when game is over
    root.quit() # remove this line when you implemet your code
    

def check(): 
    # Challenge 04 easy: write pop-up message when game is over before the reset method               
    # horizontal and vertical check                
    for i in range(3):
        if(choice[i][0]["text"] == choice[i][1]["text"] == choice[i][2]["text"] == player
        or choice[0][i]["text"] == choice[1][i]["text"] == choice[2][i]["text"] == player):
            # pop-up message "Congrats!! 'player' has won"
            reset()

    # diagonal check
    if(choice[0][0]["text"] == choice[1][1]["text"] == choice[2][2]["text"] == player
       or choice[0][2]["text"] == choice[1][1]["text"] == choice[2][0]["text"] == player):
        # pop-up message "Congrats!! 'player' has won"
        reset() 

    # draw check
    elif(choice[0][0]["state"] == choice[0][1]["state"] == choice[0][2]["state"]
         == choice[1][0]["state"] == choice[1][1]["state"] == choice[1][2]["state"]
         == choice[2][0]["state"] == choice[2][1]["state"] == choice[2][2]["state"] == DISABLED):
        # pop-up message "The match ended in draw"
        reset()
     
def click(row,col):
        choice[row][col].config(text=player,state=DISABLED,disabledforeground=colour[player])
        check()
        playerChoice()
        label.config(text=player)

root=Tk()
                
# Challenge 05 easy: add text title to the program, and name it "XO Game"
# your code 

# Challenge 06 easy: make player choice random between X and O at the start of the game
player='X'    
  
colour={
    'O':"blue",
    'X':"red"}

choice=[[],[],[]]

for row in range(len(choice)):
        for column in range(len(choice)):
                choice[row].append(button(root))
                choice[row][column].config(command= lambda row=row,col=column:click(row,col))
                choice[row][column].grid(row=row,column=column)
                
label=Label(text=player,font=('arial',22,'bold'))
label.grid(row=3,column=0,columnspan=3)

root.mainloop()