from turtle import *
from zmija import Zmija
from hrana import Hrana
from rezultat import Rezultat
import time
niz = []
class Gameplay:

#prilikom pravljenja instance klase Gameplay prvo se brise sve sa ekrana kreira pocetnu zmiju koja ima 3 segmenta
#postavlja rezultat na 0 i generise hranu na nekom nasumičnom mestu

    def __init__(self, ekran, zid, prepreka):
        ekran.clearscreen()
        ekran.bgcolor("black")
        ekran.tracer(0)
        self.flag=True
        self.zmija = Zmija()
        self.hrana = Hrana()
        self.rezultat = Rezultat()
        self.okvir()
        self.flag1=True
        self.flag2=True
        self.igra(ekran,zid,prepreka)

    def klik(self):
        self.flag1=False
        self.flag2=True
    def klik2(self):
        self.flag1 = False
        self.flag2 = False
#Funkcija okvir pravi arenu po kojoj se kreće zmija
    def okvir(self):
        t = Turtle()
        t.penup()
        t.goto(-293, 293)
        t.pendown()
        t.pencolor("white")
        t.pensize(5)
        t.hideturtle()
        for i in range(0, 4, 1):
            if i % 2 == 0:
                t.goto(t.xcor() * -1, t.ycor())
            else:
                t.goto(t.xcor(), t.ycor() * -1)
    def igra(self,ekran,zid,prepreka):
        #postavljamo ekran na listen mode u kojem će on osluškivati naše klikove na tastere
        ekran.listen()
        ekran.onkey(self.zmija.levo, "Left")
        ekran.onkey(self.zmija.desno, "Right")
        flag = True
        r = 0
        t = 0.7

        if prepreka:
            self.zmija.prepreka()
        # sledeća petlja služi kako bi se naša zmija kretala sve dok ne udari u nešto, jela hranu i rasla
        while flag:
            ekran.update()
            time.sleep(t)
            self.zmija.kretanje()
            if zid:
                self.zmija.walls()
            else:
                self.zmija.nowalls()

            print(self.zmija.telo[0].pos())
            if self.zmija.telo[0].distance(self.hrana.hrana) < 15 or (self.zmija.telo[0].distance(self.hrana.hrana) < 20 and r%5==4):
                r += 1
                t /= 1.1
                if r % 5 == 4:
                    self.hrana.velika()
                else:
                    self.hrana.premesti()
                if r % 5 == 0:
                    self.zmija.produzi()
                    t /= 1.1
                self.zmija.produzi()
                self.rezultat.clear()
                self.rezultat.prikaz()
            for i in range(1, len(self.zmija.telo) - 1, 1):
                if abs(self.zmija.telo[0].xcor()-self.zmija.telo[i].xcor())<10 and abs(self.zmija.telo[0].ycor()-self.zmija.telo[i].ycor())<10 :
                    flag = False
                    self.rezultat.udaracRep()
             #   if self.zmija.telo[0].distance(self.zmija.telo[i]) < 10:

            for i in range(0, len(self.zmija.prepreke), 1):
                if self.zmija.telo[0].distance(self.zmija.prepreke[i]) < 30:
                    self.zmija.telo[0].ht()
                    flag = False
                    self.rezultat.udaracRep()
        #sledeća kornjača prikazuje korisniku poruku šta on treba da uradi nakon što je izgubio u igrici
        tur = Turtle()
        tur.hideturtle()
        tur.penup()
        tur.goto(0, -280)
        tur.right(90)
        tur.color("white")
        tur.write("To start again click Space\nTo return to main menu click Esc", False, align="center",
                  font=("Baskerville Old Face", 24, "normal"))
        ekran.onkey(self.klik, "space")
        ekran.onkey(self.klik2, "Escape")

        while(self.flag1):
            ekran.update()


def crvena():
    for i in range(0, len(niz), 1):
        niz[i].color("red")

def zuta():
    for i in range(0, len(niz), 1):
        niz[i].color("yellow")

