from tkinter import *

player = 1
count_step = 0
win = 0

def click_button1():
    check_win()
    if win == 1:
        block_button()
    else: 
        btn1["text"] = f"{check_player()}"
        btn1["state"] = "disabled"  

def click_button2():
    check_win()
    if win == 1:
        block_button()
    else:
        btn2["text"] = f"{check_player()}"
        btn2["state"] = "disabled"  

def click_button3():
    check_win()
    if win == 1:
        block_button()
    else:
        btn3["text"] = f"{check_player()}"
        btn3["state"] = "disabled"  

def click_button4():
    check_win()
    if win == 1:
        block_button()
    else:
        btn4["text"] = f"{check_player()}"
        btn4["state"] = "disabled"  

def click_button5():
    check_win()
    if win == 1:
        block_button()
    else:
        btn5["text"] = f"{check_player()}"
        btn5["state"] = "disabled"  

def click_button6():
    check_win()
    if win == 1:
        block_button()
    else:
        btn6["text"] = f"{check_player()}"
        btn6["state"] = "disabled"  

def click_button7():
    check_win()
    if win == 1:
        block_button()
    else:
        btn7["text"] = f"{check_player()}"  
        btn7["state"] = "disabled"

def click_button8():
    check_win()
    if win == 1:
        block_button()
    else:
        btn8["text"] = f"{check_player()}"
        btn8["state"] = "disabled"  

def click_button9():
    check_win()
    if win == 1:
        block_button()
    else:
        btn9["text"] = f"{check_player()}"
        btn9["state"] = "disabled"  

def check_player():
    global player
    global count_step
    if player == 1:
        text = 'X'
        player = 2
        count_step += 1
        return text
    elif player == 2:
        text = 'O'
        player = 1 
        count_step += 1
        return text

def check_win():
    global color, win
    if count_step > 4:
        if (btn1["text"] == btn2["text"] == btn3["text"]) and btn1["text"] != ' ':
            btn1["bg"] = 'yellow'
            btn2["bg"] = 'yellow'
            btn3["bg"] = 'yellow'
            win = 1
            return
        elif (btn4["text"] == btn5["text"] == btn6["text"]) and btn4["text"] != ' ':
            btn4["bg"] = 'yellow'
            btn5["bg"] = 'yellow'
            btn6["bg"] = 'yellow'
            win = 1
            return
        elif (btn7["text"] == btn8["text"] == btn9["text"]) and btn7["text"] != ' ':
            btn7["bg"] = 'yellow'
            btn8["bg"] = 'yellow'
            btn9["bg"] = 'yellow'
            win = 1
        elif (btn1["text"] == btn4["text"] == btn7["text"]) and btn1["text"] != ' ':
            btn1["bg"] = 'yellow'
            btn4["bg"] = 'yellow'
            btn7["bg"] = 'yellow'
            win = 1
        elif (btn2["text"] == btn5["text"] == btn8["text"]) and btn2["text"] != ' ':
            btn2["bg"] = 'yellow'
            btn5["bg"] = 'yellow'
            btn8["bg"] = 'yellow'
            win = 1
        elif (btn3["text"] == btn6["text"] == btn9["text"]) and btn3["text"] != ' ':
            btn3["bg"] = 'yellow'
            btn6["bg"] = 'yellow'
            btn9["bg"] = 'yellow'
            win = 1
            return
        elif (btn1["text"] == btn5["text"] == btn9["text"]) and btn1["text"] != ' ':
            btn1["bg"] = 'yellow'
            btn5["bg"] = 'yellow'
            btn9["bg"] = 'yellow'
            win = 1
            return
        elif (btn3["text"] == btn5["text"] == btn7["text"]) and btn3["text"] != ' ':
            btn3["bg"] = 'yellow'
            btn5["bg"] = 'yellow'
            btn7["bg"] = 'yellow'
            win = 1
            return

def block_button():
    btn1["state"] = "disabled"  
    btn2["state"] = "disabled"  
    btn3["state"] = "disabled"  
    btn4["state"] = "disabled"  
    btn5["state"] = "disabled"  
    btn6["state"] = "disabled"   
    btn7["state"] = "disabled"
    btn8["state"] = "disabled"
    btn9["state"] = "disabled"  

window = Tk()
window.title('Крестики-нолики')
btn1 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button1)
btn1.grid(row='0', column='0')
btn2 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button2)
btn2.grid(row='0', column='1')
btn3 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button3)
btn3.grid(row='0', column='2')
btn4 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button4)
btn4.grid(row='1', column='0')
btn5 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button5)
btn5.grid(row='1', column='1')
btn6 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button6)
btn6.grid(row='1', column='2')
btn7 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button7)
btn7.grid(row='2', column='0')
btn8 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button8)
btn8.grid(row='2', column='1')
btn9 = Button(window, text= ' ', width='10', height='5', bg='white', command = click_button9)
btn9.grid(row='2', column='2')
window.mainloop()