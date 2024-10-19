# Задача: є файл test.json. Його вміст:
# { field1: "value1", "animal": "dog" }
# При цьому поле animal може приймати значення: dog, cat, cow, rat, alien.
# Інших полів нема, поле field1
# завжди статичне і має значення value1
# Необхідно зчитати вхідний файл і залежно від значення animal вивести звук тварини,
# відповідно: bark, meow, moo, pipi, KILL

# нижче пропоную вирішення задачі за найпростішим сценарієм.
# В якості іншого варіанту вирішення, я також можу запропонувати
# наступне: нумеруємо кожну тварину и пропонуєму користувачу обрати, звук якої тварини
# треба вивести.

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

