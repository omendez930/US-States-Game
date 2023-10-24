import pandas as pd
import turtle

screen = turtle.Screen()

screen.title('U.S. States Game')

img = 'blank_states_img.gif'
#add shape allows you to pull an image and generate it in turtle
screen.addshape(img)
turtle.shape(img)
data = pd.read_csv('50_states.csv')
state_list = data['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f'{len(guessed_states)}/50 correct ', prompt='What\'s a state name?').title()

    if answer == 'Exit':
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('States_to_learn.csv')
        break
    if answer in state_list:
        guessed_states.append(answer)
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()
        state_data = data[data['state'] == answer]
        turtle_state.goto(int(state_data.x), int(state_data.y))
        turtle_state.write(answer, align='center', font=('Arial', 8, 'normal'))

    #     print(answer)

# states_to_lear.csv



