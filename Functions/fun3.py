from turtle import*

def shape(side, size):
    for i in range(side):
        fd(size)
        lt(360/side)
def pattern(side, size, color):
    pencolor("white")
    pensize(5)
    fillcolor(color)
    begin_fill()
    shape(side, size)
    end_fill()
speed('fastest')
bgcolor('black')
for i in range(11, 3, -1):
    pattern(i, 50, 'red')
    fd(200)
    lt(360//8)

hideturtle()
mainloop()
