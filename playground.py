# Python Playground v0.1
import time
import os
# To pseudo-clear screen, copy and paste the following command: print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
yesno = ['y', 'n']
def clearScreen():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")
def rockpaperscissors():
      import random
      clearScreen()
      options = ["rock", "paper", "scissors"]
      computer_choice = random.choice(options)
      user_choice = input("Choose 'rock', 'paper', or 'scissors': ").lower()
      if user_choice not in options:
            print("Invalid choice. Please choose rock, paper, or scissors.")
      else:
            time.sleep(1)
            print(f"Computer chose {computer_choice}.")
            if user_choice == computer_choice:
                  time.sleep(2)
                  print("Tie!")
                  processEnd_HANDLER()
            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                    time.sleep(2)
                    print("You win!")
                    processEnd_HANDLER()
            else:
                    time.sleep(2)
                    print("You lose!")
                    processEnd_HANDLER()


      
def main_Menu():
        clearScreen()
        print("Welcome to the Python Playground!")
        time.sleep(2)
        clearScreen()
        print("What do you wish to do?")
        time.sleep(1)
        print("\n")
        print("1. Send a Hello World message")
        time.sleep(0.1)
        print("2. Play Rock-Paper-Scissors")
        time.sleep(0.1)
        print("3. Read the Python Playground README.txt file")
        time.sleep(0.1)
        choice = input("(1 to 3): ")

        if choice == '1':
            helloworld()     
        elif choice == '2':
            rockpaperscissors()
        elif choice == '3':
              readme()

def processEnd_HANDLER():
      time.sleep(3)
      print("Now returning to the Main Menu...")
      time.sleep(1)
      clearScreen()
      main_Menu()

def helloworld():
    clearScreen()
    print("Hello, world!")
    processEnd_HANDLER()

def readme():
      path_to_readme = r'C:\Users\arech\OneDrive\Documents\Visual Studio Projects\Python\Python Playground\README.txt'      
      clearScreen()
      with open(path_to_readme, 'r') as file:
            content = file.read()
            print(content)
            ask_mainmenu = input("Do you wish to return to the main menu? (y/n): ").lower()
            if ask_mainmenu == 'y':
                  main_Menu()
            elif ask_mainmenu == 'n':
                  readme
main_Menu()