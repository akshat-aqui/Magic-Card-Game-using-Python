print("*******WELCOME*******")
print("Basic instructions...")
print("This program can guess the number you choose\n")
print("Choose any number between 1 & 60\n")
print("Reply accepted as 'y' for yes and 'n' for no")
print("Type 'exit' to exit the program")
list=[]

def rules():
    print("""This program can guess the number you choose
    Rules:
    1. Choose a number between 1 to 60
    2. The program will display 6 cards with some numbers
    3. You have to simply type 'y' if your number is in the card shown or 'n' if not""")

def card1():
    print("""********Card-1************
  1   3   5   7   9  11
 13  15  17  19  21  23
 25  27  19  31  33  35
 37  39  41  43  45  47
 49  51  53  55  57  59""")
def card2():
    print("""********Card-2************
  2   3   6   7  10  11
 14  15  18  19  22  23
 26  27  30  31  34  35
 38  39  42  43  46  47
 50  51  54  55  58  59""")
def card3():
    print("""********Card-3************
  4  13  22  31  44  53
  5  14  23  36  45  54
  6  15  28  37  46  55
  7  20  29  38  47  60
 12  21  30  39  52  59""")
def card4():
    print("""********Card-4************
  8  13  26  31  44  57
  9  14  27  40  45  58
 10  15  28  41  46  59
 11  24  29  42  47  60
 12  25  30  43  56  xD""")
def card5():
    print("""********Card-5************
 16  21  26  31  52  57
 17  22  27  48  53  58
 18  23  28  49  54  59
 19  24  29  50  55  60
 20  25  30  51  56  xD""")
def card6():
    print("""********Card-6************
 32  37  42  47  52  57
 33  38  43  48  53  58
 34  39  44  49  54  59
 35  40  45  50  55  60
 36  41  46  51  56  xD""")

def game():
    x=0
    ready=(input("Are you ready? \n-->"))
    if ready == 'y' :
        while 1>0:
            try:
            # ******Card-1******#
                card1()
                c1=input(("Your number in card 1? \n"))
                if c1 == 'y':
                    list.append(1)
                elif c1 == 'n':
                    print("Let's move onto next one!")

            #******Card-2******#
                card2()
                c2 = input(("Your number in card 2? \n"))
                if c2 == 'y':
                    list.append(2)
                elif c2 == 'n':
                    print("Let's move onto next one!")

            # ******Card-3******#
                card3()
                c3 = input(("Your number in card 3? \n"))
                if c3 == 'y':
                    list.append(4)
                elif c3 == 'n':
                    print("Let's move onto next one!")

            # ******Card-4******#
                card4()
                c4 = input(("Your number in card 4? \n"))
                if c4 == 'y':
                    list.append(8)
                elif c4 == 'n':
                    print("Let's move onto next one!")

            # ******Card-5******#
                card5()
                c5 = input(("Your number in card 5? \n"))
                if c5 == 'y':
                    list.append(16)
                elif c5 == 'n':
                    print("Let's move onto next one!")

            # ******Card-6******#
                card6()
                c6 = input(("Your number in card 6? \n"))
                if c6 == 'y':
                    list.append(32)
                elif c6 == 'n':
                    print("""'This is the end of cards!'
If your number was not in any of the cards show then read the rules!
Bye!""")
                print("")
            except:
                print("Wrong input")
            for i in list:
                x += i
            print("Your number is: ",x)
            break

    elif ready == "n":
        choice=input(("To see the rules again type 'rules'\n"""))
        if choice == 'rules':
            rules()

    else:
        print("Incorrect input")


while 1>0:
    play = input("\nWant to play?\n-->")
    if play == 'y':
        game()
    elif play == 'n':
        rules()
    elif play == 'rules':
        rules()
    else:
        break
