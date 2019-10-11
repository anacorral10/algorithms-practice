# How to Prevent Duplicates in hashtables example 
# Suppose youre running a voting booth
# Naturally, every person can vote just once
# How do you make sure they havent voted before?
# When someone comes in to vote, you ask for their full name.
# Then you check it against the list of people who have voted
# USE A HASH! 

voted = {}
def check_voter(name):
    # the get function returns the value if the "name" is in the hash table.
    # otherwise it returns none
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")


