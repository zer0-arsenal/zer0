def center_circle(target,r):
    target.penup()
    target.forward(r)
    target.left(90)
    target.pendown()
    target.circle(r)
    target.left(90)
    target.penup()
    target.forward(r)
    target.pendown()

