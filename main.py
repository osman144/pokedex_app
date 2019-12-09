import twilio, flask
from twilio.rest import Client 
import os
# import dotenv
# from dotenv import load_dotenv
# Import requests and Python's core JSON library.
import requests
import json
from flask import Flask, request, redirect, url_for, render_template
from twilio.twiml.messaging_response import MessagingResponse
# from twilio.twiml import Response


# BASEDIR = os.path.abspath(os.path.dirname(__file__))

# load_dotenv(os.path.join(BASEDIR, '.env'))


account_id = os.getenv('twilio_account_sid')
token = os.getenv('twilio_account_authtoken')

# Account Sid and Auth Token from twilio.com/console

twilio_account_sid = account_id
twilio_auth_token = token

# Creating an instance of Flask
app = Flask(__name__)
BASE_URL = 'http://pokeapi.co'

def query_pokeapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None

def pokedex_description(pokemon_species):
    url = '{0}{1}'.format(BASE_URL, pokemon_species)
    response_two = requests.get(url)

    if response_two.status_code == 200:
        return json.loads(response_two.text)
    return None
    
# Render home()
@app.route("/")
def home():
    return render_template("home.html")

# Render incoming message 
# -------------------------------
@app.route("/sms", methods=["GET", "POST"])
def incoming_message():
    twiml = MessagingResponse()

    client = Client(twilio_account_sid, twilio_auth_token)

    body = request.values.get("Body", "").lower().strip().replace(" ","")
    
    pokemon_url = "/api/v2/pokemon/{0}/".format(body)
    pokemon_json = query_pokeapi(pokemon_url)

    # pokemon_index = pokemon_json['game_indices'][0]['game_index']

    pokemon_url_two = "/api/v2/pokemon-species/{0}/".format(body)
    pokemon_json_two = pokedex_description(pokemon_url_two)
    
    if pokemon_json == None:
        msg = twiml.message ("Oops try again")
        return str(twiml)
    elif pokemon_json:

        # description = pokemon_json_two['flavor_text_entries'][1]['flavor_text']

        # Look for English pokedex description
        for i in pokemon_json_two['flavor_text_entries']:
            if i["language"]["name"] == "en":
                description = i["flavor_text"]
                break 

        sprite = pokemon_json['sprites']['front_default']

        msg = twiml.message(description)

        msg.media(sprite)
        
        # client.messages.create(
        #     body = description,
        #     from_ = '+0000000000',
        #     to = '',
        #     media_url = sprite
        # )
        return str(twiml)

if __name__ == "__main__":
    app.run(debug=True)

# incoming_message()