# version 4. add one more row. 4x4
import random
from rich.console import Console
from rich import print
import time

""" Spel enarmad banit, slot machine """

money = 1000
used_money = 0
con = Console()
stop_counter = True
win = False # if you able to stop 3 rows

old_row0 = {}
old_row1 = {}
old_row2 = {}
old_row3 = {}

all_fruits = ":apple: :banana: :lemon: :melon: :mango: :peach: :pineapple: :watermelon: :grapes: :strawberry: :cherries:"
jackpot = {1: ":cherries:", 2: ":cherries:", 3: ":cherries:", 4: ":cherries:"}
silver = {1: ":cherries:", 2: ":cherries:", 3: ":cherries:", 4: ":apple:"}
brons = {1: ":cherries:", 2: ":cherries:", 3: ":banana:", 4: ":watermelon:"}

# TESTING
#fusk1  = {1: ":cherries:", 2: ":apple:", 3: ":banana:", 4: ":apple:"}
#fusk2  = {1: ":apple:", 2: ":cherries:", 3: ":apple:", 4: ":watermelon:"}
#fusk3  = {1: ":banana:", 2: ":apple:", 3: ":cherries:", 4: ":apple:"}
#fusk4  = {1: ":apple:", 2: ":lemon:", 3: ":banana:", 4: ":cherries:"}

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


# Returns a new dictionary with 4 random fruits
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
    ''' The main function for spin. num=number from the user. num=witch row to stop '''
    new_fruit_row_0 = get_4_fruits()
    new_fruit_row_1 = get_4_fruits()
    new_fruit_row_2 = get_4_fruits()
    new_fruit_row_3 = get_4_fruits()
    
    # TESTING
    #new_fruit_row_0 = fusk1
    #new_fruit_row_1 = fusk2
    #new_fruit_row_2 = fusk3
    #new_fruit_row_3 = fusk4

    # check witch row to stop
    r1, r2, r3, r4 = stop_rows(num, new_fruit_row_0,new_fruit_row_1,new_fruit_row_2, new_fruit_row_3)

    # print new table
    print_table(r1, r2, r3, r4)

    # check for duplicates fruits
    find_duplicates(r1, r2, r3, r4)


