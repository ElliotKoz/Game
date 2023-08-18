# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)

# Add your existing functions here (roll_dice, runway_response, etc.)
def roll_dice():
    return random.randint(1, 6)

def runway_response():
    roll = roll_dice()
    if roll ==1:
        return "Ok Thanks (Non Answer)"
    elif roll ==2:
        return "No"
    elif roll == 3:
        return "Are you a robot? I've seen the same thing a few times this month."
    elif roll ==4:
        return "Give me Proof of funds and send me your offer"
    else:
        return "Make an Offer"

def establish_value_cloqc():
    roll = roll_dice()
    if roll == 1:
        return "They Believe their value is justified"
    elif roll == 2:
        return "What's your offer?"
    elif roll == 3:
        return "No"
    elif roll == 4:
        return "The Bottom Line is x"
    elif roll == 5:
        return "We’ve declined numbers over your number"
    else:
        return "They ask what your needs as a buyer is"

def refuse_to_provide_offer():
    roll = roll_dice()
    if roll in [1, 2, 3]:
        return "They just want this number"
    else:
        return "They CAN’T go down because of X"

def make_stair_step_offer():
    roll = roll_dice()
    if roll == 1:
        return "Offer Accepted (You lose)"
    elif roll == 2:
        return "No We won’t accept a low offer"
    elif roll == 3:
        return "No and ask us to go up"
    elif roll == 4:
        return "Give me a real #"
    elif roll == 5:
        return "Counter offer"
    else:
        return "The bottom line is x"

def make_swag_offer():
    roll = roll_dice()
    if roll == 1:
        return "Offer Accepted (You lose)"
    elif roll == 2:
        return "No We won’t accept a low offer"
    elif roll == 3:
        return "No and ask us to go up"
    elif roll == 4:
        return "We may accept an offer close to that #"
    elif roll == 5:
        return "Counter offer"
    else:
        return "The bottom line is x"

def confirm_number_and_ask_to_lower():
    roll = roll_dice()
    if roll in [1, 2, 3]:
        return "Get Candy"
    else:
        return "No and ask us to go up"

def increase_and_ask_to_counter():
    roll = roll_dice()
    if roll in [1, 2, 3]:
        return "Get Candy"
    else:
        return "No and ask us to go up"

def confirm_counterpart():
    roll = roll_dice()
    if roll in [1, 2, 3, 4]:
        return "Yes"
    else:
        return "No"

def cat_2_response():
    roll = roll_dice()
    if roll == 1:
        return "No"
    elif roll in [2, 3, 4, 5]:
        return "Ask us to make an offer"
    else:
        return "The Bottom Line is X"

def ask_to_lower():
    roll = roll_dice()
    if roll in [1, 2, 3]:
        return "Get Candy (They go lower)"
    else:
        return "No"

def fomo_statement():
    roll = roll_dice()
    if roll in [1, 2, 3, ]:
        return "That’s Right"
    elif roll == 4:
        return "Okay Thanks (Non answer), with justification on price."
    elif roll == 5:
        return "The seller lowers the price"
    else:
        return "No"

def discover():
    roll = roll_dice()
    if roll ==1:
        return "Seller doesn't care about value difference and insists on offer"
    elif roll ==2:
        return "Seller doesn't care about value difference and insists on offer"
    elif roll == 3:
        return "Seller doesn't care about value difference and insists on offer"
    else:
        return "Seller Can't go lower after value beast discussion"


def start_game():
    game_start_state = "Welcome to the Gap Compression Game! You will interact with a seller (the computer) to reach a successful negotiation. The game starts with a randomly selected starting option. Good luck!"
    starting_roll = roll_dice()
    if starting_roll in [1, 2]:
        game_start_state += "\n\nYou Started On: Category 3 Runway Response"
        game_start_state += "\nThe sellers Response is: " + runway_response()
    elif starting_roll == 3:
        game_start_state += "\n\nYou Started On: Category 1: Make a Stair Step Offer"
        game_start_state += "\nThe sellers Response is: " + make_stair_step_offer()
    elif starting_roll in [4, 5]:
        game_start_state += "\n\nYou Started On: Category 1: Make a SWAG Offer"
        game_start_state += "\nThe sellers Response is: " + make_swag_offer()
    else:
        game_start_state += "\n\nYou Started On: Cat 2 Response"
        game_start_state += "\nThe sellers Response is: " + cat_2_response()

    return game_start_state



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    choice = int(request.form.get('choice'))

    # Implement your game logic here based on the user's choice
    # and return the appropriate response
    if choice == 1:
        response = establish_value_cloqc()
    elif choice == 2:
        response = refuse_to_provide_offer()
    elif choice == 3:
        response = make_stair_step_offer()
    elif choice == 4:
        response = make_swag_offer()
    elif choice == 5:
        response = confirm_number_and_ask_to_lower()
    elif choice == 6:
        response = increase_and_ask_to_counter()
    elif choice == 7:
        response = confirm_counterpart()
    elif choice == 8:
        response = ask_to_lower()
    elif choice == 9:
        response = "You left the store. The game is over."
    elif choice == 10:
        response = fomo_statement()
    elif choice == 11:
        response = discover()
    else:
        response = "Invalid choice. Please choose a number between 1 and 10."

    return {'response': response}

@app.route('/start_game', methods=['POST'])
def handle_start_game():
    game_start_state = start_game()
    return {'response': game_start_state}

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)


