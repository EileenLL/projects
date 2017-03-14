import random

possible_words = ("magma", "merry", "happy", "tacky", "jumpy", 
    "quack", "taxes", "jumbo", "juicy", "fuzzy", 
    "klutz", "crazy", "squad","quilt", "squid", 
    "puppy", "kitty","click")

intro = raw_input("Would you like to play a guessing game? y/n ")

if str.lower(intro) == "n":
    print "Goodbye"
else:
    game_list = random.sample(possible_words, 6)
    password = random.choice(game_list)
    print game_list
   
def start_game(): 
    first_guess = raw_input("What is your first guess? ")
    user_choice = first_guess
    list(password)
    list(user_choice)
    guess_response = []
    count_matching_letters(password, user_choice)

start_game()

def count_matching_letters(password, user_choice):
    char_match = []
    for index in range(len(password)):
        if password[index] == user_choice[index]:
            char_match = char_match + (1,)
    next_letter()

print str(range(char_match)) + "/5"

def next_letter():
    if int(range(char_match)) == 5:
        print "You got it!"
    else:
        user_choice = raw_input("Almost, try again: ")




    



