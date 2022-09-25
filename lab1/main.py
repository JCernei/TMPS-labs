from lion import Lion
from mouse import Mouse
from snake import Snake

def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())

def animal_description(animals: list):
    for animal in animals:
        print(animal.get_name(), animal.get_danger_level())

animals = [
    Lion('Simba'),
    Mouse('Jerry'),
    Snake('Python'),
]

# animal_sound(animals)
animal_description(animals)