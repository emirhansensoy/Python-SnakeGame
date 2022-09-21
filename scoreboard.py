from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file_r:
            self.high_score = int(file_r.read())
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.setposition(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def update_high_score(self):
        with open("data.txt", "w") as file_w:
            file_w.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.update_high_score()
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.color("red")
    #    self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
