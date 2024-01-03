import turtle 
import time
import random

score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Cupcake Sanke")
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

cupcake = turtle.Turtle()
cupcake.speed(0)
cupcake.shape("circle")
cupcake.color("Blue")
cupcake.penup()
cupcake.goto(0,100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(-295,0)
pen.write("Use the arrow keys onyour keyboard \nto controlthesanke.\n\n\
          Eat the cupcake to increase the \nscore and the length of the snake.\n\n\
          The game over if the sanke head \nhit anywhere on its body",
          align="left",font = ("Courier,20,normal"))
time.sleep(10)

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"
        
def go_left():
    if head.direction != "right":
        head.direction = "left"
        
def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
      y = head.ycor()
      head.sety(y + 10)
      
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 10)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 10)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 10)
        
wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_left,"Left")
wn.onkeypress(go_right,"Right")

while True:
    wn.update()
    
    if head.distance(cupcake) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        cupcake.goto(x,y)
        
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        score += 10
        
        if score > high_score:
            high_score = score
            
    if head.xcor()> 300:
        head.setx(-300)
    if head.xcor()<-300:
        head.setx(300)
    if head.ycor()> 300:
        head.sety(-300)
    if head.ycor()<-300:
        head.sety(300)
        
    for index in range(len(segments)-1 , 0 , -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)
        
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    move()
    
    for segment in segments:
        if segment.distance(head) < 10:
            pen.goto(0,-200)
            pen.write("You collided with your oun body! \nGame over",
                      align="Center",font=("courier",20,"normal"))
            time.sleep(5)
            pen.clear()
            
            head.goto(0,0)
            head.direction = "stop"
            
            for segment in segments:
                segment.goto(1000,1000)
                
            segments.clear()
            
            score = 0
  
    pen.goto(0,260)
    pen.clear()
    pen.write("Score: {}  High Score:  {}".format(score,high_score),align="center",font=("couier",20,"normal"))
    
    time.sleep(0.05)
    
wn.mainloop()
  
            