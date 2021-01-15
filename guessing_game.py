import random
import math
from IPython.display import clear_output
count = 0
guess_list = []
responses_list = ["null"] 
guessing = True

def clear_screen():
    '''
    Clears all previous output and produces the computer's guess and the number the player has chosen.
    '''
    clear_output()
    print(f"The computer has guessed {guess} and your number is {number}.")

while True:
    try:
        high = int(input('Please choose a higher bound for the guessing game: '))
    except:
        clear_output()
        print('Please select a positive integer!')
    else:
        if high <= 0:
            clear_output()
            print('Please select a positive integer!')
        else:
            clear_output()
            print(f'You have selected {high} as the higher bound.')
            guess_list.append(high)
            break
        
while True:
    try:
        number = int(input(f"Please choose a postive number, under {high}, that you'd like the computer to guess: "))
    except:
        clear_output()
        print(f"Please choose a postive integer under {high}!")
    else:
        if number >= high or number < 0: # negative 
            clear_output()
            print(f"Please choose a positive integer under {high}!")
        else:
            clear_output()
            print(f'You have selected {number}')
            guess = random.randint(0, high)
            guess_list.append(guess)
            break

while guessing:
    if guess == number:
        print(f"The computer has guessed {number} correctly in {count + 1} guesses!")
        print(f'The guesses were {", ".join([str(x) for x in guess_list[1::]])}.')
        guessing = False
        break
    else:
        clear_screen()
        
        while True:
            response = input("Is your number higher or lower? Respond with 'h/l' ")
            
            if len(response) < 1:
                clear_screen()
                print("Please enter in 'h' or 'l' for higher or lower!")
            elif response[0].lower() not in ("h", "l"):
                clear_screen()
                print("Please enter in 'h' or 'l' for higher or lower!")
            elif response[0].lower() == "h" and number < guess:
                clear_screen()
                print("Double check your answer!")
            elif response[0].lower() == "l" and number > guess: #  Split these instead of writing in one line
                clear_screen()
                print("Double check your answer!")
            else:
                clear_screen()
                responses_list.append(response[0].lower())
                previous_guess = guess_list[count]
                count += 1
                break

        if responses_list[count][0].lower() == 'h':
            if count <= 1:
                guess = math.ceil((high + guess)/2)
            else:
                guess = guess +  max(1, math.floor(math.fabs((previous_guess - guess)/2)))

        else: # If response is lower
            if count <= 1 or "l"*count == "".join(responses_list[1::]): 
                guess = math.floor((guess)/2)
            else:
                guess = guess - math.ceil(math.fabs((previous_guess - guess)/2))
                
        guess_list.append(guess)
        
# Debugging code below, shows what turn corresponds to which guess
#         for item in enumerate(guess_list):
#             print(item)   
