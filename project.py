# import the required modules
from pyfiglet import Figlet
import pokebase
import requests
import random
from PIL import Image, ImageFont, ImageDraw
import json
from io import BytesIO


def main():
    try:
        f = Figlet(font="ogre")
        print(f.renderText("Pokemon Card Generator"))
        choice = input(
            "Which pokemon do you want today ? \n 1. Not sure \n 2. I know what I want \n \n"
        ).strip()

        if int(choice) == 1:
            try:
                print()
                print("Ok, I guess I can help you..")
                type = input("What type would you like ? ")
                name_i = pokemon_finder(type)
                if name_i:
                    pokemon_i = pokebase.pokemon(name_i)
                    if pokemon_image(pokemon_i):
                        if pokemon_writer(pokemon_i):
                            print()
                            print("All done :)")
                        else:
                            print("Not a valid pokemon :(")
                    else:
                        print("Not a valid pokemon :(")
                else:
                    print("Not a valid type :(")

            # handles user input that is not a string
            except ValueError:
                print("Please enter valid pokemon attributes :*?!")

        elif int(choice) == 2:
            print()
            name_i = input("Which pokemon did you mean exactly ? ").strip().lower()
            # creates a pokemon object
            pokemon_i = pokebase.pokemon(name_i)
            if pokemon_image(pokemon_i):
                if pokemon_writer(pokemon_i):
                    print()
                    print("All done :)")
                else:
                    print("Not a valid pokemon :(")
            else:
                print("Not a valid pokemon :(")
        # handles integers that are not 1 or 2
        else:
            print("Invalid choice :( pick either 1 or 2.")

    # handles any inputs that aren't integers
    except ValueError:
        print("Invalid choice :( pick either 1 or 2.")


def pokemon_finder(type):
    try:
        # load the data from the website
        data = requests.get(f"https://pokeapi.co/api/v2/type/{type}").json()
        # find the list of pokemons for that type and pick a random one
        n = len(data["pokemon"])
        name_i = data["pokemon"][random.randint(0, n)]["pokemon"]["name"]
        return name_i
    # handles invalid types
    except ValueError:
        return False


def pokemon_image(pokemon_i):
    try:
        # load the data from the pokemon's website
        data = requests.get(pokemon_i.url).json()
        # find the pokemon's first type
        type = data["types"][0]["type"]["name"]
        # make a new image object, and import the correct base image
        card = Image.open(f"./base/{type}.png")
        card = card.convert("RGBA")
        # extract the pokemon's image
        pic = requests.get(pokemon_i.sprites.front_default).content
        # convert it into an Image object
        image = Image.open(BytesIO(pic))
        image = image.convert("RGBA")
        image = image.resize((345, 228))
        # paste this image in the correct location and size
        card.paste(image, (39, 63), image)
        card.save("card.png")
        return True
    # handles pokemon that don't exist
    except KeyError:
        return False


def pokemon_writer(pokemon_i):
    try:
        # collect some parameters from the pokemon object
        name_w = pokemon_i.name
        weight_w = pokemon_i.weight
        id_w = pokemon_i.id
        height_w = pokemon_i.height
        # collect some paramaters from the website
        data = requests.get(pokemon_i.url).json()
        type_w = data["types"][0]["type"]["name"]
        hp_w = data["stats"][0]["base_stat"]
        n = len(data["moves"])
        moves_1 = data["moves"][random.randint(0, n)]["move"]["name"]
        moves_2 = data["moves"][random.randint(0, n)]["move"]["name"]
        # collect the weakness and resistances
        data = requests.get(f"https://pokeapi.co/api/v2/type/{type_w}").json()
        weakness = data["damage_relations"]["double_damage_from"][0]["name"]
        try:
            resistance = data["damage_relations"]["no_damage_from"][0]["name"]
            resistance_image = Image.open(f"./symbols/{resistance}.png")
            resistance_image = resistance_image.convert("RGBA")
            resistance_image = resistance_image.resize((20, 20))
        # handle pokemon that aren't resistant to any type
        except IndexError:
            resistance_image = Image.open(f"./symbols/blank.png")
            resistance_image = resistance_image.convert("RGBA")
            resistance_image = resistance_image.resize((20, 20))
        # convert the weakness and resistance to images
        weakness_image = Image.open(f"./symbols/{weakness}.png")
        weakness_image = weakness_image.convert("RGBA")
        weakness_image = weakness_image.resize((20, 20))
        type_image = Image.open(f"./symbols/{type_w}.png")
        type_image = type_image.convert("RGBA")
        type_image = type_image.resize((20, 20))
        card = Image.open("card.png")
        draw = ImageDraw.Draw(card)
        # setting up required fonts
        font1 = ImageFont.truetype("./fonts/decotura.ttf", 28)
        font2 = ImageFont.truetype("./fonts/decotura.ttf", 20)
        font3 = ImageFont.truetype("./fonts/Arialn.ttf", 14)
        # write the required parameters, in black and save the changes
        draw.text((100, 22), name_w, font=font1, fill=(0, 0, 0))
        draw.text((328, 32), f"HP {hp_w}", font=font2, fill=(0, 0, 0))
        draw.text(
            (140, 290),
            f"NO.{id_w} HT:{height_w}' WT:{weight_w} lbs.",
            font=font3,
            fill=(0, 0, 0),
        )
        card.paste(type_image, (40, 381), type_image)
        draw.text((65, 378.5), moves_1, font=font2, fill=(0, 0, 0))
        card.paste(type_image, (40, 423), type_image)
        draw.text((65, 420.5), moves_2, font=font2, fill=(0, 0, 0))
        card.paste(weakness_image, (47, 513), weakness_image)
        card.paste(resistance_image, (124, 513), resistance_image)
        card.save("card.png")
        return True
    # handles pokemon that don't exist
    except AttributeError:
        return False


if __name__ == "__main__":
    main()
