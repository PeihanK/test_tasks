import json


with open("test.json", "r") as file:
    data = json.load(file)

animal_say = {
    "dog": "bark",
    "cat": "meow",
    "cow": "moo",
    "rat": "pipi",
    "alien": "KILL"
}

animal = data.get("animal")
voice = animal_say.get(animal)

print(f"{animal} say {voice}")

