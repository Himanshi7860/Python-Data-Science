from turtle import*

def square(size,color):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size*5)
        lt(90)
    end_fill()

speed('fastest')
colors =['red', 'blue', 'green']
for i in range(6):
    square(60, colors[i%3])
    lt(360//6)

hideturtle()
mainloop()