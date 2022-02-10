# encoding: utf-8
"""
@author: Zeep
@file: olympic.py
@time: 2022/2/9 22:28
@desc:
"""

import turtle as t

GOLDEN = (246, 229, 66)


def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def circle(angle, radius, degree):
    t.setheading(angle)
    t.circle(radius, degree)


def click():
    wn = t.Screen()

    def fxn(x, y):
        t.goto(x, y)
        print(str(x) + ", " + str(y))

    # onclick action
    wn.onclick(fxn)
    wn.mainloop()


class Shuey:
    def __init__(self, x, y):
        line_color = "black"
        line_size = 1
        t.pensize(line_size)
        t.pencolor(line_color)
        self.head(x, y)
        self.grown(x, y, line_color, line_size)
        self.hat(x, y)
        self.right_arm(x, y)
        self.left_arm(x, y)
        self.body(x, y)
        self.face(x, y, line_color, line_size)
        self.tie(x, y)
        self.belly(x, y, line_color, line_size)
        self.logo(x, y, line_color)

    @classmethod
    def grown(cls, x, y, line_color, line_size):
        t.pencolor("yellow")
        t.pensize(3)
        goto(18 + x, 270 + y)
        t.setheading(90)
        t.circle(15, 60)
        t.circle(-10, 180)
        t.setheading(45)
        t.circle(-40, 120)
        t.setheading(0)
        t.circle(-10, 180)
        t.setheading(-110)
        t.circle(-15, 60)
        t.setheading(140)
        t.circle(70, 50)
        goto(40 + x, 270 + y)
        t.setheading(90)
        t.circle(12, 80)
        goto(60 + x, 262 + y)
        t.setheading(70)
        t.circle(-12, 80)
        t.pensize(line_size)
        t.pencolor(line_color)

    @classmethod
    def head(cls, x, y):
        t.fillcolor("red")
        goto(18 + x, 266 + y)
        t.begin_fill()
        goto(-103 + x, -118 + y)
        circle(160, -202, 75)  # 1
        circle(76, -220, 60)  # 2

        circle(22, -220, 27)  # 3
        circle(10, -70, 50)  # 4
        circle(-22, -220, 27)  # 5

        t.circle(-260, 40)  # 6
        circle(-99, -198, 56)  # 7
        t.setheading(179)
        t.goto(-103 + x, -118 + y)
        t.end_fill()

    @classmethod
    def hat(cls, x, y):
        t.fillcolor("white")
        t.begin_fill()
        goto(-82.32 + x, 247.68 + y)
        t.setheading(16.0)
        circle(22, -220, 27)  # 1
        circle(10, -70, 50)  # 2
        circle(-22, -220, 27)  # 3
        circle(142.0, 100, 45)  # 4
        circle(137.0, 140, 60)  # 5
        circle(149, 60, 32)  # 6
        t.end_fill()

    @classmethod
    def body(cls, x, y):
        # body
        goto(-103 + x, -118 + y)
        t.fillcolor("red")
        t.begin_fill()
        t.setheading(240)
        t.circle(140, 70)
        t.goto(-90 + x, -290 + y)
        t.setheading(-45)
        t.circle(68, 66)
        t.goto(-12 + x, -292 + y)
        t.setheading(-90)
        t.circle(25, 80)
        t.goto(45 + x, -318 + y)
        t.setheading(8)
        t.circle(30, 80)
        t.setheading(48)
        t.circle(120, 35)
        t.setheading(120)
        t.circle(-120, 40)
        t.setheading(10)
        t.circle(80, 20)
        t.goto(113.47 + x, -126.16 + y)
        t.goto(-103 + x, -118 + y)
        t.end_fill()

    @classmethod
    def right_arm(cls, x, y):
        goto(-170 + x, -79 + y)
        t.fillcolor("red")
        t.begin_fill()
        t.setheading(200)
        t.circle(32, 120)
        t.circle(124, 32)
        t.goto(-103 + x, -118 + y)
        t.goto(-170 + x, -79 + y)
        t.end_fill()

    @classmethod
    def left_arm(cls, x, y):
        # left arm
        goto(100.73 + x, -223.67 + y)
        t.fillcolor("red")
        t.begin_fill()
        t.setheading(-20)
        t.circle(30, 100)
        t.circle(70, 64)
        t.goto(64.0 + x, -147.0 + y)
        t.goto(100.73 + x, -223.67 + y)
        t.end_fill()

    @classmethod
    def cheek(cls, x, y, loc, c, line_color, line_size):
        goto(loc[0] + x, loc[1] + y)
        t.pencolor((255, 240, 247))
        t.pensize(5)
        t.fillcolor((255, 183, 197))
        t.begin_fill()
        circle(*c)
        t.end_fill()
        t.pensize(line_size)
        t.pencolor(line_color)

    @classmethod
    def face(cls, x, y, line_color, line_size):
        t.pencolor("white")
        goto(-168 + x, 7 + y)
        t.fillcolor("white")
        t.begin_fill()
        circle(194, -45, 145)
        circle(110, -42, 125)
        circle(60, -58, 106)
        circle(22, -46, 106)
        circle(-80, 30, 106)
        circle(22, -50, 130)
        circle(-38, -32, 200)
        circle(-150, -188, 73)
        t.end_fill()
        goto(-147.0 + x, 86.0 + y)
        t.fillcolor("black")
        t.begin_fill()
        circle(0, -10, 360)
        t.end_fill()
        goto(2.0 + x, 50.0 + y)
        t.fillcolor("black")
        t.begin_fill()
        circle(0, -10, 360)
        t.end_fill()

        cls.cheek(x, y, (-193.0, 78.0), (0, -20, 360), line_color, line_size)
        cls.cheek(x, y, (73.0, 25.0), (0, -20, 360), line_color, line_size)

        t.pensize(line_size)
        t.pencolor(line_color)

    @classmethod
    def tie(cls, x, y):
        goto(-103 + x, -118 + y)
        t.fillcolor(GOLDEN)
        t.begin_fill()
        t.goto(-110.0 + x, -135.0 + y)
        circle(-16, 400, 28)
        circle(10, 80, 20)
        t.goto(113.47 + x, -126.16 + y)
        t.goto(-103 + x, -118 + y)
        t.end_fill()

        goto(-97.0 + x, -139.0 + y)
        t.fillcolor(GOLDEN)
        t.begin_fill()
        t.goto(-111.0 + x, -188.0 + y)
        t.goto(-93.0 + x, -193.0 + y)
        t.goto(-83.0 + x, -142.0 + y)
        t.goto(-97.0 + x, -139.0 + y)
        t.end_fill()

    @classmethod
    def belly(cls, x, y, line_color, line_size):
        t.pencolor(GOLDEN)
        t.pensize(2)
        t.fillcolor("white")
        t.begin_fill()
        goto(-26.0 + x, -159.0 + y)
        circle(0, -55, 360)
        t.end_fill()
        t.pensize(line_size)
        t.pencolor(line_color)

    @classmethod
    def logo(cls, x, y, line_color):
        import cv2
        t.getscreen().colormode(255)
        img = cv2.imread('logo.png')
        width, height = (70, 70)
        img = cv2.resize(img, (width, height))
        sx = -26 - width / 2
        sy = -214 + height / 2
        goto(sx + x, sy + y)
        t.tracer(200)
        for row, col in enumerate(img):
            for pixel in col:
                r, g, b = pixel
                if r == 0 and g == 0 and b == 0:
                    r, g, b = (255, 255, 255)
                t.pencolor((r, g, b))
                t.fd(1)
            goto(sx + x, sy - row - 1 + y)
        goto(-66 + x, -229 + y)
        t.pencolor("black")
        t.write("Shuey Rhon Rhon", font=('Arial', 8, 'bold italic'))
        t.pencolor(line_color)


