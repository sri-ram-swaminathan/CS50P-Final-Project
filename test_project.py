# import the required modules
import pytest
import pokebase
from PIL import Image
from project import pokemon_finder
from project import pokemon_image
from project import pokemon_writer


# test valid input for pokemon_finder
def test_valid_1():
    assert pokemon_finder("fire") != False


# test invalid input for pokemon_finder
def test_invalid_1():
    assert pokemon_finder("muck") == False


# test for valid input for pokemon_image
def test_valid_2():
    pokemon_i = pokebase.pokemon("darkrai")
    assert pokemon_image(pokemon_i) == True


# test for invalid input for pokemon_image
def test_invalid_2():
    pokemon_i = pokebase.pokemon("pickachu")
    assert pokemon_image(pokemon_i) == False


# test for valid input input for pokemon_writer
def test_valid_3():
    card = Image.open("./base/bug.png")
    card.save("card.png")
    pokemon_i = pokebase.pokemon("raichu")
    assert pokemon_writer(pokemon_i) == True


# test for invalid input for pokemon_writer
def test_invalid_3():
    card = Image.open("./base/bug.png")
    card.save("card.png")
    pokemon_i = pokebase.pokemon("pickachu")
    assert pokemon_writer(pokemon_i) == False