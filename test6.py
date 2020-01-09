import turtle
t = turtle.Pen()
colors = ['red', "yellow", "blue", 'orange',"green", 'purple' ,'pink']
turtle.bgcolor("black")
#sides=6
sides=eval(input('Enter a number:'))

for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/200)
    t.left(90)
