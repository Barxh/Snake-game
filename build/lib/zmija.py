from turtle import Turtle, Screen
POCETNE_POZICIJE=[(0,0),(-20,0),(-40,0)]
GORE=90
DOLE=270
LEVO=180
DESNO=0

class Zmija:

    def __init__(self):
        self.telo=[]
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
            self.dodaj(self.telo[-1].position())
    def kretanje(self):

        for i in range(len(self.telo) - 1, 0, -1):
            x = self.telo[i - 1].xcor()
            y = self.telo[i - 1].ycor()
            self.telo[i].goto(x, y)
        self.telo[0].forward(20)

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




