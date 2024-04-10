from turtle import Turtle

class Rezultat(Turtle):
    def __init__(self):
        super().__init__()
        self.r=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f"Rezultat: {self.r}" , False, align="center", font=("Arial",24,"normal"))
    def udaracRep(self):
        self.goto(0, 0)
        self.write("Kraj igre!", align="center", font=("Arial", 24, "normal"))


    def udaracZid(self):
        self.goto(0,0)
        self.write("Kraj igre!",align="center", font=("Arial",24,"normal"))


    def prikaz(self):
        self.r+=1
        self.write(f"Rezultat: {self.r}", False, align="center", font=("Arial",24,"normal"))

