import turtle

screen = turtle.Screen()
screen.title("U.S. states Game")

image = "blank_states_img.gif"
screen.addshape(image)   # creat new shape
turtle.shape(image)     # use the shape we created

'''
this code is to get the x and y coordinate of the states but no need for that because it's already found and stored in the file
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
'''
import pandas
data = pandas.read_csv("50_states.csv")
df = pandas.DataFrame(data)
states = data["state"]
score = 0
gussed_states = []
missed = []
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="what's another states name?")
    if answer_state == "exit":
        missed = [st for st in states if not st in gussed_states]
        # for state in states:
        #     if not state in gussed_states:
        #         missed.append(state)
        missed = pandas.DataFrame(missed)
        missed.to_csv("missing_states.csv")
        break
    for state in states:
        if answer_state.lower() == state.lower() and not state in gussed_states:
            gussed_states.append(state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            row = data[data["state"] == state]
            t.goto(int(row.x), int(row.y))
            t.write(state)
            score += 1


# screen.exitonclick()