import tkinter
import tkinter.messagebox as msg
import random
BG_COLOR="pink"
windown=tkinter.Tk()
windown.geometry("1680x980+120+0")
windown.title("Крестики Нолики")
windown.configure(bg=BG_COLOR,cursor="dotbox")

area=[["*","*","*"],["*","*","*"],["*","*","*"]]
for i in area:
    print(i)
  
areabtn=[]
for j in range(-1,2):
    areabtn.append([])
    for i in range(-1,2):
        btn1=tkinter.Button(windown,bg="pink",font=("Arial", 100))

        btn1.place(relx=0.5,x= i*300,y=450+300*j,width=300,height=300,anchor="center")

        areabtn[j+1].append(btn1)
        areabtn[j+1][i+1]["command"]=lambda b=btn1, row=j+1, col=i+1: push(b,row,col)
        
for i in areabtn:
    print(i)
turn=1

def new():
    global turn ,area , areabtn
    turn=1
    area=[["*","*","*"],["*","*","*"],["*","*","*"]]

    for j in range(-1,2):
        for i in range(-1,2):
            areabtn[j+1][i+1]["text"]=""

def chek():
    if area[0][0]=="x" and area[0][1]=="x" and area[0][2]=="x":
            return "x"
    elif area[1][0]=="x" and area[1][1]=="x" and area[1][2]=="x":
            return "x"
    elif area[2][0]=="x" and area[2][1]=="x" and area[2][2]=="x":
            return "x"
    elif area[0][0]=="x" and area[1][0]=="x" and area[2][0]=="x":
            return "x"
    elif area[0][1]=="x" and area[1][1]=="x" and area[2][1]=="x":
                return "x"
    elif area[0][2]=="x" and area[1][2]=="x" and area[2][2]=="x":
            return "x"
    elif area[0][0]=="x" and area[1][1]=="x" and area[2][2]=="x":
            return "x"
    elif area[0][2]=="x" and area[1][1]=="x" and area[2][0]=="x":
            return "x"
        
    elif area[0][0]=="0" and area[0][1]=="0" and area[0][2]=="0":
            return "0"
    elif area[1][0]=="0" and area[1][1]=="0" and area[1][2]=="0":
            return "0"
    elif area[2][0]=="0" and area[2][1]=="0" and area[2][2]=="0":
            return "0"
    elif area[0][0]=="0" and area[1][0]=="0" and area[2][0]=="0":
            return "0"
    elif area[0][1]=="0" and area[1][1]=="0" and area[2][1]=="0":
                return "0"
    elif area[0][2]=="0" and area[1][2]=="0" and area[2][2]=="0":
            return "0"
    elif area[0][0]=="0" and area[1][1]=="0" and area[2][2]=="0":
            return "0"
    elif area[0][2]=="0" and area[1][1]=="0" and area[2][0]=="0":
            return "0"
    
    return "draw"

def push(btn,row,col):
    print(row,col)
    if btn ["text"]=="":
        global turn, area, areabtn
        print(turn)
        if turn%2 ==1:
            btn["text"]="x"
            area[row][col]="x"
        if turn%2 ==0:
            btn["text"]="0"
            area[row][col]="0"
        turn=turn+1
        for i in area:
            print(i)
        
        answer=""
        
        winner= chek()
        if winner == "x" :
            answer=msg.askyesnocancel(title="Игра Закончена", message="Победили: Крестики " +"\nХотите играть снова?")
        if   winner =="0":
            answer=msg.askyesnocancel(title="Игра Закончена", message="Победили: Нолики " +"\nХотите играть снова?")

        if winner == "draw" and turn==10 :
            answer=msg.askyesnocancel(title="Игра Закончена", message="Ничья " +"\nХотите играть снова?")

        print(answer)
        if answer== True :
              new()

        elif answer == False:
            windown.destroy()

        elif answer == None:
           windown.destroy()

windown.mainloop()