import random

def main():
    playing = True
    correct_answer = False
    while playing:
        intro = raw_input("Would you like to play a guessing game? y/n ")
        if str.lower(intro) == "n":
            playing = False
            print "Goodbye"
        else:
            game_list = random.sample(possible_words, 6)
            password = random.choice(game_list)
            print game_list
            while not correct_answer: #not False == True
                guess = get_user_guess()
                match_count = count_matching_letters(password, guess)
                print match_count
                if len(password) == match_count:
                    print "Yay you got it!"
                    correct_answer = True
# make 15 while loop own function to call on "play_game" line 19 if pw = match_count own function

def get_user_guess(): 
    user_choice = raw_input("What is your first guess? ")
    return user_choice
    count_matching_letters(password, user_choice)

def count_matching_letters(password, user_choice):
    char_match = 0
    for index in range(len(password)):
        if password[index] == user_choice[index]:
            char_match += 1

    return char_match
    next_letter()

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






    



