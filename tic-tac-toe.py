
from tkinter import *
import tkinter.messagebox as msg

rose = Tk() # creating a window
rose.title("TIC-TAC-TOE")
Label(rose,text = "Player 1 : X", font = 'calibri 16'). grid(row = 0, column = 1)
Label(rose,text = "Player 2 : O", font = 'calibri 16'). grid(row = 0, column = 2)

digits = [1,2,3,4,5,6,7,8,9] 
mark = '' # will be used to play the X and O
count = 0 # counting the number of clicks
panels = ['panel'] * 10

# function for winning the game
def win (panels, sign):
    return(
        (panels[1]== panels[2] == panels[3] == sign)
        or (panels[1] == panels[4] == panels[7] == sign)
        or (panels[1] == panels[5] == panels[9] == sign)
        or (panels[2] == panels[5] == panels[8] == sign)
        or (panels[3] == panels[6] == panels[9] == sign)
        or (panels[3] == panels[5] == panels[7] == sign)
        or (panels[4] == panels[6] == panels[5] == sign)
        or (panels[7] == panels[8] == panels[9] == sign)
    )
def checker(digit):
    global count,mark,digits  # global variables

    # check if the button is clicked

# button 1
    if digit == 2 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
          mark = "X"
          panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_1.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
#button2
    if digit == 2 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_2.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
#button3
    if digit == 3 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_3.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
#button4
    if digit == 4 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_4.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
#button 5
    if digit == 5 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_5.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
# button 6
    if digit == 6 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_6.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
# button 7 
    if digit == 7 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_7.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
# button 8 
    if digit == 8 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "0"
            panels[digit] = mark
        
        button_8.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
# button 9 
    if digit == 9 and digit in digits: 
        digits.remove(digit)
    # playinger 1 will play of the value of the count is even
        if count % 2 == 0:
            mark = "X"
            panels[digit] = mark
        elif count % 2 != 0:
            mark = "O"
            panels[digit] = mark
        
        button_9.config(text = mark)
        count = count + 1
        sign = mark

        if(win(panels,sign) and sign == "X"):
            msg.showinfo("Result", "Player1 WINS")
            rose.destroy()
        elif(win(panels,sign) and sign == "O"):
            msg.showinfo("Result", 'Player2 WINS')
            rose.destroy()
   
    # if count is greater than 8, the match is tied
    if(count > 8 and win(panels,"X") == False and win(panels,"O") == False):
        msg.showinfo("Result", "Match Tied")
        rose.destroy()

button_1 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(1))
button_1.grid(row = 1, column = 1)
button_2 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(2))
button_2.grid(row = 1, column = 2)
button_3 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(3))
button_3.grid(row = 1, column = 3)
button_4 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(4))
button_4.grid(row = 2, column = 1)
button_5 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(5))
button_5.grid(row = 2, column = 2)
button_6 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(6))
button_6.grid(row = 2, column = 3)
button_7 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(7))
button_7.grid(row = 3, column = 1)
button_8 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(8))
button_8.grid(row = 3, column = 2)
button_9 = Button(rose,width = 16, height = 8, font = ("calibri 16"), command = lambda:checker(9))
button_9.grid(row = 3, column = 3)
rose.mainloop() # tells the events (above) to run