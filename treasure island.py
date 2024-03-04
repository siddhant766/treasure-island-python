print("Hello ! , welcome to the treasure island \nYour mission is to find the treasure !!!")
a=str(input("choose a direction L or R : "))
if a=='L':
    print("Go to next challange")
else:
    print("Game Over")
b=str(input("what you will do wait or swim : "))
if b=="wait":
    print("next task")
else:
    print("game over")
c=str(input("which door ?\nRed\nYellow\nBlue\n:"))
if c=='Yellow':
    print("YOU WIN !!")
else:
    print("Game Over")
    #try and modify this programe