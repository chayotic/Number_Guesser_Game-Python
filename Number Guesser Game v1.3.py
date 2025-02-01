# Number Guessing Game
# Version 1.3
import time
import random
from termcolor import colored

# INITIAL VARIABLES
commands = {"/updlogs": "show_logs", "/number": "show_number", "/dev": "toggle_dev_mode", "/bot": "use_bot","/set":"set_variable"}
setvar=["timesleep","high","low"]
yes = {"y", "yes"}
no = {"n", "no"}
guess = True
dev_mode = False
bot = False
user="you"
total_games = 0
average_tries = 0
tries = 0
high, low = 100, 0
timeslp=0.2

# FUNCTIONS
    
def dev_error():
    print(colored("\tTurn On Developer Mode!", "red", attrs=["bold"]))

def set_error(var_name,value):
    print("\tVariable",var_name,"could not set to",value)

def set_done(var_name,value):
    print("\tVariable",var_name,"set to",value)
    
def set(var,value):
    if dev_mode:
        if var=="timesleep":
            global timeslp
            timeslp=value
            if timeslp<0:
                tmslp=0
                set_error(var,timeslp)
            else:
                set_done(var,timeslp)
        if var=="high":
            global high
            high=value
            if high>100:
                set_error(var,high)
                high=0
            else:
                set_done(var,high)
        if var=="low":
            global low
            low=value
            if low<0:
                set_error(var,low)
                low=0
            else:
                set_done(var,low)
    else:
        dev_error()
          
def show_logs():
    """Displays update logs if developer mode is on."""
    if dev_mode:
        logs = """
\t# Update Log:
\t# v0.1: Initial Release
\t# v0.2: Range Restriction
\t# v0.3: Error Handling
\t# v0.4: Improved Input Validation
\t# v0.5: Average Tries Feature
\t# v0.6: Bug Fix
\t# v0.7: Developer Options Added
\t# v0.8: Toggle Developer Mode & UI Improvement
\t# v0.9: UI Improvements
\t# v1.0: Cleaner Code For Better Accesibility
\t# v1.1: Added AI... use command /bot to activate it
\t# v1.2: Added /set command to modify game variables along\n\twith enhanced error handling
\t# v1.3: /set supports floats and bot starts at 50 for\n\tbetter chances and UI enhancement.
        """
        print(colored(logs, "cyan"))
    else:
        dev_error()


def show_number(target):
    """Displays the target number if developer mode is on."""
    if dev_mode:
        print(colored(f"\tThe Number is: {target}", "yellow"))
    else:
        dev_error()

def toggle_dev_mode():
    """Toggles developer mode on/off."""
    global dev_mode
    dev_mode = not dev_mode
    status = "on" if dev_mode else "off"
    print(colored(f"\tDeveloper mode turned {status}!", "yellow", attrs=["bold"]))


def calculate_average(current_tries):
    """Calculates the average tries across all games."""
    global total_games, average_tries
    total_games += 1
    average_tries = ((average_tries * (total_games - 1)) + current_tries) / total_games
    return round(average_tries, 1)


def use_bot():
    if dev_mode:
        global bot
        global user
        user="the bot"
        bot = True
    else:
        dev_error()

# MAIN GAME LOOP
print("\n\n\tWelcome to the Number Guessing Game!")

while guess:
    target_number = random.randint(0, 100)
    tries = 0
    print(colored("\n\tGuess a Number Between 0-100!", "magenta", attrs=["bold"]))

    while True:
        if not bot:
            user_input = input("\n\tEnter your guess or a command: ").strip()
        else:
            if low > high:
                print(colored("\tError: Invalid Range for Bot.Resetting the Game!", "red"))
                low, high=0, 100            
                break            
            if tries !=0:
                user_input = str(random.randint(low, high))
            else:
                user_input = str(50)
            print("\n\tBot Guessed:",user_input)            

        # Handle commands
        if user_input in commands:
            if commands[user_input] == "show_logs":
                show_logs()
            elif commands[user_input] == "show_number":
                show_number(target_number)
            elif commands[user_input] == "use_bot":
                use_bot()
                continue
            elif commands[user_input] == "set_variable":
                if dev_mode:
                    var=input("\t/set")
                    if var in setvar:
                            val=input("\tto_value_")
                            try:
                                float(val)
                                set(var,float(val))
                            except ValueError:
                                print(colored("\tError","red",attrs=["bold"]))
                    else:
                        print(colored("\tError","red",attrs=["bold"]))
                else:
                    dev_error()
                    
            elif commands[user_input] == "toggle_dev_mode":
                toggle_dev_mode()
            continue

        # Handle numeric input
        if user_input.isdigit():
            guess_number = int(user_input)
            if not 0 <= guess_number <= 100:
                print(colored("\tError! Number Must Be Between 0-100.", "red"))
                continue

            tries += 1
            if guess_number == target_number:
                print(colored(f"\tPERFECT! {user} guessed it!", "green", attrs=["bold"]))
                print(f"\n\tIt Took {user} {tries} Tries")
                print(f"\tAverage Tries Across Games: {calculate_average(tries)}")

                # Play again prompt
                while True:
                    play_again = input(colored("\n\tStart a New Game? (Yes/No): ", "yellow")).lower()
                    if play_again in yes:
                        high, low = 100, 0
                        bot = False
                        user="You"
                        break
                    elif play_again in no:
                        guess = False
                        print(colored("\n\n\tThank You for Playing!", "cyan", attrs=["bold"]))
                        break
                    else:
                        print(colored("\tError! Please Enter 'Yes' or 'No'.", "red"))
                break
            else:
                hint = "Higher" if guess_number < target_number else "Lower"
                color = "yellow" if hint == "Higher" else "cyan"
                print(colored(f"\tTry Going {hint}!", color, attrs=["bold"]))
                if hint == "Higher":
                    low = guess_number + 1
                else:
                    high = guess_number - 1
        else:
            print(colored("\tError! Enter a Valid Number or Command.", "red"))
        time.sleep(timeslp)