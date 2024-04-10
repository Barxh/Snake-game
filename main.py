import turtle
import time
from turtle import *
from gameplay import Gameplay

def promeni():
    mod[0] = False

# funkcija mode omogućava selekciju modova
def mode():
    #16-18 brise sve sto se nalazilo do tad na ekranu i ponovo definise neke atribute ekrana
    ekran.clearscreen()
    ekran.bgcolor("black")
    ekran.tracer(0)
    k = []
    #sledeća petlja pravi 5 kornjača i dodaje ih u niz
    for i in range(0, 5, 1):
        k.append(Turtle())
        k[i].penup()
        if i < 3:
            k[i].goto(0, 130 - 170 * i)
#23-31 dodajemeo atribute kornjačama
    k[0].shape("classic.gif")
    k[1].shape("nowalls.gif")
    k[2].shape("prepreke.gif")
    k[3].color("white")
    k[3].hideturtle()
    k[3].goto(0, 280)
    k[3].write("Choose your gamemode", False, align="center", font=("Baskerville Old Face", 36, "normal"))
    k[4].goto(300, 300)
    k[4].hideturtle()
    #peta kornjača nam služi za odabir moda tako sto na nas klik odlazi na prostor nekog od dugmadi i tako biramo mod
    ekran.onclick(k[4].goto, 1, True)
    ekran.listen()
    ekran.onkey(welcome, "Escape")
    b = True
    while (b):
        ekran.update()
        if (k[4].xcor() > -150 and k[4].xcor() < 150) and (k[4].ycor() < 205 and k[4].ycor() > 55):
            a = Gameplay(ekran, True, False)
            while (a.flag2):
                a = Gameplay(ekran, True, False)
            b = a.flag2

        if (k[4].xcor() > -150 and k[4].xcor() < 150) and (k[4].ycor() < 35 and k[4].ycor() > -115):
            a = Gameplay(ekran, False, False)
            while (a.flag2):
                a = Gameplay(ekran, False, False)
            b = a.flag2
        if (k[4].xcor() > -150 and k[4].xcor() < 150) and (k[4].ycor() < -135 and k[4].ycor() > -285):
            a = Gameplay(ekran, True, True)
            while (a.flag2):
                a = Gameplay(ekran, True, True)
            b = a.flag2
    return 0



#funkcija credits polako pomera kornjaču, na kojoj se nalazi neki natpis, na gore
def credits():
    ekran.clearscreen()
    ekran.bgcolor("black")
    ekran.tracer(0)
    kor = Turtle()
    kor.color("white")
    kor.left(90)
    kor.penup()
    kor.goto(0, -550)
    kor.shape("tekst.gif")

    ekran.listen()
    ekran.onkey(promeni, "Escape")

    for i in range(1,1050,1):
        ekran.update()
        kor.fd(1)
        time.sleep(0.02)
        if (mod[0])==False:
            return 0

    return 0

#definiše glavni meni
def welcome():
    ekran.clearscreen()
    ekran.bgcolor("black")
    ekran.tracer(0)
    niz = []

    for i in range(0, 5, 1):
        niz.append(Turtle())
        niz[i].penup()
        if i > 0:
            niz[i].goto(0, 0 - 70 * (i - 1))
    niz[0].goto(0, 180)
    niz[0].shape("Zmija.gif")
    niz[0].right(90)

    niz[4].goto(300, 300)
    niz[4].hideturtle()
    niz[1].shape("playy.gif")
    niz[2].shape("untitled.gif")
    niz[3].shape("exit.gif")

    ekran.onclick(niz[4].goto, 1, True)
    a=True
    while (a):
        ekran.update()
        if (niz[4].xcor() > -80 and niz[4].xcor() < 80) and (niz[4].ycor() > -30 and niz[4].ycor() < 30):
            mode()
            a=welcome()
        if (niz[4].xcor() > -80 and niz[4].xcor() < 80) and (niz[4].ycor() < -40 and niz[4].ycor() > -100):
            credits()
            a=welcome()
        if (niz[4].xcor() > -80 and niz[4].xcor() < 80) and (niz[4].ycor() < -110 and niz[4].ycor() > -170):
            return 0
    return 0


turtle.register_shape("playy.gif")
turtle.register_shape("settings.gif")
turtle.register_shape("untitled.gif")
turtle.register_shape("exit.gif")
turtle.register_shape("Zmija.gif")
turtle.register_shape("nowalls.gif")
turtle.register_shape("classic.gif")
turtle.register_shape("prepreke.gif")
turtle.register_shape("tekst.gif")

ekran = Screen()
ekran.setup(width=650, height=700)
ekran.title("Zmijica")

mod = [True]
welcome()