def stop_rows(num, new_fruit_row_0, new_fruit_row_1, new_fruit_row_2, new_fruit_row_3):
    ''' check which rows to stop. num=number of the row to stop '''
    global old_row0 
    global old_row1 
    global old_row2
    global old_row3
    global stop_counter
    global win
        
    # save old_row from the spin before
    if stop_counter == False:
        old_row0 = new_fruit_row_0
        old_row1 = new_fruit_row_1
        old_row2 = new_fruit_row_2
        old_row3 = new_fruit_row_3
        stop_counter = True
        win = False
        print("Stop rows this time = ", stop_counter)
    elif stop_counter == True: 
        stop_counter = False
        print("Stop rows this time = ", stop_counter)
    
    ''' Stop row with 8 different combinations: 12, 13, 14, 23, 24, 34, 124, 134 '''
    # user stop row 1 and 2
    if num == 12 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row1 = new_fruit_row_1
    elif num == 12 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replace row with the old_row
        new_fruit_row_1 = old_row1 # replace row with the old_row

    # user stop row 1 and 3
    if num == 13 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row2 = new_fruit_row_2
    elif num == 13 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replace row with the old_row
        new_fruit_row_2 = old_row2 # replace row with the old_row

    # user stop row 1 and 4
    if num == 14 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row3 = new_fruit_row_3
    elif num == 14 and stop_counter == False:
        new_fruit_row_0 = old_row0 # replace row with the old_row
        new_fruit_row_3 = old_row3 # replace row with the old_row

    # user stop row 2 and 3
    if num == 23 and stop_counter == True:
        old_row1 = new_fruit_row_1
        old_row2 = new_fruit_row_2
    elif num == 23 and stop_counter == False:
        new_fruit_row_1 = old_row1 # replace row with the old_row
        new_fruit_row_2 = old_row2 # replace row with the old_row

    # user stop row 2 and 4
    if num == 24 and stop_counter == True:
        old_row1 = new_fruit_row_1
        old_row3 = new_fruit_row_3
    elif num == 24 and stop_counter == False:
        new_fruit_row_1 = old_row1 # replace row with the old_row
        new_fruit_row_3 = old_row3 # replace row with the old_row

    # user stop row 3 and 4
    if num == 34 and stop_counter == True:
        old_row2 = new_fruit_row_2
        old_row3 = new_fruit_row_3
    elif num == 34 and stop_counter == False:
        new_fruit_row_2 = old_row2 # replace row with the old_row
        new_fruit_row_3 = old_row3 # replace row with the old_row

    # user stop row 1, 3 and 4. Stop 3 rows!
    if num == 134 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row2 = new_fruit_row_2
        old_row3 = new_fruit_row_3
    elif num == 134 and stop_counter == False:
        new_fruit_row_0 = old_row0
        new_fruit_row_2 = old_row2 
        new_fruit_row_3 = old_row3 

    # user stop row 1, 2 and 4. Stop 3 rows!
    if num == 124 and stop_counter == True:
        old_row0 = new_fruit_row_0
        old_row1 = new_fruit_row_1
        old_row3 = new_fruit_row_3
    elif num == 124 and stop_counter == False:
        new_fruit_row_0 = old_row0
        new_fruit_row_1 = old_row1 
        new_fruit_row_3 = old_row3 
    
    # TODO if not win do this...
    # stop row 1, 2 and 3. 
    if win == False:
        if num == 123 and stop_counter == True:
            old_row0 = new_fruit_row_0
            old_row1 = new_fruit_row_1
            old_row2 = new_fruit_row_2
        elif num == 123 and stop_counter == False:
            new_fruit_row_0 = old_row0 
            new_fruit_row_1 = old_row1 
            new_fruit_row_2 = old_row2 
            win = True

        # user stop row 2, 3 and 4. 
        if num == 234 and stop_counter == True:
            old_row1 = new_fruit_row_1
            old_row2 = new_fruit_row_2
            old_row3 = new_fruit_row_3
        elif num == 234 and stop_counter == False:
            new_fruit_row_1 = old_row1
            new_fruit_row_2 = old_row2 
            new_fruit_row_3 = old_row3 
            win = True
    
    # return new table
    return new_fruit_row_0, new_fruit_row_1, new_fruit_row_2, new_fruit_row_3



def print_table(new_fruit_row_0, new_fruit_row_1, new_fruit_row_2, new_fruit_row_3,  ):
    print("        -----------------------")
    print("Row 1: | ", end=" ")
    spin_animation(new_fruit_row_0, 0.1)
    print("\n       |     |     |     |     |   ")
    print("Row 2: | ", end=" ")
    spin_animation(new_fruit_row_1, 0.1)
    print("\n       |     |     |     |     |   ")
    print("Row 3: | ", end=" ")
    spin_animation(new_fruit_row_2, 0.1)
    print("\n       |     |     |     |     |   ")
    print("Row 4: | ", end=" ")
    spin_animation(new_fruit_row_3, 0.1)
    print("\n        -----------------------")


