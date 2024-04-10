from turtle import Turtle

class Rezultat(Turtle):
    def __init__(self):
        super().__init__()
        self.r=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,310)
        self.write(f"Score: {self.r}" , False, align="center", font=("Arial",24,"normal"))
    def udaracRep(self):
        self.goto(0, 0)
        self.write("Game over!", align="center", font=("Arial", 24, "normal"))


    def prikaz(self):
        self.r+=1
        self.write(f"Score: {self.r}", False, align="center", font=("Arial",24,"normal"))
