from flask import Flask, render_template
import random

app = Flask(__name__)

subjects = [
    "Amir Khan",
    "Virat Kohli",
    "A Bunny",
    "A stray cat",
    "A rickshaw driver from Dhaka",
    "Shakib Khan",
    "Prime Minister"
]

actions = [
    "launches",
    "cancels",
    "dances",
    "orders",
    "declares war on",
    "celebrates",
    "eats"
]

places_or_things = [
    "at Red Fort",
    "in Dhaka Metro",
    "a plate of samosa",
    "inside parliament",
    "at Ghatpar",
    "during IPL match",
    "at Basundhara Gate"
]

@app.route("/")
def home():
    headline = f"{random.choice(subjects)} {random.choice(actions)} {random.choice(places_or_things)}"
    return render_template("index.html", headline=headline)

if __name__ == "__main__":
    app.run(debug=True)
