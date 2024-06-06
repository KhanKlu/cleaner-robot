# Program v turtl graphic na prototyp robota na upratovanie v plochej miestnosti(odpad, oblečenie, nepoužite jedlo, riady )

import turtle
import random

robot_speed = 1
all_items = 20


class Box(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.speed(0)
        self.goto(x, y)
        self.count = 0
        self.count_text = turtle.Turtle()
        self.count_text.penup()
        self.count_text.hideturtle()
        self.update_count_text()

    def update_count_text(self):
        self.count_text.clear()
        self.count_text.goto(self.xcor(), self.ycor())
        self.count_text.write(self.count, align="center", font=("Arial", 12, "normal"))


class Robot(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("arrow")
        self.color("black")
        self.penup()
        self.goto(x, y)


    def go_to_item(self, item):
        self.goto(item.xcor(), item.ycor())
    
    def carry_to_box(self, box):
        self.goto(box.xcor(), box.ycor())
        box.count += 1
        box.update_count_text()
        


class Item(turtle.Turtle):
    def __init__(self, color, x, y):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.speed(1000000)
        self.goto(x, y)
        
    def delete(self):
        self.hideturtle()

# Vytvorenie okna pre grafiku
wn = turtle.Screen()
wn.title("Cleaner Bot")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Vytvorenie hracej plochy
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("black")
border_pen.penup()
border_pen.setposition(-250, -250)
border_pen.pendown()
border_pen.pensize(2)
for side in range(4):
    border_pen.fd(500)
    border_pen.lt(90)
border_pen.hideturtle()

# Vytvorenie troch debničiek
box1 = Box("blue", 230, -230)
box2 = Box("red", 230, -190)
box3 = Box("green", 230, -150)

colors = ["blue", "red", "green"]
num_items1 = random.randint(1,all_items)
items = []

for _ in range(num_items1):
    color = random.choice(colors)
    x = random.randint(-245,245)
    y = random.randint(-245, 245)

    item = Item(color, x, y)
    items.append(item)
    item.speed(50000)

#vytvorenie robota
robot = Robot(0,0)
robot.speed(robot_speed)

for item in items[:]:
    robot.go_to_item(item)
    item_color = item.color()[0]
    if item_color == "blue":
        robot.carry_to_box(box1)
    elif item_color == "red":
        robot.carry_to_box(box2)
    elif item_color == "green":
        robot.carry_to_box(box3)
    item.delete()
    items.remove(item)

# Zastavenie okna
wn.mainloop()