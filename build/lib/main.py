from turtle import Screen
from zmija import Zmija
from hrana import Hrana
from rezultat import Rezultat
import time


ekran=Screen()
ekran.setup(width=600,height=600)
ekran.bgcolor("black")
ekran.title("Zmijica")
ekran.tracer(0)
zmija=Zmija()
hrana=Hrana()
rezultat=Rezultat()
ekran.listen()
ekran.onkey(zmija.levo,"Left")
ekran.onkey(zmija.desno,"Right")
flag=True
r=0
t=0.3
while flag:
    ekran.update()
    time.sleep(t)
    zmija.kretanje()
    if zmija.telo[0].distance(hrana.hrana)<15:
        r+=1
        t-=0.0033
        if r%5 == 4:
            hrana.velika()
        else:
            hrana.premesti()
        if r%5==0:
            zmija.produzi()
            t -= 0.0033
        zmija.produzi()
        rezultat.clear()
        rezultat.prikaz()
    if zmija.telo[0].xcor()>300 or zmija.telo[0].xcor()<-300 or zmija.telo[0].ycor()<-300 or zmija.telo[0].ycor()> 300:
        rezultat.udaracZid()
        flag=False
    for i in range(1, len(zmija.telo) - 1, 1):
        if zmija.telo[0].distance(zmija.telo[i])<10:
            flag = False
            rezultat.udaracRep()

ekran.exitonclick()