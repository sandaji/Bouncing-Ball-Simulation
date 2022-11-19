               
               # GROUP MEMBERS
# IJAMY VINCENT SANDAJI           PA101/G/1590/15
# MESHACK KIBET                   PA101/G/1570/15
# DANIEL NGESA                    PA101/G/1582/15
# CHRISTINE MWENDE MUTUA          PA101/G/8230/19
# BENSON MAINA kAMAU              PA101/G/7398/19    


import turtle
import random  

container=turtle.Screen()
container.bgcolor("black")
container.title("BOUNCING BALL")
container.tracer(0)

balls=[]

for _ in range(15):
    balls.append(turtle.Turtle())

colors = ["red", "green", "yellow", "blue", "pink","purple","white", "indigo", "orange"] 
size =["1","2","2.5","3","1.5"]  

# ball=turtle.Turtle()
for ball in balls:
    ball.shape("circle")
   
    ball.color(random.choice(colors))
    ball.penup()
    # ball.shapesize(random.choice(size))
    ball.speed(0)
    ball.width(10)
    x= random.randint(-300,300)
    y= random.randint(-300,300)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx=random.randint(-3,3)
    ball.da=random.randint(-5,5)

gravity= 0.01

while True:
    container.update()
    for ball in balls:
        ball.rt(ball.da)
        ball.dy -=gravity
        ball.sety(ball.ycor() + ball.dy)

        # changing the x cordinates + change in x speed
        ball.setx(ball.xcor() + ball.dx)

    # check for wall collision
        if ball.xcor() >300:
            ball.dx *=-1
            ball.da *= -1

        if ball.xcor() < -300:
            ball.dx *=-1  
            ball.da *= -1
 
    # check for a bounce
        if ball.ycor() < -300:
            ball.sety(-300)
            ball.dy *=-1
            ball.da *=-1

    # check for collision detection between balls
    for i in range(0, len(balls)):  
        for j in range( i+ 1, len(balls) ):
            #check for collision
            if balls[i].distance(balls[j]) <20:
                temp_dx = balls[i].dx
                temp_dy = balls[i].dy

                balls[i].dx = balls[j].dx
                balls[i].dy = balls[j].dy

                balls[j].dx = temp_dy
                balls[j].dy = temp_dx 

container.mainloop()