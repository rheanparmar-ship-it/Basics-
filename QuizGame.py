import turtle
import random
import time
screen = turtle.Screen()
pen = turtle.Turtle()
screen.setup(1000,700)
screen.bgcolor("hotpink")
pen.up()
pen.goto(-250,-0)
pen.write("WELCOME", font=("arial", 75))
pen.goto(-300,-100)
pen.write("to the amazing quiz game", font=("arial", 40))
time.sleep(2.5)
pen.clear()
a=random.randint(1,20)
b=random.randint(1,20)
chances=3
for i in range(3):
    pen.goto(-300,200)
    pen.write(f"Question 1: What is {a}+{b}?", font=("arial", 40))
    user=screen.textinput("Question 1","Enter your answer:")
    user=int(user)
    if user==a+b:
        pen.clear()
        screen.bgcolor("lime")
        pen.goto(-250,0)
        pen.write("CORRECT", font=("arial", 75))
        break
    else:
        pen.clear()
        chances=chances-1
        screen.bgcolor("red")
        pen.goto(-300,0)
        pen.write("INCORRECT", font=("arial", 75))
        pen.goto(-300,-100)
        pen.write(f"You have {chances} chances left", font=("arial", 40))
    if chances==0:
        time.sleep(1.5)
        pen.clear()
        screen.bgcolor("red")
        pen.goto(-400,0)
        pen.write("GAME OVER", font=("arial", 100))
screen.mainloop()