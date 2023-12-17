from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0,260)
        self.score = 0
        self.write(f'Score: {self.score} ' , True,align='center' , font=("arial",22,"normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0,260)
        self.write(f'Score: {self.score} ' , True,align='center' , font=("arial",22,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over.' , True , align='center', font=("arial",22,"normal"))
        