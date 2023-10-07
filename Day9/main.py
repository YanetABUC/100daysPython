#from replit import clear
from art import logo


#HINT: You can call clear() to clear the output in the console.
def find_highest_bid(bids_list):
    winner_name = ""
    highest_bid = 0

    for key in bids_list:
        if bids_list[key] > highest_bid:
            winner_name = key
            highest_bid = bids_list[key]

    print(f"The winner is {winner_name} with a bid of ${highest_bid}")


print(logo)
print("Welcome to the secret auction program.")
bids_list = {}
end_program = False

while not end_program:
    name = input("What is your name?: ")
    bid = float(input("What is your bid? $"))
    bids_list[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no': ") == "no":
        end_program = True
        clear()
        find_highest_bid(bids_list)
    else:
        #clear() - Clear the console
        pass
