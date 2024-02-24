import random
#user_play = "y"
print("Let's play some rock, paper, scissors, lizard, Spock!!")
#set options for computer to run
options = ["r", "p", "sc", "l", "sp"]
comp_choice = random.choice(options)
#set options for user
user_choice = input("Make your choice: (r)ock, (p)aper, (sc)issors, (l)izard, (sp)ock? ")
#while user_play == "y":
    #run all rock conditionals
if(user_choice == "r" and comp_choice == "p"):
    print("Sorry, you lose! You chose rock & the comp chose paper! Paper covers rock!")
elif(user_choice == "r" and comp_choice == "sc"):
    print("Yay, you won! You chose rock & the comp chose scissors! Rock smashes scissors!")
elif(user_choice == "r" and comp_choice == "l"):
    print("Yay, you won! You chose rock & the comp chose lizard! Rock crushes lizard!")
elif(user_choice == "r" and comp_choice == "sp"):
    print("Sorry, you lose! You chose rock & the comp chose Spock! Spock vaporizes rock!")
elif(user_choice == "r" and comp_choice == "r"):
    print("It's a tie! You chose rock & the comp chose rock!")
#run all paper conditionals
elif(user_choice == "p" and comp_choice == "p"):
    print("It's a tie! You chose paper & the comp chose paper!")
elif(user_choice == "p" and comp_choice == "sc"):
    print("Sorry, you lose! You chose paper & the comp choice scissors! Scissors cuts paper!")
elif(user_choice == "p" and comp_choice == "l"):
    print("Sorry, you lose! You chose paper & the comp choice lizard! Lizard eats paper!")
elif(user_choice == "p" and comp_choice == "sp"):
    print("Yay, you win! You chose paper & the comp choice Spock! Paper disproves Spock!")
elif(user_choice == "p" and comp_choice == "r"):
    print("Yay, you win! You chose rock & the comp chose paper! Paper covers rock!")
#run all scissors conditionals
elif(user_choice == "sc" and comp_choice == "p"):
    print("Yay, you win! You chose scissors & the comp chose paper! Scissors cuts paper!")
elif(user_choice == "sc" and comp_choice == "sc"):
    print("It's a tie! You chose scissors & the comp chose scissors!")
elif(user_choice == "sc" and comp_choice == "l"):
    print("Yay, you win! You chose scissors & the comp choice lizard! Scissors decapitates lizard!")
elif(user_choice == "sc" and comp_choice == "sp"):
    print("Sorry, you lose! You chose scissors & the comp choice Spock! Spock smashes scissors!")
elif(user_choice == "sc" and comp_choice == "r"):
    print("Sorry, you lose! You chose scissors & the comp choice rock! Rock smashes scissors!")
    #run all lizard conditionals
elif(user_choice == "l" and comp_choice == "p"):
    print("Yay, you win! You chose lizard & the comp chose paper! Lizard eats paper!")
elif(user_choice == "l" and comp_choice == "sc"):
    print("Sorry, you lose! You chose lizard & the comp choice scissors! Scissors decapitates lizard!")
elif(user_choice == "l" and comp_choice == "l"):
    print("It's a tie! You chose lizard & the comp chose lizard!")
elif(user_choice == "l" and comp_choice == "sp"):
    print("Yay, you win! You chose lizard & the comp choice Spock! Lizard poisons Spock!")
elif(user_choice == "l" and comp_choice == "r"):
    print("Sorry, you lose! You chose rock & the comp chose lizard! Rock crushes lizard!")
    #run all spock conditionals
elif(user_choice == "sp" and comp_choice == "p"):
    print("Sorry, you lose! You chose paper & the comp choice Spock! Paper disproves Spock!")
elif(user_choice == "sp" and comp_choice == "sc"):
    print("Yay, you win! You chose scissors & the comp choice Spock! Spock smashes scissors!")
elif(user_choice == "sp" and comp_choice == "l"):
    print("Sorry, you lose! You chose lizard & the comp choice Spock! Lizard poisons Spock!")
elif(user_choice == "sp" and comp_choice == "sp"):
    print("It's a tie! You chose Spock & the comp chose Spock!")
elif(user_choice == "sp" and comp_choice == "r"):
    print("Yay, you win! You chose rock & the comp chose Spock! Spock vaporizes rock!")
else:
    print("Oops, wrong value")
    print("Next time, choose from 'r', 'p', 'sc', 'l', or 'sp'.")
    #user_play = input("Continue to play? (y)es or (n)o? ")```