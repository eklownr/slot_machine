# version 3. 
import random
from rich.console import Console
from rich import print
import time

""" Spel enarmad banit, slot machine """

money = 1000
used_money = 0
con = Console()
win = 0
stop_counter = True

old_row0 = {}
old_row1 = {}
old_row2 = {}


all_fruits = ":apple: :banana: :lemon: :melon: :mango: :peach: :pineapple: :watermelon: :grapes: :strawberry: :cherries:"
jackpot = {1: ":cherries:", 2: ":cherries:", 3: ":cherries:", 4: ":cherries:"}
silver = {1: ":cherries:", 2: ":cherries:", 3: ":cherries:", 4: ":apple:"}
brons = {1: ":cherries:", 2: ":cherries:", 3: ":banana:", 4: ":watermelon:"}

fruits = {
    1: ":apple:",
    2: ":banana:",
    3: ":lemon:",
    4: ":melon:",
    5: ":mango:",
    6: ":peach:",
    7: ":pineapple:",
    8: ":watermelon:",
    9: ":grapes:",
    10: ":strawberry:",
    11: ":cherries:",
}


# Returns a new dictionary with random fruits
def get_4_fruits():
    random_fruits = random.sample(list(fruits.items()), 4)
    new_fruits = dict(random_fruits)
    return new_fruits


# print animation
def spin_animation(fruits, speed):
    for fruit in fruits:
        print( fruits[fruit] + " |", end=" ", flush=True)
        time.sleep(speed)
        print(" ", end="", flush=True)


def spin(num):
    new_fruit_row_0 = get_4_fruits()
    new_fruit_row_1 = get_4_fruits()
    new_fruit_row_2 = get_4_fruits()

    global old_row0 
    global old_row1 
    global old_row2

    global stop_counter
        
    if stop_counter == False:
        old_row0 = new_fruit_row_0
        old_row1 = new_fruit_row_1
        old_row2 = new_fruit_row_2
        stop_counter = True
        print("Stop rows this time = ", stop_counter)
    elif stop_counter == True: 
        stop_counter = False
        print("Stop rows this time = ", stop_counter)

    # user stop row 1 and 2
    if num == 12 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row1 = new_fruit_row_1
    elif num ==12 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replays row 1 with the old_row
        new_fruit_row_1 = old_row1 # replays row 1 with the old_row

    # user stop row 1 and 3
    if num == 13 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row2 = new_fruit_row_2
    elif num ==13 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replays row 1 with the old_row
        new_fruit_row_2 = old_row2 # replays row 1 with the old_row

    # user stop row 2 and 3
    if num == 23 and stop_counter == True:
        old_row1 = new_fruit_row_1
        old_row2 = new_fruit_row_2
    elif num == 23 and stop_counter == False:
        new_fruit_row_1 = old_row1 # replays row 1 with the old_row
        new_fruit_row_2 = old_row2 # replays row 1 with the old_row

    # user stop row 1 
    if num == 1 and stop_counter == True:
        old_row0 = new_fruit_row_0
    elif num == 1 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replays row 1 with the old_row

    # user stop row  2
    if num == 2 and stop_counter == True:
        old_row1 = new_fruit_row_1
    elif num == 2 and stop_counter == False:
        new_fruit_row_1 = old_row1 # replays row 1 with the old_row

    # user stop row 3
    if num == 3 and stop_counter == True:
        old_row2 = new_fruit_row_2
    elif num == 3 and stop_counter == False:
        new_fruit_row_2 = old_row2 # replays row 1 with the old_row


    print("        -----------------------")
    print("Row 1: | ", end=" ")
    spin_animation(new_fruit_row_0, 0.1)
    print("\n       |     |     |     |     |   ")
    print("Row 2: | ", end=" ")
    spin_animation(new_fruit_row_1, 0.1)
    print("\n       |     |     |     |     |   ")
    print("Row 3: | ", end=" ")
    spin_animation(new_fruit_row_2, 0.1)
    print("\n        -----------------------")

    find_duplicates(new_fruit_row_0, new_fruit_row_1, new_fruit_row_2)


def find_duplicates(a, b, c):
    global money
    rad0 = list(a.values())
    rad1 = list(b.values())
    rad2 = list(c.values())

    for i in range(4):

        if rad0[i] == rad1[i] and rad2[i] == rad0[i]:
            print("Winning on: ", rad0[i], rad1[i], rad2[i], " !")
            jackpot_animation()
            money += 10000
        elif rad0[i] == rad1[i]:
            print("Winning on: ", rad0[i], rad1[i], " !")
            print("You won 500")
            money += 500
        elif rad1[i] == rad2[i]:
            print("Winning on: ", rad1[i], rad2[i], " !")
            print("You won 500")
            money += 500


def jackpot_animation():
    global con
    con.print(
        "[bold blink red] JACKPOT! [/] \nCongratulations! You won 10 000 !"
    )


def silver_animation():
    global money
    money += 3000
    spin()
    print("-------------------")
    spin_animation(silver, 0.5)
    print("")
    spin()
    print("-------------------")
    print("Three cherries in a row!\nCongratulations! You won 3000 $!")


def brons_animation():
    global money
    money += 1000
    spin()
    print("-------------------")
    spin_animation(brons, 0.5)
    print("")
    spin()
    print("-------------------")
    print("Two cherries in a row!\nCongratulations! You won 1000 $!")


def welcome_message():
    global con
    con.print(all_fruits, all_fruits)
    con.print(
        "Welcome to play and to lose all your money in the :moneybag:[bold red]SLOT MACHINE[/]:moneybag:",
        style="bold yellow",
    )
    con.print(
        "\n:slot_machine: Hit [bold red]ENTER[/] to Spin the fruits end win the game!:slot_machine: "
    )
    print("Stop a row with 1, 2 or 3. Stop 2 rows with 12, 13 or 23")
    spin_animation(get_4_fruits(), 0.1)


def main():
    global money, used_money, win, con
    congrats = 10000
    welcome_message()

    while True:
        if money - used_money < 100:
            con.print("You don't have enough money to play!")
            break
        if money - used_money > congrats:
            con.print(f"[bold yellow blink]Congratulations [/]You have now: {money - used_money} $!")
            congrats += 10000

        response = input(f"\n{money - used_money} $ Hit ENTER to spin: ")

        if response == "":  # Hitt enter to play
            used_money += 100 # It cost 100 to play
            spin(0)
        elif response == "q":
            con.print("Thank you for playing!")
            break
        elif response == "12": # stop row 1 and 2
            spin(12)
        elif response == "13":
            spin(13)
        elif response == "23":
            spin(23)
        elif response == "1":
            spin(1)
        elif response == "2":
            spin(2)
        elif response == "3":
            spin(3)
        else:
            con.print("'q' for quit.")
            con.print(
                f":wheel_of_dharma: Spin Money to use: [bold red]{money - used_money}[/] $"
            )


if __name__ == "__main__":
    main()
