import turtle

p = turtle.Pen()

while True:
    choices = input('start?( y or n )')
    if choices == 'y':
        for a in range(4):
            p.forward(100)
            p.left(90)
        turtle.done
    elif choices == 'n':
        exit()
    else:
        pass