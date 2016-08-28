import turtle
#Haha TTpro
def draw_triangle(the_turtle,length,ori,recursion):
    recursion=recursion+1
    Hamza = the_turtle

    for i in range(0,3):
        if(recursion<4):
        #if (0):
            Hamza.forward(length/2)
            Hamza.left(120)
            draw_triangle(Hamza,length/2,0,recursion)
            Hamza.right(120)
            Hamza.forward(length/2)
        else:
            Hamza.forward(length)
        if (ori==1):
            Hamza.left(120)
        else:
            Hamza.right(120)

Hamza = turtle.Turtle() # init
Hamza.speed(10) # speed = 1 to slow turtle down
Hamza.color("yellow","green") # set color5
Hamza.shape("turtle") # set shape to a turtle
background = turtle.Screen()  # create background
background.bgcolor("red")     # set background color to red


draw_triangle(Hamza,200,1,0)

#Hamza.forward(100)
#Hamza.left(120)
#draw_triangle(Hamza,100,0,0)
#Hamza.right(120)

background.exitonclick()      # click anywhere to close background
