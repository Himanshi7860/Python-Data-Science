from turtle import*

pencolor('blue')
pensize(5)
speed('fastest')

for i in range(6):
    fd(100)
    lt(360/6)
    for i in range(3):
        fd(150)
        lt(360/3)

hideturtle()
mainloop()