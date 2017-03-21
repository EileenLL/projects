import random

# Tip: define all variables as late as possible (e.g. before you need to use them)

def main():
    playing = True
    # correct_answer = False
    while playing:
        correct_answer = False
        intro = raw_input("Would you like to play a guessing game? y/n ")
        if str.lower(intro) == "n":
            playing = False
            print "Goodbye"
        else:
            play_game()
            
def play_game():
    game_list = random.sample(possible_words, 6)
    password = random.choice(game_list)
    print game_list
    # It's better to define correct_answer here
    correct_answer = False
    while not correct_answer: #not False == True
        guess = get_user_guess()
        match_count = count_matching_letters(password, guess)
        print match_count
        if len(password) == match_count:
            print "Yay you got it!"
            correct_answer = True

def get_user_guess(): 
    user_choice = raw_input("What is your guess? ")
    return user_choice
    count_matching_letters(password, user_choice) #don't need

def count_matching_letters(password, user_choice):
    char_match = 0
    for index in range(len(password)):
        if password[index] == user_choice[index]:
            char_match += 1

    return char_match 
    next_letter() #don't need

# def next_letter():
#     if int(range(char_match)) == 5:
#         print "You got it!"
#     else:
#         print str(range(char_match)) + "/5"
#         user_choice = raw_input("Almost, try again: ")

possible_words = ("magma", "merry", "happy", "tacky", "jumpy", 
    "quack", "taxes", "jumbo", "juicy", "fuzzy", 
    "klutz", "crazy", "squad","quilt", "squid", 
    "puppy", "kitty","click")
    # not global variable, make it something that can be passed in to game, make it a file to be imported and read

if __name__ == "__main__":
    main()
    # intro = raw_input("Would you like to play a guessing game? y/n ")

    # if str.lower(intro) == "n":
    #     print "Goodbye"
    # else:
    #     game_list = random.sample(possible_words, 6)
    #     password = random.choice(game_list)
    #     print game_list
       
        # start_game()

    # print str(range(char_match)) + "/5"






    



