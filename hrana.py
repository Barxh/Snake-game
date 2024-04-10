from turtle import Turtle
import random


class Hrana:
    def __init__(self):
        self.hrana = Turtle()
        self.hrana.shape("circle")
        self.hrana.penup()
        self.hrana.speed("fastest")
        self.premesti()

    def premesti(self):
        self.hrana.color("white")
        self.hrana.shapesize(stretch_len=0.5, stretch_wid=0.5)
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.hrana.goto(x, y)
    def velika(self):
        self.hrana.shapesize(stretch_len=1, stretch_wid=1)
        self.hrana.color("red")
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.hrana.goto(x, y)


