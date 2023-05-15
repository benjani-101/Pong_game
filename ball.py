from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.paddle_bounce_state = 0
        self.wall_bounce_state = 0

    def bounce_paddle(self, paddle):
        if self.paddle_bounce_state > 1:
            distance_from_center = paddle.ycor() - self.ycor()
            # adjust angle based on point of contact with paddle
            angle_adjust = (distance_from_center/35) * 45
            if self.heading() > 270 or self.heading() < 90:
                new_heading = 180 + angle_adjust
            else:
                new_heading = 0 - angle_adjust
                if new_heading < 0:
                    new_heading = 360 + new_heading


            self.setheading(new_heading)
            # reset bounce state to ensure only one bounce recorded per contact
            self.paddle_bounce_state = 0

    def at_paddle_line(self, paddle):
        # get absolute value of distance from line
        distance_from_line = abs(paddle.xcor() - self.xcor())
        if distance_from_line < 4.9:
            return True
        else:
            return False

    def wall_bounce(self):
        if self.wall_bounce_state > 0:
            if self.heading() > 180:
                if self.heading() < 270:
                    incidence = self.heading() - 180
                    new_angle = 180 - incidence
                else:
                    incidence = 360 - self.heading()
                    new_angle = 0 + incidence

            else:
                if self.heading() < 90:
                    incidence = 180 - self.heading()
                    new_angle = 180 + incidence
                else:
                    incidence = self.heading()
                    new_angle = 360 - incidence
            self.setheading(new_angle)
            self.wall_bounce_state = 0






