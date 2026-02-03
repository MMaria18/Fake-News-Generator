import random

subjects = [
    "Amir Khan ",
    "Virat kohli",
    "A Bunny",
    "A stray cat",
    "Rickshaw Driver From Dhaka",
    "Shakib Khan",
    "Prime Minister"
]

actions=[
    "launches",
    "cancels",
    "dances",
    "orders",
    "declares war on",
    "celebrates",
    "eats"
]

placesOrThings=[
    "at Red Fort",
    "in Dhaka Metro",
    "a plate of samosa",
    "inside parliament",
    "at Ghatpar",
    "during IPl match",
    "at Basundhara gate"
]

while True:
    subject= random.choice(subjects)
    action = random.choice(actions)
    placesOrThing= random.choice(placesOrThings)


    headline =f"BREAKING NEWS: {subject} {action} {placesOrThing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()

    if user_input=="no":
        break
    print("\n Thanks for using fake news generator")