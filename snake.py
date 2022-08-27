from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
MOVE_UP = 90
MOVE_DOWN = 270
MOVE_LEFT = 180
MOVE_RIGHT = 0



class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]




    def create_snake(self):
        for position in START_POS:
            self.add_segment(position)

    def add_segment(self, position):
        t = Turtle(shape = "square")
        t.penup()
        t.color("white")
        t.goto(position)
        self.snake.append(t)


    def extend(self):
        self.add_segment(self.snake[-1].position())


    def move(self):
        for seg_num in range(len(self.snake) - 1 , 0 , -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)



    
    def up(self):
        if self.head.heading() != MOVE_DOWN:
            self.head.setheading(MOVE_UP)
        
    def down(self):
        if self.head.heading() != MOVE_UP:
            self.head.setheading(MOVE_DOWN)

    def left(self):
        if self.head.heading() != MOVE_RIGHT:
            self.head.setheading(MOVE_LEFT) 

    def right(self):
        if self.head.heading() != MOVE_LEFT:
            self.head.setheading(MOVE_RIGHT)      


