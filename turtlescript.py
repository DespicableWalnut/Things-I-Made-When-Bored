import turtle

def theturtle():
    
    t = turtle.Turtle()

    def color(cmd):
        color = cmd[6:].strip()
        try:
            t.color(color)
        except:
            print("That color does not exist")
            
    def right(cmd):
        move = cmd[3:]
        t.right(int(move))

    def left(cmd):
        move = cmd[3:]
        t.left(int(move))

    def forward(cmd):
        move = cmd[3:]
        t.forward(int(move))

    def backward(cmd):
        move = cmd[3:]
        t.back(int(move))

    def game():
        print("forwards: fw [pixels], backwards: bw [pixels], left: lt [pixels], right: rt [pixels], change the color: color [pixels]")
        while True:
            userask = input(": ")

            if "rt" in userask:
                right(userask)
            elif "lt" in userask:
                left(userask)
            elif "fw" in userask:
                forward(userask)
            elif "bw" in userask:
                backward(userask)
            elif "color" in userask:
                color(userask)
    game()
        
if __name__ == '__main__':
    theturtle()
