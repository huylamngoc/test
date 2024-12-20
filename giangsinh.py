import turtle as tu
from turtle import *
import random as ra
import tkinter as tk
import math

word = "Chúc Em Bé 16 tuổi giáng sinh vui vẻ" 

def christmas():
    setup(1.0, 1.0, None, None)
    screensize(1.0, 1.0)   
    bgcolor('black')  
    title("🎄")
    t = tu.Pen()
    t.ht()            

    def tree():  
        pencolor("#008500")
        pensize(10)
        penup()
        hideturtle()
        goto(0, 150)
        showturtle()
        pendown()
        shape(name="classic")

        seth(-120)
        for i in range(10):
            fd(12)
            right(2)
        penup()
        goto(0, 150)
        seth(-60)
        pendown()
        for i in range(10):
            fd(12)
            left(2)
        seth(-150)
        penup()
        fd(10)
        pendown()
        for i in range(5):
            fd(10)
            right(15)
        seth(-150)
        penup()
        fd(8)
        pendown()
        for i in range(5):
            fd(10)
            right(15)
        seth(-155)
        penup()
        fd(5)
        pendown()
        for i in range(5):
            fd(7)
            right(15)

        penup()
        goto(-55, 34)
        pendown()
        seth(-120)
        for i in range(10):
            fd(8)
            right(5)

        penup()
        goto(50, 35)
        seth(-60)
        pendown()
        for i in range(10):
            fd(8)
            left(5)
        seth(-120)
        penup()
        fd(10)
        seth(-145)
        pendown()
        for i in range(5):
            fd(10)
            right(15)
        penup()
        fd(10)
        seth(-145)
        pendown()
        for i in range(5):
            fd(12)
            right(15)
        penup()
        fd(8)
        seth(-145)
        pendown()
        for i in range(5):
            fd(10)
            right(15)
        penup()
        seth(-155)
        fd(8)
        pendown()
        for i in range(5):
            fd(11)
            right(15)

        penup()
        goto(-100, -40)
        seth(-120)
        pendown()
        for i in range(10):
            fd(6)
            right(3)
        penup()
        goto(80, -39)
        seth(-50)
        pendown()
        for i in range(10):
            fd(6)
            left(3)
        seth(-155)
        penup()
        fd(10)
        pendown()
        for i in range(5):
            fd(8)
            right(10)
        penup()
        fd(8)
        seth(-145)
        pendown()
        for i in range(7):
            fd(8)
            right(10)
        penup()
        fd(8)
        seth(-145)
        pendown()
        for i in range(7):
            fd(7)
            right(10)
        penup()
        fd(8)
        seth(-145)
        pendown()
        for i in range(7):
            fd(7)
            right(10)
        penup()
        fd(8)
        seth(-140)
        pendown()
        for i in range(7):
            fd(6)
            right(10)


        penup()
        goto(-120, -95)
        seth(-130)
        pendown()
        for i in range(7):
            fd(10)
            right(5)
        penup()
        goto(100, -95)
        seth(-50)
        pendown()
        for i in range(7):
            fd(10)
            left(5)
        penup()
        seth(-120)
        fd(10)
        seth(-155)
        pendown()
        for i in range(6):
            fd(8)
            right(10)
        penup()
        seth(-160)
        fd(10)
        seth(-155)
        pendown()
        for i in range(6):
            fd(8)
            right(10)
        penup()
        seth(-160)
        fd(10)
        seth(-155)
        pendown()
        for i in range(6):
            fd(8)
            right(10)
        penup()
        seth(-160)
        fd(10)
        seth(-160)
        pendown()
        for i in range(6):
            fd(8)
            right(10)
        penup()
        seth(-160)
        fd(10)
        seth(-160)
        pendown()
        for i in range(6):
            fd(8)
            right(10)
        penup()
        seth(-160)
        fd(10)
        seth(-165)
        pendown()
        for i in range(5):
            fd(10)
            right(11)

        penup()
        goto(-70, -165)
        seth(-85)
        pendown()
        for i in range(3):
            fd(5)
            left(3)
        penup()
        goto(70, -165)
        seth(-95)
        pendown()
        for i in range(3):
            fd(5)
            right(3)
        seth(-170)
        penup()
        fd(10)
        pendown()
        pendown()
        for i in range(10):
            fd(12)
            right(2)

        penup()
        goto(70, -165)
        pendown()
        seth(-90)
        pensize(8)
        pencolor("#00cc00")
        circle(-20, 90)

        penup()
        goto(30, -185)
        pendown()
        seth(-180)
        pensize(8)
        pencolor("#00cc00")
        fd(40)

        penup()
        goto(-5, -170)
        pendown()
        seth(-180)
        pensize(8)
        pencolor("#00cc00")
        fd(35)


        def guest(x, y, z):
            penup()
            goto(x, y)
            seth(-z)
            pendown()
            for angel in range(5):
                fd(10)
                right(10)


        def guet(x, y, z):
            penup()
            goto(x, y)
            seth(-z)
            pendown()
            for angel in range(5):
                fd(10)
                left(10)


        def qu(x, y, z):
            penup()
            goto(x, y)
            seth(-z)
            pendown()
            for angel in range(5):
                fd(6)
                right(10)
            seth(-150)
            fd(20)


        guest(-70, -150, 160)
        guest(100, -150, 160)
        guet(110, -110, 50)
        guest(160, -140, 150)
        qu(80, -120, 180)
        guest(70, -85, 165)
        guest(-40, -85, 165)
        guet(90, -50, 50)
        guest(130, -80, 150)
        pencolor("#00cc00")
        qu(-40, -60, 180)
        pencolor('#00cc00')
        qu(80, -30, 180)
        pencolor("#00cc00")
        qu(40, 10, 180)
        pencolor("#00cc00")
        guest(-60, 30, 120)
        guest(-20, -20, 150)
        guet(45, 40, 60)
        guest(-30, 40, 170)
        guest(-30, 110, 115)
        guet(40, 90, 60)
        guest(80, 50, 160)
        pencolor("red")


        def hdj(x, y):
            penup()
            goto(x, y)
            seth(80)
            pendown()
            pensize(2)
            circle(5)
            seth(10)
            fd(15)
            seth(120)
            fd(20)
            seth(240)
            fd(20)
            seth(180)
            fd(20)
            seth(-60)
            fd(20)
            seth(50)
            fd(20)
            seth(-40)
            fd(30)
            seth(-130)
            fd(5)
            seth(135)
            fd(30)
            seth(-60)
            fd(30)
            seth(-150)
            fd(6)
            seth(110)
            fd(30)


        def uit(x, y):
            penup()
            goto(x, y)
            pendown()
            pensize(2)
            circle(5)
            seth(-10)
            fd(15)
            seth(90)
            fd(15)
            seth(200)
            fd(15)
            seth(160)
            fd(15)
            seth(-90)
            fd(15)
            seth(10)
            fd(15)
            seth(-60)
            fd(20)
            seth(-180)
            fd(5)
            seth(110)
            fd(20)
            seth(-90)
            fd(20)
            seth(-180)
            fd(6)
            seth(70)
            fd(15)
            hideturtle()


        def yut(x, y, z):
            penup()
            goto(x, y)
            pendown()
            seth(z)
            for po in range(5):
                fd(4)
                left(36)


        def ytu(x, y, z):
            penup()
            goto(x, y)
            pendown()
            seth(z)
            for kk in range(5):
                fd(4)
                left(36)

        seth(0)
        uit(40, -160)
        hdj(-80, -120)
        yut(-67, -115, 120)
        yut(-86, -123, 150)
        hdj(40, -50)
        yut(52, -45, 130)
        yut(34, -55, 160)
        seth(0)
        pencolor("pink")
        uit(-20, -60)
        ytu(-4, -60, 100)
        ytu(-20, -60, 120)
        hdj(-30, 20)
        yut(-15, 25, 130)
        yut(-40, 20, 180)
        uit(30, 70)
        ytu(45, 70, 100)
        ytu(30, 70, 120)

        pencolor("yellow")
        pensize(5)
        penup()
        seth(0)
        goto(0, 150)
        pendown()
        circle(10)
        seth(-15)
        fd(40)
        seth(90)
        fd(40)
        seth(200)
        fd(40)
        seth(160)
        fd(40)
        seth(-90)
        fd(40)
        seth(15)
        fd(40)
        seth(-70)
        pencolor("yellow")
        pensize(4)
        fd(40)
        seth(-180)
        fd(10)
        seth(100)
        fd(40)
        seth(-100)
        fd(40)
        seth(-180)
        fd(10)
        seth(70)
        fd(40)
        penup()
        seth(0)
        goto(0, 130)
        pencolor("yellow")
        pendown()

        def iou(x, y, z):
            penup()
            goto(x, y)
            pencolor("yellow")
            pendown()
            seth(z)
            for po in range(10):
                fd(4)
                left(18)


        seth(0)
        iou(35, 145, 100)
        iou(-7, 145, 110)
        pencolor("red")
        pensize(7)
        penup()
        goto(-35, 135)
        pendown()

        seth(-20)
        pensize(2)
        penup()
        goto(-30, -120)
        pencolor("white")
        pendown()
        fillcolor("red")
        fd(30)
        circle(4, 180)
        fd(30)
        circle(4, 180)
        penup()
        goto(-25, -115)
        seth(75)
        pendown()
        begin_fill()
        for i in range(5):
            fd(6)
            right(20)
        seth(-10)
        for i in range(5):
            fd(8)
            right(15)
        seth(145)
        for i in range(5):
            fd(5)
            left(2)
        seth(90)
        for i in range(5):
            fd(1)
            left(2)
        seth(-90)
        for i in range(4):
            fd(4)
            right(6)
        seth(161)
        fd(30)
        end_fill()
        pensize(1)
        pencolor("white")


        def koc(x, y, size):
            pensize(2)
            pencolor("yellow")
            penup()
            goto(x, y)
            pendown()
            begin_fill()
            fillcolor("yellow")
            for i in range(5):
                left(72)
                fd(size)
                right(144)
                fd(size)
            end_fill()


        
        seth(-15)
        koc(-120, -70, 10)
        seth(10)
        koc(100, -20, 10)
        seth(-10)
        koc(10, 40, 10)
        seth(30)
        koc(-80, 60, 10)
        koc(100, -150, 10)
        koc(-140, -150, 10)
        koc(20, 120, 10)

        seth(-20)
        pensize(2)
        penup()
        goto(-20, 80)
        pencolor("white")
        pendown()
        fillcolor("red")
        fd(25)
        circle(4, 180)
        fd(25)
        circle(4, 180)
        penup()
        goto(-15, 80)
        pendown()
        begin_fill()
        fillcolor("red")
        seth(-120)
        fd(20)
        seth(150)
        fd(5)
        circle(7, 180)
        fd(15)
        circle(5, 90)
        fd(30)
        seth(160)
        fd(18)
        end_fill()

        penup()
        seth(0)
        goto(0, 240)
        pendown()
        pencolor("yellow")
        write(word, align="center", font=("Comic Sans MS", 40, "bold"))

        penup()
        seth(0)
        goto(100, -251)
        pendown()

        pencolor("yellow")
        write("Merry Christmas To Anh thư!            ", align="center", font=("Comic Sans MS", 24, "bold"))

    class Hat():          
        def __init__(self): 
            self.x=ra.randint(-1000,1000)   
            self.y=ra.randint(-500,500)     
            self.r=ra.uniform(0.5,1)
            self.k=ra.randint(-50,50)
            self.f = ra.uniform(-3.14, 3.14)
            self.speed = ra.randint(3, 8)

        def draw(self):
            t.penup()                
            t.goto(self.x,self.y)   
            t.pendown()             
            t.seth(-20 + self.k)
            t.pensize(2)
            t.pencolor("white")
            t.begin_fill()
            t.fillcolor("white")
            t.fd(30 * self.r)
            t.circle(4 * self.r, 180)
            t.fd(30 * self.r)
            t.circle(4 * self.r, 180)
            t.end_fill()
            t.seth(75 + self.k)
            t.begin_fill()
            t.fillcolor("red")
            for i in range(5):
                t.fd(6 * self.r)
                t.right(20)
            t.seth(-10 + self.k)
            for i in range(5):
                t.fd(8 * self.r)
                t.right(15)
            t.seth(145 + self.k)
            for i in range(5):
                t.fd(5 * self.r)
                t.left(2)
            t.seth(90 + self.k)
            for i in range(5):
                t.fd(1 * self.r)
                t.left(2)
            t.seth(-90 + self.k)
            for i in range(4):
                t.fd(4 * self.r)
                t.right(6)
            t.seth(161 + self.k)
            t.fd(30 * self.r)
            t.end_fill()

        def change(self):
            if self.y >= -500:        
                self.y -= self.speed   
                self.x += self.speed * math.sin(self.f) 
                self.f += 0.1           
            else:                     
                self.r = ra.uniform(0.5,1)
                self.x = ra.randint(-1000,1000)
                self.y = 500
                self.f = ra.uniform(-3.14,3.14)
                self.speed = ra.randint(3,8)
                self.k = ra.uniform(-50,50)



    class Sock():        
        def __init__(self): 
            self.x = ra.randint(-1000,1000)   
            self.y = ra.randint(-500,500)                          
            self.r = ra.uniform(0.5,1)
            self.s = ra.randint(-50,50)
            self.f = ra.uniform(-3.14, 3.14)
            self.speed = ra.randint(3, 8)

        def draw(self):
            t.penup()               
            t.goto(self.x,self.y)     
            t.pendown()                
            t.seth(self.s)
            t.pensize(2)
            t.pencolor("white")
            t.begin_fill()
            t.fillcolor("white")
            t.fd(25 * self.r)
            t.circle(4 * self.r, 180)
            t.fd(25 * self.r)
            t.circle(4 * self.r, 180)
            t.end_fill()
            t.begin_fill()
            t.fillcolor("red")
            t.right(90)
            t.fd(20 * self.r)
            t.left(-100)
            t.fd(5 * self.r)
            t.circle(7 * self.r, 180)
            t.fd(15 * self.r)
            t.circle(5 * self.r, 90)
            t.fd(30 * self.r)
            t.end_fill()

        def change(self):
            if self.y >= -500:        
                self.y -= self.speed   
                self.x += self.speed * math.sin(self.f)    
                self.f += 0.1         
            else:                    
                self.r = ra.uniform(0.5,1)
                self.x = ra.randint(-1000,1000)
                self.y = 500
                self.f = ra.uniform(-3.14,3.14)
                self.speed = ra.randint(3,8)

    class Star():        
        def __init__(self):   
            self.r=1     
            self.x=ra.randint(-1000,1000)    
            self.y=ra.randint(-500,500)        
            self.c="gold"         
        def draw(self):                   
            t.pensize(1)           
            t.penup()                 
            t.goto(self.x,self.y)   
            t.pendown()              
            t.color(self.c)          
            for i in range(5):        
                t.forward(self.r)
                t.right(144)
                t.forward(self.r)
                t.left(72)
        def change(self):            
            if self.r<=10:        
                self.r+=0.5       
            else:                    
                self.r = 1
                self.x = ra.randint(-1000, 1000)
                self.y = ra.randint(-500, 500)
                self.c = "gold"

    class Snow():  
        def __init__(self):
            self.r = ra.uniform(2,3)     
            self.x = ra.randint(-1000,1000) 
            self.y = ra.randint(-500,500)    
            self.f = ra.uniform(-3.14,3.14) 
            self.speed = ra.randint(10,15)    
            self.color = "white"   
            self.outline = 2               
        def draw(self):                
            x=self.r                   
            t.pensize(self.outline)  
            t.penup()               
            t.goto(self.x,self.y)  
            t.pendown()              
            t.color(self.color)        
            for i in range(6):       
                t.forward(x*5)
                t.backward(x*2)
                t.left(60)
                t.forward(x*2)
                t.backward(x*2)
                t.right(120)
                t.forward(x*2)
                t.backward(x*2)
                t.left(60)
                t.backward(x*3)
                t.right(60)
        def change(self):                  
            if self.y >= -500:         
                self.y -= self.speed   
                self.x -= self.speed * math.sin(self.f)   
                self.f -= 0.1         
            else:                       
                self.r = ra.uniform(2,3)
                self.x = ra.randint(-1000,1000)
                self.y = 500
                self.f = ra.uniform(-3.14,3.14)
                self.speed = ra.randint(10,15)
                self.color = "white"
                self.outline = 2

    Christmas=[]              
    for i in range(99):           
        Christmas.append(Hat())   
        Christmas.append(Sock())  
    
        Christmas.append(Snow()) 
        Christmas.append(Snow())
    while True:                  
        tu.tracer(0)
        t.clear()
        t.penup()
        t.goto(-366,0)
        t.pendown()
        tree()
        for i in range(66):
            Christmas[i].draw()
            Christmas[i].change()
        tu.update()
    tu.mainloop()
def love():
    root = tk.Tk()
    root.title('🎄')
    root.resizable(0, 0)
    root.wm_attributes("-toolwindow", 1)
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    widths = 300
    heights = 100
    x = (screenwidth - widths) / 2
    y = (screenheight - heights) / 2 - 66
    root.geometry('%dx%d+%d+%d' % (widths, heights, x, y))
    tk.Label(root, text='Anh Thư có yêu nh ko=)))!', width=32, font=('Verdana', 12, 'bold'), anchor='center').place(x=0, y=0)

    def OK(): 
        root.destroy()
        christmas() 


    def NO(): 
        tk.messagebox.showwarning('🎄', 'Chọn sai, chọn lại!')


    def closeWindow():
        tk.messagebox.showwarning('🎄', 'Ai cho thoát')


    tk.Button(root, text='có', width=5, height=1, command=OK).place(x=80, y=50)
    tk.Button(root, text='không', width=5, height=1, command=NO).place(x=160, y=50)
    root.protocol('WM_DELETE_WINDOW', closeWindow) 
    root.mainloop()

if __name__ == "__main__":
    love()
