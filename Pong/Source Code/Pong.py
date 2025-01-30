# Pong Game

import turtle
import winsound

win = turtle.Screen()
win.title = ("Pong by @AikonDev")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)

# Score
scoreOne = 0
scoreTwo = 0

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.0625
ball.dy = -0.0625

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0  Player Two: 0", align="center", font=("Courier", 24, "normal"))



# Function
def paddleA_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleA_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleB_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleB_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keybinds
win.listen()
win.onkeypress(paddleA_up, "w")
win.onkeypress(paddleA_down, "s")

win.onkeypress(paddleB_up, "Up")
win.onkeypress(paddleB_down, "Down")

# Main Game Loop
while True:
    win.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Boundary Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Wall.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Wall.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreOne += 1
        pen.clear()
        pen.write("Player One: {}  Player Two: {}".format(scoreOne, scoreTwo), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Score.wav", winsound.SND_ASYNC)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreTwo += 1
        pen.clear()
        pen.write("Player One: {}  Player Two: {}".format(scoreOne, scoreTwo), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Score.wav", winsound.SND_ASYNC)


    # Paddle & Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Paddle.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("C:\\Users\\Ayaan\\Documents\\Python Projects\\Pong\\Source Code\\Assets\\SoundFX\\Paddle.wav", winsound.SND_ASYNC)

    # AI Player
    if paddleB.ycor() < ball.ycor() and abs(paddleB.ycor() - ball.ycor()) > 65:
        paddleB_up()

    elif paddleB.ycor() > ball.ycor() and abs(paddleB.ycor() - ball.ycor()) > 65:
        paddleB_down()