class Bing:
    def __init__(self, x, y):
        # 左手
        t.penup()
        t.goto(176 + x, 111 + y)
        t.pencolor("lightgray")
        t.pensize(3)
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(80)
        t.circle(-45, 210)
        # t.circle(-290, 25)
        t.circle(-290, 18)
        t.end_fill()

        # 左手内
        t.penup()
        t.goto(182 + x, 95 + y)
        t.pencolor("black")
        t.pensize(1)
        t.fillcolor("black")
        t.begin_fill()
        t.setheading(95)
        t.pendown()
        t.circle(-37, 160)
        t.circle(-20, 50)
        t.circle(-200, 30)
        t.end_fill()
        # 轮廓
        # 头顶
        t.penup()
        t.goto(-73 + x, 230 + y)
        t.pencolor("lightgray")
        t.pensize(3)
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(20)
        t.circle(-250, 35)
        # 左耳
        t.setheading(50)
        t.circle(-42, 180)
        # 左侧
        t.setheading(-50)
        t.circle(-190, 30)
        t.circle(-320, 45)
        # 左腿
        t.circle(120, 30)
        t.circle(200, 12)
        t.circle(-18, 85)
        t.circle(-180, 23)
        t.circle(-20, 110)
        t.circle(15, 115)
        t.circle(100, 12)
        # 右腿
        t.circle(15, 120)
        t.circle(-15, 110)
        t.circle(-150, 30)
        t.circle(-15, 70)
        t.circle(-150, 10)
        t.circle(200, 35)
        t.circle(-150, 20)
        # 右手
        t.setheading(-120)
        t.circle(50, 30)
        t.circle(-35, 200)
        t.circle(-300, 23)
        # 右侧
        t.setheading(86)
        t.circle(-300, 26)
        # 右耳
        t.setheading(122)
        t.circle(-53, 160)
        t.end_fill()

        # 右耳内
        t.penup()
        t.goto(-130 + x, 180 + y)
        t.pencolor("black")
        t.pensize(1)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(120)
        t.circle(-28, 160)
        t.setheading(210)
        t.circle(150, 20)
        t.end_fill()

        # 左耳内
        t.penup()
        t.goto(90 + x, 230 + y)
        t.setheading(40)
        t.begin_fill()
        t.pendown()
        t.circle(-30, 170)
        t.setheading(125)
        t.circle(150, 23)
        t.end_fill()

        # 右手内
        t.penup()
        t.goto(-180 + x, -55 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.setheading(-120)
        t.pendown()
        t.circle(50, 30)
        t.circle(-27, 200)
        t.circle(-300, 20)
        t.setheading(-90)
        t.circle(300, 14)
        t.end_fill()

        # 左腿内
        t.penup()
        t.goto(108 + x, -168 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(-115)
        t.circle(110, 15)
        t.circle(200, 10)
        t.circle(-18, 80)
        t.circle(-180, 13)
        t.circle(-20, 90)
        t.circle(15, 60)
        t.setheading(42)
        t.circle(-200, 29)
        t.end_fill()
        # 右腿内
        t.penup()
        t.goto(-38 + x, -210 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(-155)
        t.circle(15, 100)
        t.circle(-10, 110)
        t.circle(-100, 30)
        t.circle(-15, 65)
        t.circle(-100, 10)
        t.circle(200, 15)
        t.setheading(-14)
        t.circle(-200, 27)
        t.end_fill()

        # 右眼
        # 眼圈
        t.penup()
        t.goto(-64 + x, 120 + y)
        t.begin_fill()
        t.pendown()
        t.setheading(40)
        t.circle(-35, 152)
        t.circle(-100, 50)
        t.circle(-35, 130)
        t.circle(-100, 50)
        t.end_fill()
        # 眼珠
        t.penup()
        t.goto(-47 + x, 55 + y)
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(25, 360)
        t.end_fill()
        t.penup()
        t.goto(-45 + x, 62 + y)
        t.pencolor("darkslategray")
        t.fillcolor("darkslategray")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(19, 360)
        t.end_fill()
        t.penup()
        t.goto(-45 + x, 68 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(10, 360)
        t.end_fill()
        t.penup()
        t.goto(-47 + x, 86 + y)
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(5, 360)
        t.end_fill()

        # 左眼
        # 眼圈
        t.penup()
        t.goto(51 + x, 82 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(120)
        t.circle(-32, 152)
        t.circle(-100, 55)
        t.circle(-25, 120)
        t.circle(-120, 45)
        t.end_fill()
        # 眼珠
        t.penup()
        t.goto(79 + x, 60 + y)
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(24, 360)
        t.end_fill()
        t.penup()
        t.goto(79 + x, 64 + y)
        t.pencolor("darkslategray")
        t.fillcolor("darkslategray")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(19, 360)
        t.end_fill()
        t.penup()
        t.goto(79 + x, 70 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(10, 360)
        t.end_fill()
        t.penup()
        t.goto(79 + x, 88 + y)
        t.pencolor("white")
        t.fillcolor("white")
        t.begin_fill()
        t.pendown()
        t.setheading(0)
        t.circle(5, 360)
        t.end_fill()

        # 鼻子
        t.penup()
        t.goto(37 + x, 80 + y)
        t.fillcolor("black")
        t.begin_fill()
        t.pendown()
        t.circle(-8, 130)
        t.circle(-22, 100)
        t.circle(-8, 130)
        t.end_fill()

        # 嘴
        t.penup()
        t.goto(-15 + x, 48 + y)
        t.setheading(-36)
        t.begin_fill()
        t.pendown()
        t.circle(60, 70)
        t.setheading(-132)
        t.circle(-45, 100)
        t.end_fill()

        # 彩虹圈
        t.penup()
        t.goto(-135 + x, 120 + y)
        t.pensize(5)
        t.pencolor("cyan")
        t.pendown()
        t.setheading(60)
        t.circle(-165, 150)
        t.circle(-130, 78)
        t.circle(-250, 30)
        t.circle(-138, 105)
        t.penup()
        t.goto(-131 + x, 116 + y)
        t.pencolor("slateblue")
        t.pendown()
        t.setheading(60)
        t.circle(-160, 144)
        t.circle(-120, 78)
        t.circle(-242, 30)
        t.circle(-135, 105)
        t.penup()
        t.goto(-127 + x, 112 + y)
        t.pencolor("orangered")
        t.pendown()
        t.setheading(60)
        t.circle(-155, 136)
        t.circle(-116, 86)
        t.circle(-220, 30)
        t.circle(-134, 103)
        t.penup()
        t.goto(-123 + x, 108 + y)
        t.pencolor("gold")
        t.pendown()
        t.setheading(60)
        t.circle(-150, 136)
        t.circle(-104, 86)
        t.circle(-220, 30)
        t.circle(-126, 102)
        t.penup()
        t.goto(-120 + x, 104 + y)
        t.pencolor("greenyellow")
        t.pendown()
        t.setheading(60)
        t.circle(-145, 136)
        t.circle(-90, 83)
        t.circle(-220, 30)
        t.circle(-120, 100)
        t.penup()

        # 爱心
        t.penup()
        t.goto(220 + x, 115 + y)
        t.pencolor("brown")
        t.pensize(1)
        t.fillcolor("brown")
        t.begin_fill()
        t.pendown()
        t.setheading(36)
        t.circle(-8, 180)
        t.circle(-60, 24)
        t.setheading(110)
        t.circle(-60, 24)
        t.circle(-8, 180)
        t.end_fill()

        t.speed(20)
        # 五环
        t.penup()
        t.pensize(3)
        pencolor = ['blue', 'black', 'red', 'yellow', 'green']  # 列表存储画笔颜色
        xx, yy = (-30, -170)
        r = 10
        for i in range(5):
            if i == 3:
                x += r
                y -= r
            if i < 3:
                goto(xx + i * 20 + x, yy + y)
                t.pencolor(pencolor[i])
                t.circle(10)
            else:
                goto(xx + (i - 3) * 20 + x, yy + y)
                t.pencolor(pencolor[i])
                t.circle(10)

        t.penup()
        t.pencolor("black")
        t.goto(-70 + x, -150 + y)
        t.write("Bing Dwen Dwen", font=('Arial', 14, 'bold italic'))


def main():
    t.setup(1.0, 1.0)  # 设置窗口大小
    t.colormode(255)
    t.screensize(800, 800)
    t.speed(1000)

    Bing(-320, 15)
    Shuey(320, -15)

    ts = t.getscreen()
    ts.getcanvas().postscript(file="olympic.eps")

    t.hideturtle()
    t.done()


if __name__ == '__main__':
    main()
