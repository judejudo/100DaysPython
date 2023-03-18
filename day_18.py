import turtle as t
import random 

# # for i in range(4):
# #     tim.forward(100)
# #     tim.right(90)

# # def draw_shape(num_sides):
# #     angle =  360 / num_sides
# #     for i in range (num_sides):
# #         tim.forward(100)
# #         tim.right(angle)
        


# # for shape_side_n in  range(3,11):
# #     tim.color(random.choice(colours))
# #     draw_shape(shape_side_n)


# tim = t.Turtle()
# tim.speed('fast')
t.colormode(255)

# tim.width(5)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color1 = (r, g, b)
#     return random_color1

# # move = True
# # directions = [0,90,180,360]
# # while  move == True:
# #     tim.color(random_color())
# #     tim.setheading(random.choice(directions))
# #     tim.forward(10)


# for i in range(36):
#     tim.speed('fastest')
#     tim.color(random_color())
#     tim.circle(60)
#     tim.left(10)





# screen = t.Screen()
# screen.exitonclick()

# import colorgram as cg
# rgb_colors = []
# colors = cg.extract('hirst spot painting.jpeg' , 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

# colour_list = [ (1, 9, 30), (229, 235, 242), (239, 232, 238), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218)]

# tim = t.Turtle()

# tim.up()
# tim.setx(-300)
# tim.sety(-200)
# def create_dot_move(): 
#     tim.speed('fast')
#     tim.color(random.choice(colour_list))
#     tim.dot(20)
    
# def hit_row():
#     for i in range(10):
#         create_dot_move()
#         tim.forward(50)
#         tim.penup()
#         if i == 9:
#             create_dot_move()



# def turn_left(): 
#     tim.left(90)
#     tim.penup()
#     tim.forward(50)
#     tim.left(90)

# def turn_right(): 
#     tim.right(90)
#     tim.penup()
#     tim.forward(50)
#     tim.right(90)

# for i in range(5):
#     hit_row()  
#     turn_left()
#     hit_row()
#     turn_right()


screen = t.Screen()
screen.exitonclick()