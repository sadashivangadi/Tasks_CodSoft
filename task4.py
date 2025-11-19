#CodSoft Task 4 - Rock Paper Scissors (Begginer Version)
import random
print("\n\n======✊(Rock), ✋(Paper), and ✌️(Scissors)=====")
choice=["rock","paper","scissors"]
user=""
while True:
    print("\n Enter your option--:\n\n")
    print("1.Rock ✊\n")
    print("2.Paper ✋\n")
    print("3.Scissors ✌️\n")

    user_input=input("\n✅Enter 1,2,3\t")

    #conver user input into ntext choice
    if user_input=='1':
        user='rock'
    elif user_input=='2':
        user='paper'
    elif user_input=='3':
        user='scissors'
    else:
        print("\n Invalid choice ❌,Please Enter the ✅1,2,3\n")

    #computer choice
    computer=random.choice(choice)

    print("You choice the user 👤", user)
    print("\nYou choice the computer 💻", computer)

    #game logic
    if user==computer:
        print("Result is Tie 🔗")
    elif user=='rock':
        if computer=='scissors':
            print("\n✅ Result.you Win!✅")
        else:
            print("\n❌Result.you Lose!❌")
    elif user=='paper':
        if computer=='rock':
            print("\n✅ Result.you Win!✅")
        else:
            print("\n❌ Result.you Lose!❌")
    elif user=='scissors':
        if computer=='paper':
            print("\n✅ Result.you Win!✅✅")
        else:
            print("\n❌Result.you Lose!❌")
    
    #play again
    again=input("\n Do you want to play again✅(yes/no)❌:").lower()
    if again!="yes":
        print("\nThanks for playing 🤝! Goodbye!!👋")
        break
