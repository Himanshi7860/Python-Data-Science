from turtle import *

speed('slowest')
pensize(1)

speed('slowest')
pensize(1)
penup()
goto(-500,0)
pendown()
lt(60)
for i in range(10):
    fd(120)
    rt(120)
    fd(100)
    lt(120)

hideturtle()
mainloop()
