import turtle
import winsound

#Window Setup

window = turtle.Screen()
window.title("PONG GAME")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

#Paddle Setup

#PaddleA
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350,0)

#PaddleB
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.3
ball.dy = 0.3

#Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Play A: 0   Player B: 0", align = "center", font =("Courỉer", 24, "normal"))

#update Score
scoreA = 0
scoreB = 0


#Function for Paddle movement

def paddleAUp():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

#Set moving
window.listen()
window.onkeypress(paddleAUp, "w")
window.onkeypress(paddleADown, "s")
window.onkeypress(paddleBUp, "7")
window.onkeypress(paddleBDown, "4")

#Main game
while True :
    window.update();

    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking up and donw
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    #Border checking left and right
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreA += 1
        pen.clear()
        pen.write("Play A: {}   Player B: {}".format(scoreA, scoreB), align="center", font=("Courỉer", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        scoreB += 1
        pen.clear()
        pen.write("Play A: {}   Player B: {}".format(scoreA,scoreB), align="center", font=("Courỉer", 24, "normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    #Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor()<350) and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40) :
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor()> -350) and (ball.ycor() > paddleA.ycor() - 40 and ball.ycor() < paddleA.ycor() + 40) :
        ball.setx(-340)
        ball.dx *= -1
