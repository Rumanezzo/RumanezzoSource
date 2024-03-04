import turtle as t

t0 = t.Turtle()
t0.shape('triangle')

s0 = t.Screen()
s0.mode('logo')

s0.title('Это мои эксперименты')
t0.speed(0)

s0.setup(0.99, 0.9, 0, 0)
s0.bgcolor('grey')
#-------------------------------------------------------------------------------------------

def branch(length, angle, flag=0):
    if flag:
        t0.rt(180)
    for i in range(180 // abs(angle)):    
        t0.fd(length)
        t0.rt(angle)
        t0.shapesize(0.5 + 0.2 * i)
        t0.stamp()
    t0.ht()
    t0.pu()
    t0.home()
    t0.pd()
    
for i in range(5):
    branch(50 - 5 * i, 10 + 2 * i)
    branch(50 - 5 * i, 10 + 2 * i, 1)
    
    branch(50 - 5 * i, -10 - 2 * i)
    branch(50 - 5 * i, -10 - 2 * i, 1)

t0.color('red')
t0.width(10)
t0.circle(80)
t0.circle(-80)
t0.pu()
t0.color('green')
t0.goto(35, 0)
t0.rt(30)
t0.stamp()
t0.goto(-35, 0)
t0.lt(60)
t0.stamp()

#-------------------------------------------------------------------------------------------
s0.title('Работа завершена!')
s0.exitonclick()