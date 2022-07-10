from turtle import *

color('black', 'red')
shape('turtle')
begin_fill()
i = 0
r = 100

while i < 10:
    circle(r, 360, 10)
    r = r - 10
    i = i + 1

i = 0
r = 100
while i < 10:
    circle(-r, 360, 10)
    r = r - 10
    i = i + 1
end_fill()
begin_fill()
color('black', 'green')
forward(200)
circle(100)
left(180)
forward(400)
circle(100)
end_fill()

begin_fill()
color('black', 'brown')
circle(-100)
left(180)
forward(400)
circle(-100)
end_fill()
done()
