import turtle




def draw_square (some_turtle):
    Turns = 0 
    while (Turns < 4):
        some_turtle.forward(100)
        some_turtle.right(90)
        Turns = Turns + 1
        
def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    #create turtle
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(7)
    Turns = 0 
    
    circle = 0;
    while ( circle < 36 ):
        draw_square(brad)
        brad.right(10)
        
    #for i in range (1,37) :
        #draw_square(brad)
        #brad.right(10)

        
    #ceate circle
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    window.exitonclick()


draw_art()
