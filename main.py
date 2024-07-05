import random as rd;

user = input("Want to play game (Y/N): ");

while user=='Y' or user=='y':

    print("================================");
    print("Rock Paper Scissors Lizard Spock");
    print("================================");

    userInput = int(input("1) ✊\n2) ✋\n3) ✌️\n4) 🦎\n5) 🖖\nPick a number: "));
    computerInput  = rd.randint(1,5);

    if userInput==1 and computerInput==1:
        print('You chose: ✊');
        print('CPU chose: ✊');
        print('It\'s a tie!');

    elif userInput==2 and computerInput==2:
        print('You chose: ✋');
        print('CPU chose: ✋');
        print('It\'s a tie!');

    elif userInput==3 and computerInput==3:
        print('You chose: ✌️');
        print('CPU chose: ✌️');
        print('It\'s a tie!');

    elif userInput==4 and computerInput==4:
        print('You chose: 🦎');
        print('CPU chose: 🦎');
        print('It\'s a tie!');

    elif userInput==5 and computerInput==5:
        print('You chose: 🖖');
        print('CPU chose: 🖖');
        print('It\'s a tie!');

    elif userInput==1 and computerInput==2:
        print('You chose: ✊');
        print('CPU chose: ✋');
        print('Computer won!');

    elif userInput==1 and computerInput==3:
        print('You chose: ✊');
        print('CPU chose: ✌️');
        print('You Won!💖');

    elif userInput==1 and computerInput==4:
        print('You chose: ✊');
        print('CPU chose: 🦎');
        print('You Won!💖');

    elif userInput==1 and computerInput==5:
        print('You chose: ✊');
        print('CPU chose: 🖖');
        print('Computer won!');

    elif userInput==2 and computerInput==1:
        print('You chose: ✋');
        print('CPU chose: ✊');
        print('You Won!💖');

    elif userInput==2 and computerInput==3:
        print('You chose: ✋');
        print('CPU chose: ✌️');
        print('Computer won!');

    elif userInput==2 and computerInput==4:
        print('You chose: ✋');
        print('CPU chose: 🦎');
        print('Computer won!');

    elif userInput==2 and computerInput==5:
        print('You chose: ✋');
        print('CPU chose: 🖖');
        print('You Won!💖');

    elif userInput==3 and computerInput==1:
        print('You chose: ✌️');
        print('CPU chose: ✊');
        print('Computer won!');

    elif userInput==3 and computerInput==2:
        print('You chose: ✌️');
        print('CPU chose: ✋');
        print('You Won!💖');

    elif userInput==3 and computerInput==4:
        print('You chose: ✌️');
        print('CPU chose: 🦎');
        print('You Won!💖');

    elif userInput==3 and computerInput==5:
        print('You chose: ✌️');
        print('CPU chose: 🖖');
        print('Computer won!');

    elif userInput==4 and computerInput==1:
        print('You chose: 🦎');
        print('CPU chose: ✊');
        print('Computer won!');

    elif userInput==4 and computerInput==2:
        print('You chose: 🦎');
        print('CPU chose: ✋');
        print('You Won!💖');

    elif userInput==4 and computerInput==3:
        print('You chose: 🦎');
        print('CPU chose: ✌️');
        print('Computer won!');

    elif userInput==4 and computerInput==5:
        print('You chose: 🦎');
        print('CPU chose: 🖖');
        print('You Won!💖');

    elif userInput==5 and computerInput==1:
        print('You chose: 🖖');
        print('CPU chose: ✊');
        print('You Won!💖');

    elif userInput==5 and computerInput==2:
        print('You chose: 🖖');
        print('CPU chose: ✋');
        print('Computer won!');

    elif userInput==5 and computerInput==3:
        print('You chose: 🖖');
        print('CPU chose: ✌️');
        print('You Won!💖');

    elif userInput==5 and computerInput==4:
        print('You chose: 🖖');
        print('CPU chose: 🦎');
        print('Computer won!');

    else:
        print('Wrong Input');
    
    user = input("Want to play more (Y/N): ");
