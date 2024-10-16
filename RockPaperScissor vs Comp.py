import random

def game(comp, you):
    if comp == you:
        return None
    
    elif comp == "r":
        if you == "p":
            return True
        else :
            return False

    elif comp == "p":
        if you == "s":
            return True
        else:
            return False

    elif comp == "s":
        if you == "r":
            return True
        else:
            return False
        
print("\n\n\t\t##### W E L C O M E   T O   T H E   R O C K - P A P E R - S C I S S O R   G A M E #####\n")
p = input("\nEnter the name of Player : ")
n = int(input("Enter the number of round you wanna play : "))
cw = 0
pw = 0

for i in range(n):
    print("\n\t\tROUND : ",(i+1))
    print("Rock(r) Paper(p) Scissor(s)")
    s = input("Enter your choice : ")

    # while(s != 'p' or s != 's' or s != 'r' ):
    #     print("\n***ERROR 404 PLZ ENTER THE CORRECT CHOICE***\n")
    #     s = input("Enter your choice : ")
        
    c = random.randint(1,3)
    if c == 1:
        c = 'r'
    elif c == 2:
        c = 'p'
    elif c == 3:
        c = 's'
    print("Computer's choice is : ",c)
    win = game(c,s)

    if win == None:
        print("\n*****\tThis Round is a Tie\t*****\n")
    elif win:
        print("\n*****\tYou Win This Round\t*****\n")
        pw = pw + 1
    else :
        print("\n*****\tYou Lost this Round\t*****\n")
        cw = cw + 1

print(f"{p}'s Score is : {pw}\nComputer's Score is : {cw}")

if cw>pw:
    print("\n\n**********  G A M E   O V E R  *********\n\n")
elif pw>cw:
    print("\n\n********   Y O U   W I N   T H E   G A M E   *********\n\n")
else:
    print("\n\n********   T H E   G A M E   I S   T I E   *********\n\n")