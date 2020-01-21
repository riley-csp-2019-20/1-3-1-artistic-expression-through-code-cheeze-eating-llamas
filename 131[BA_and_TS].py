 # create turtles
import turtle as trtl 
player1 = trtl.Turtle()
franklin = trtl.Turtle()
drawer = trtl.Turtle()
mapper = trtl.Turtle()
writer = trtl.Turtle()
writer.speed(0)
mapper.speed(0)
mapper.ht()

#import random
import random 

# create color list to randomize colors 
rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]

def draw_maze():
    franklin.penup()
    franklin.goto(0,0)
    franklin.pendown()
    franklin.speed(0)
    franklin.pensize(5)
    franklin.ht()
    crash = trtl.Turtle()
    crash.shape("turtle")
    crash.speed(0)
    crash_size = 1
    crash.shapesize(crash_size)
    crash.pensize(crash_size)
    crash.ht()

    #import 
    # om function so you can randomize maze and colors
    import random

    #name parts of your maze
    wall_size = 20
    gap_size = 50
    counter = 25
    franklin.penup()

    #define a thing to make a barrier
    def make_barrier():
        franklin.left(90)
        franklin.forward(40)
        franklin.back(40)
        franklin.right(90)

    #define a thing to create door
    def make_door():
        franklin.penup()
        franklin.forward(gap_size)
        franklin.pendown()


    def go_down():
        global crash_size
        crash.setheading(90)
        crash.forward(5)
        rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
        color = random.choice(rad_colors)
        crash.pencolor(color)
        crash.stamp()
        color = random.choice(rad_colors)
        crash.color(color)


    # create maze and hide your moving turtle
    crash.ht()
    while (counter >= 0):
        if counter < 21:
            #randomize gap and wall placement
            door = random.randint(gap_size, wall_size - gap_size)
            barrier = random.randint(gap_size, wall_size - gap_size)

        #make colors to be randomly chosen have your walls become those colors
            rad_colors = ["silver", "dark grey", "grey", "dim grey", "black", "light slate grey", "slate grey", "navy", "medium blue", "deep sky blue", "dodger blue", "dark turquoise", "deep pink", "pale violet red", "hot pink", "dark magenta", "medium violet red", "dark violet", "indigo", "medium purple", "chocolate", "sienna", "maroon", "firebrick", "lime", "crimson", "brown", "orange red", "lawn green", "forest green", "dark sea green"]
            color = random.choice(rad_colors)
            franklin.pencolor(color)
            franklin.pendown()

        #based on what is drawn first draw things in a certain order
            if (door > barrier):
                franklin.forward(barrier)
        #make sure it doesnt draw barrier on the last or first few lines in maze
                if (counter <= 19):
                    if (counter >= 1):
                        make_barrier()
                franklin.forward(door-barrier)
        #make sure it doesn't create a door on the outer walls of the maze
                if (counter >= 4):
                    make_door()
                else:
                    franklin.forward(gap_size)
                franklin.forward(wall_size-door-gap_size)
                franklin.left(90)

        
            else:
                franklin.forward(door)
        #make sure it doesn't create a door on the outer walls of the maze
                if (counter >= 4):
                    make_door()
                else:
                    franklin.forward(gap_size)
                franklin.forward(barrier-door-gap_size)
        #make sure it doesnt draw barrier on the last or first few lines in maze
                if (counter <= 19):
                    if (counter >= 1):
                        make_barrier()
                franklin.forward(wall_size-barrier)
                franklin.left(90)
        wall_size += 20
        counter -= 1 

# create function to move turtle to start of the maze
def goto_maze_start():
    global franklin
    drawer.penup()
    xor = franklin.xcor()
    yor = franklin.ycor()
    drawer.goto(xor, yor)
    drawer.pendown()

#movement functions
def go_up():
    drawer.setheading(0)
    drawer.forward(20)

def go_down():
    drawer.setheading(270)
    drawer.forward(20)

def go_left():
    drawer.setheading(180)
    drawer.forward(20)

def go_right():
    drawer.setheading(90)
    drawer.forward(20)

# make map
# make finish circle
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.circle(50)
mapper.end_fill()

#make square 1
mapper.penup()
mapper.right(180)
mapper.forward(25)
mapper.back(75)

mapper.left(180)
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.end_fill()

#make square 2
mapper.penup()
mapper.right(180)
mapper.forward(25)
mapper.back(75)

mapper.left(180)
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.end_fill()

#make square 3
mapper.penup()
mapper.right(180)
mapper.forward(25)
mapper.back(75)

