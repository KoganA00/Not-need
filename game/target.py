import tkinter, random
MainWindow = tkinter.Tk()


def check(event):
    win= False

    while win==False:
        x = input("guess x ")
        y = input("guess y ")
        y = int(y, 10)
        x = int(x, 10)
        x=x-1
        y = (y-1) * 10
        if x == xr and y == yr:
          win=True
    print("you win")



def Init():

    canvas = tkinter.Canvas(MainWindow, height=700, width=1000, background="green")
    canvas.pack()
    oval=canvas.create_oval(10,10,20,20)
    oval=canvas.create_oval(20,10,30,20)
    y=0
    global xr,yr
    xr=random.randint(0,100)
    yr=random.randint(0,70)
    yr=yr*10
    while y<700:
     for x in range (100):
            if x==xr and y==yr:
               oval = canvas.create_oval(x * 10, y, x * 10 + 10, y + 10, fill="pink")

            else:
              oval = canvas.create_oval(x*10, y, x*10+10, y+10, fill="red")
     y+=10
     canvas.bind("<Button>",check)

if __name__=="__main__":
    Init()
    MainWindow.mainloop()
