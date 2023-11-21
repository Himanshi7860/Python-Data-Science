from turtle import *

speed('slowest')
pensize(2)

colors = ['red','blue','yellow','green','orange','purple']

for i in range(6):
    write(colors[i], font=('Arial',16,'bold'))
    pencolor(colors[i])
    fd(120)
    lt(360/6)

hideturtle()
mainloop()