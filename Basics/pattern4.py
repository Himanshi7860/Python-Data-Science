from turtle import*

speed('fastest')
pensize(1)
penup()
goto(-500,0)
pendown()
lt(75)
spikes = 10
while spikes > 0:
    fd(100)
    rt(150)
    fd(100)
    lt(150)
    spikes -= 1

hideturtle()
mainloop()