def find_duplicates(r1, r2, r3, r4):
    ''' find duplicates and add money if win '''
    global money, win
    rad0 = list(r1.values())
    rad1 = list(r2.values())
    rad2 = list(r3.values())
    rad3 = list(r4.values())

    # check ONLY ONCE for diagonal wins. Left to right
    if rad0[0] == rad1[1] and rad2[2] == rad0[0] and rad3[3] == rad0[0]:
        print("Winning on: ", rad0[0], rad1[1], rad2[2], rad3[3], " !")
        print("You won 500 000 €")
        print("row 1 and 2 and 3 and 4")
        super_mega_jackpot_animation()
        money += 500000

    # check ONLY ONCE for diagonal wins. Right to left 
    if rad0[3] == rad1[2] and rad2[1] == rad0[3] and rad3[0] == rad0[3]:
        print("Winning on: ", rad0[3], rad1[2], rad2[1], rad3[0], " !")
        print("You won 500 000 €")
        print("row 1 and 2 and 3 and 4")
        super_mega_jackpot_animation()
        money += 500000

    for i in range(4):
        # check row 1,2,3,4
        if rad0[i] == rad1[i] and rad2[i] == rad0[i] and rad3[i] == rad0[i]:
            print("Winning on: ", rad0[i], rad1[i], rad2[i], rad3[i], " !")
            print("You won 200 000 €")
            print("row 1 and 2 and 3 and 4")
            mega_jackpot_animation()
            money += 200000
            win = True
        # check row 1,2,3
        elif rad0[i] == rad1[i] and rad2[i] == rad0[i]:
            print("Winning on: ", rad0[i], rad1[i], rad2[i], " !")
            print("You won 10 000 €")
            print("row 1 and 2 and 3")
            jackpot_animation()
            money += 10000
            win = True
        # check row 2,3,4
        elif rad1[i] == rad2[i] and rad2[i] == rad3[i]:
            print("Winning on: ", rad1[i], rad2[i], rad3[i], " !")
            print("You won 10 000 €")
            print("row 2 and 3 and 4")
            jackpot_animation()
            money += 10000
            win = True
        elif rad0[i] == rad1[i]:
            print("Winning on: ", rad0[i], rad1[i], " !")
            print("You won [yellow]FREE SPIN[/]")
            print("row 1 and 2")
            money += 100
        elif rad1[i] == rad2[i]:
            print("Winning on: ", rad1[i], rad2[i], " !")
            print("You won [yellow]FREE SPIN[/]")
            print("row 2 and 3")
            money += 100
        elif rad2[i] == rad3[i]:
            print("Winning on: ", rad2[i], rad3[i], " !")
            print("You won [yellow]FREE SPIN[/]")
            print("row 3 and 4")
            money += 100



def super_mega_jackpot_animation():
    global con
    con.print(
        "[bold blink red] SUPER MEGA JACKPOT! [/] \nCongratulations! You won 500 000 !"
    )


def mega_jackpot_animation():
    global con
    con.print(
        "[bold blink red] MEGA JACKPOT! [/] \nCongratulations! You won 200 000 !"
    )


def jackpot_animation():
    global con
    con.print(
        "[bold blink red] JACKPOT! [/] \nCongratulations! You won 10 000 !"
    )


def welcome_message():
    global con
    con.print(all_fruits, all_fruits)
    con.print(
        "Welcome to play and to lose all your money in the :moneybag:[bold red]SLOT MACHINE[/]:moneybag:",
        style="bold yellow",
    )
    con.print(
        "\n:slot_machine: Hit [bold red]ENTER[/] to Spin the fruits and win the game!:slot_machine: "
    )
    con.print("To stop rows use: 12, 13, 14, 23, 24, 34 124 or 134", style="bold green",)
    con.print("I give you a free spin", style="purple")


def main():
    global money, used_money, con
    congrats = 10000
    welcome_message()

    # run one free spin
    spin(0)

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
        elif response == "13": # stop row 1 and 3
            spin(13)
        elif response == "14": # ...
            spin(14)
        elif response == "23":
            spin(23)
        elif response == "24":
            spin(24)
        elif response == "34":
            spin(34)
        elif response == "124":
            spin(124)
        elif response == "134":
            spin(134)
        elif response == "123":
            spin(123)
        elif response == "234":
            spin(234)
        else:
            con.print("'q' for quit.")
            con.print("To stop rows use: 12, 13, 14, 23, 24, 34, 124 or 134")
            con.print(
                f":wheel_of_dharma: Spin Money to use: [bold red]{money - used_money}[/] $"
            )


if __name__ == "__main__":
    main()
