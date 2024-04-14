import random
from rich.console import Console
from rich import print
import time

''' Spel enarmad banit, slot machine '''

money = 1000
used_money = 0
con = Console()

all_fruits = ":apple: :banana: :lemon: :melon: :mango: :peach: :pineapple: :watermelon: :grapes: :strawberry: :cherries:"
jackpot = {1 : ":cherries:", 2 : ":cherries:", 3 : ":cherries:", 4 : ":cherries:"}
silver = {1 : ":cherries:", 2 : ":cherries:", 3 : ":cherries:", 4 : ":apple:"}
brons = {1 : ":cherries:", 2 : ":cherries:", 3 : ":banana:", 4 : ":watermelon:"}

fruits = {1: ":apple:", 2: ":banana:", 3: ":lemon:", 4: ":melon:", 5: ":mango:", 6: ":peach:", 7: ":pineapple:", 8: ":watermelon:", 9: ":grapes:", 10: ":strawberry:", 11: ":cherries:"}

# Returns a new dictionary with random fruits 
def spin4_fruits():
    random_fruits = random.sample(list(fruits.items()), 4)
    new_fruits = dict(random_fruits)
    return new_fruits

# print animation
def spin_animation(fruits, speed):
   for fruit in fruits:
        print(fruits[fruit], end=" ", flush=True)
        time.sleep(speed)
        print(" ", end="", flush=True)

def spins():
    spin = spin4_fruits() # TODO
    print("-------------------")
    spin_animation(spin, 0.1)
    print("")

def jackot_animation():
    global money
    money += 5000
    spins()
    print("-------------------")
    spin_animation(jackpot, 0.5)
    print("")
    spins()
    print("-------------------")
    con.print("[bold blink red] JACKPOT! [/] \nFour cherries in a row!\nCongratulations! You won 5000 $!")
    

def silver_animation():
    global money
    money += 3000
    spins()
    print("-------------------")
    spin_animation(silver, 0.5)
    print("")
    spins()
    print("-------------------")
    print("Three cherries in a row!\nCongratulations! You won 3000 $!")
    

def brons_animation():
    global money
    money += 1000
    spins()
    print("-------------------")
    spin_animation(brons, 0.5)
    print("")
    spins()
    print("-------------------")
    print("Two cherries in a row!\nCongratulations! You won 1000 $!")
    

# Welcome message
con.print(all_fruits)
con.print("Welcome to lose all your money in the :moneybag:[bold red]SLOT MACHINE[/]:moneybag:", style="bold yellow")
con.print("\n:slot_machine: Hit [bold red]ENTER[/] to Spin the fruits end win the game!:slot_machine: ")
spin_animation(spin4_fruits(), 0.1)


def main():
    global money, used_money
    congrats = 10000
    while True:
        random_win = random.randint(1, 20)
        
        if money - used_money < 100:
            con.print("You don't have enough money to play!")
            break
        if money - used_money > congrats:
            con.print(f"[bold yellow blink]Congratulations [/]You have now: {money - used_money} $!")
            congrats += 10000
            
        response = input(f"\n{money - used_money} $ Hit ENTER to spin: ")
        
        if response == "":
            used_money += 100
            if random_win == 1:
                jackot_animation()
            elif random_win == 2 or random_win == 3:
                silver_animation()
            elif random_win == 4 or random_win == 5 or random_win == 6 or random_win == 7 or random_win == 8 or random_win == 9 or random_win == 10:
                brons_animation()
            else:    
                for _ in range(3):
                    spins()
        elif response == "q":
            con.print("Thank you for playing!")
            break
        else:
            con.print("'q' for quit.")
            con.print(f":wheel_of_dharma: Spin Money to use: [bold red]{money - used_money}[/] $")
            

if __name__ == "__main__":
    main()