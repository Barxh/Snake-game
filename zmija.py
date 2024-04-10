import turtle
from turtle import Turtle, Screen
POCETNE_POZICIJE=[(0,0),(-20,0),(-40,0)]
GORE=90
DOLE=270
LEVO=180
DESNO=0

class Zmija:

    def __init__(self):
        self.telo=[]
        self.prepreke=[]
        self.napraviZmiju()
    def napraviZmiju(self):
        for pozicija in POCETNE_POZICIJE:
            self.dodaj(pozicija)
    def dodaj(self,pozicija):
        glava = Turtle("square")
        if len(self.telo)%2==0:
            glava.color("green")
        else:
            glava.color("lime")
        glava.penup()
        glava.goto(pozicija)
        self.telo.append(glava)
    def produzi(self):
            self.dodaj(self.telo[len(self.telo)-1].position())
    def kretanje(self):
#svaki deo zmije ide na mesto svog prethodnika osim glave koja se pokreće za 20 piksela u napred
        for i in range(len(self.telo) - 1, 0, -1):
            x = self.telo[i - 1].xcor()
            y = self.telo[i - 1].ycor()
            self.telo[i].goto(x, y)

        self.telo[0].forward(20)
#walls i no walls su funcije koje dodatno odredjuju način kretanja u zavisnosti od odabranog moda
    def walls(self):
        niz = [300, -300]
        for i in range(0, 2, 1):

            if (self.telo[0].xcor() >=300 or self.telo[0].xcor() <=-300 or self.telo[0].ycor() >=300 or self.telo[0].ycor() <=-300):
                self.telo[0].goto(self.telo[1].pos())
                print("cao")
    def nowalls(self):
        if self.telo[0].xcor()>=300:
            self.telo[0].goto(-280,self.telo[0].ycor())
            print("cao")
        if self.telo[0].xcor()<=-300:
            self.telo[0].goto(280,self.telo[0].ycor())
            print("cao")

        if self.telo[0].ycor()>=300:
            self.telo[0].goto(self.telo[0].xcor(),-280)
            print("cao")

        if self.telo[0].ycor()<=-300:
            self.telo[0].goto(self.telo[0].xcor(),280)
            print("cao")

    # Dodaje prepreke na mapi
    def prepreka(self):
        for i in range(0,2,1):
            self.prepreke.append(Turtle())
            self.prepreke[i].shapesize(stretch_wid=2,stretch_len=2)
            self.prepreke[i].color("white")
            self.prepreke[i].shape("square")
            self.prepreke[i].penup()
        self.prepreke[0].goto(110,130)
        self.prepreke[1].goto(-110,-130)



#funkije levo i desno proveravaju u kom smeru gleda zmija i u zavisnosti od smera ide levo ili desno
    def levo(self):
        if self.telo[0].xcor()-self.telo[1].xcor()==20:
            self.telo[0].setheading(GORE)
        if self.telo[0].xcor() - self.telo[1].xcor() == -20:
            self.telo[0].setheading(DOLE)
        if self.telo[0].ycor()-self.telo[1].ycor()==20:
            self.telo[0].setheading(LEVO)
        if self.telo[0].ycor() - self.telo[1].ycor() == -20:
            self.telo[0].setheading(DESNO)
    def desno(self):
        if self.telo[0].xcor()-self.telo[1].xcor()==20:
            self.telo[0].setheading(DOLE)
        if self.telo[0].xcor() - self.telo[1].xcor() == -20:
            self.telo[0].setheading(GORE)
        if self.telo[0].ycor()-self.telo[1].ycor()==20:
            self.telo[0].setheading(DESNO)
        if self.telo[0].ycor() - self.telo[1].ycor() == -20:
            self.telo[0].setheading(LEVO)




