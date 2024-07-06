import random as rd;

user = input("Want to play game (Y/N): ");

while user=='Y' or user=='y':

    print("================================");
    print("Rock Paper Scissors Lizard Spock");
    print("================================");

    userInput = int(input("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\nPick a number: "));
    
    if userInput==1:
        print('You chose: ✊');
    elif userInput==2:
        print('You chose: ✋');
    elif userInput==3:
        print('You chose: ✌️');
    elif userInput==4:
        print('You chose: 🦎');
    elif userInput==5:
        print('You chose: 🖖');
    else:
        print('Invalid Choice!!');
        user = input("Want to try again (Y/N): ");
        continue;
    
    computerInput  = rd.randint(1,5);

    if computerInput==1:
        print('CPU chose: ✊');
    elif computerInput==2:
        print('CPU chose: ✋');
    elif computerInput==3:
        print('CPU chose: ✌️');
    elif computerInput==4:
        print('CPU chose: 🦎');
    elif computerInput==5:
        print('CPU chose: 🖖');
    else:
        print('Invalid Choice!!');
        user = input("Want to try again (Y/N): ");
        continue;
    
    if userInput==computerInput:
        print("It's a tie!");
    
    elif (userInput==1 and (computerInput==3  or computerInput==4)) or (userInput==2 and (computerInput==1  or computerInput==5)) or (userInput==3 and (computerInput==2  or computerInput==4)) or (userInput==4 and (computerInput==5  or computerInput==2)) or (userInput==5 and (computerInput==3  or computerInput==1)):
         print("You Won 🏆!!");
    
    else:
        print("Computer Won 🏆!!");
    
    user = input("Want to play again (Y/N): ");