mapper.left(180)
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.end_fill()

#make square 4
mapper.penup()
mapper.right(90)
mapper.forward(0)
mapper.back(125)

mapper.left(180)
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.end_fill()

#make square 3
mapper.penup()
mapper.right(180)
mapper.forward(25)
mapper.back(75)

mapper.left(180)
color = random.choice(rad_colors)
mapper.fillcolor(color)
mapper.begin_fill()
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.left(90)
mapper.forward(75)
mapper.end_fill()

# put player_1 at start of board
xor = mapper.xcor()
yor = mapper.ycor()
player1.penup()
player1.goto(xor,yor)
player1.right(180)
player1.forward(75/2)
player1.right(90)
player1.forward(75/2)
player1.pendown()

# create your questions and answers and write on screen
questions = ["When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?", "Which Williams sister has won more Grand Slam titles?", "Which racer holds the record for the most Grand Prix wins?", "Which Jamaican runner is an 11-time world champion and holds the record in the 100 and 200-meter race?", "Which boxer was known as “The Greatest” and “The People’s Champion”?", "What year was the original model of the iPhone released"]
answers = ["A: 7   B: 6   C: 8    D: 5", "E: Serena Williams   F: Venus Williams    G: Josh Groban    H: Arthur Raddley", "I: Danica Patrick    J: Jimmie Johns    K: Michael Schumacher   L: Richard Petty", "M: Nesta Carter    N: Asafa Powell   O: Yohan Blake   P: Usain Bolt", "Q: Muhammad Ali   R: Rocky Balboa   S: The Rock   T: Big Bird", "U: 2007   V: 2006  W: 2009  X: 2005"]

# create outside of function so that numbers are coherent
current_question = random.randint(0,len(questions))

# define a function to ask a question
def ask_question():
    global questions
    global answers
    global current_question

    # choose random number for current question
    current_question = random.randint(0,len(answers)-1)

    #choose random question and answer and put it on screen
    writer.penup()
    writer.goto(-450,350)
    writer.write(questions[current_question], font=("Arial", 15))

    writer.goto(-450,325)
    writer.write(answers[current_question], font=("Arial", 15))

    writer.goto(-450,300)
    writer.write("input a letter in the terminal", font=("Arial", 15))


    #let input decide movement and answers
    answer = input("Enter here ")
    #if answer correct tell them and move turtle based on how many questions are left
    if (answer == "B" or answer == "b" or answer == "E" or answer == "e" or answer == "K" or answer == "k" or answer == "P" or answer == "p" or answer == "Q" or answer == "q" or answer == "U" or answer == "u"): 
        writer.goto(-250,-350)
        writer.write("CORRECT!", font=("Arial", 25))
        coolors = random.choice(rad_colors)
        player1.pencolor(coolors)
        coolors = random.choice(rad_colors)
        player1.color(coolors)
        if (len(answers) > 1):
            writer.goto(-250,-375)
            writer.write("press space to get another question", font=("Arial", 15))
            if (len(answers) == 6):
                player1.goto(-162.49999999999983,-87.49999999999983)

            elif (len(answers) == 5):
                player1.goto(-37.49999999999983,-87.4999999999998)

            elif (len(answers) == 4):
                player1.goto(87.50000000000017,-87.49999999999977)

            elif (len(answers) == 3):
                player1.goto(87.50000000000014,37.50000000000023)
        
            else:
                player1.goto(0,0)
                player1.clear()
                mapper.clear()
                writer.clear()
                player1.shape("circle")
                player1.shapesize(10)
                player1.clear()
                writer.goto(-250,-375)
                writer.write("YOU WIN!!!!", font=("Arial", 25))
                player1.color("Gold")
                draw_maze()
                goto_maze_start()
                player1.ht()
        questions.pop(current_question)
        answers.pop(current_question)

    else:
        writer.clear()
        writer.write("WRONG!", font=("Arial", 25))
        writer.goto(-250,-375)
        writer.write("press space to get another question", font=("Arial", 15))

current_question = random.randint(0,len(questions))
ask_question()


#create function to clear and ask another question when spacebar is pressed
def space_clear():
    global questions
    global answers
    global current_question
    writer.clear()
    ask_question()

#make space_clear happen when spacebar is clicked
wn = trtl.Screen() 
wn.onkeypress(space_clear, "space")
wn.onkeypress(go_up, "Right")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Up")
wn.onkeypress(go_left, "Left")
wn.listen()

#create a sustained turtle screen
wn.mainloop()