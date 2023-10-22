This is my final project for CS50's Introduction to Programming with Python,
<br>
Pokemon Card Generator.
---

Growing up, I had a pokemon card collection. The very good cards were hard to come by and it was near impossible to catch them all ! Now however .. :) I can finally complete my collection. (well sort of)

[YouTube tutorial](https://youtu.be/7vTrzvf29ZI?si=c2cu77NYoDbCvqvn)

---

- I use [pokeAPI](https://pokeapi.co/) (the coolest pokemon database) in order to extract relevant pokemon features.

- I also use the [pokebase](https://github.com/PokeAPI/pokebase) library and it's wonderful class pokemon.

- The images for the cards come from [LevelInfinitum](https://www.deviantart.com/levelinfinitum/art/Pokemon-Blank-Card-Templates-Stage-2-643173197). The images for the type symbols come from [JorMxDos](https://www.deviantart.com/jormxdos).

`project.py` has 3 functions

`pokemon_finder(type)` :
- This function accepts a type(str) as input and loads all the data about that type.
- Then it finds the list of pokemons of the specified type and returns a random pokemon's name.

`pokemon_image(pokemon_i)` :
- This function accepts a pokemon object (pokebase) as an input and loads all the data about that pokemon.
- It extracts the pokemon's type and default sprite (png image).
- A new image of the corresponding type's card is opened. The pokemon's sprite is then resized and pasted in the centre.
- This image is now saved.

`pokemon_writer(pokemon_i)` :
- This function accepts a pokemon object (pokebase) as an input and loads the previously created image.
- It then extracts the corresponding features about the pokemon : name, weight, id, height, type and hp.
- It then finds the list of the pokemon's moves(which can often times be 100+) and generates 2 random moves.
- It extracts the weakness and resistance of the pokemon, and converts it into the corresponding symbol.
- Lastly, it writes all these attributes using the 2 pokemon fonts onto the correct positions on the card.

The main function gives the user a choice. If the user is unsure about a pokemon, then all of the 3 functions are executed based on a user's type input. Otherwise, the second and third functions are run.

`test_project.py` has 6 functions, that test the working of the functions in `project.py`. 

---

<u>Note</u>

If you make the program generate a random pokemon based on type and the pokemon is generated on another card type, don't worry. This is not a bug, this happens because pokemon can have more than one type !

pokeAPI lists all of the pokemon's types in the dedicated pokemon website. However, the type website lists all pokemon that fullfil a specific type (like fire), which need not be the pokemon's first type.

The code written uses the pokemon's first type in order to find the card and hence the confusion.

Example:

I generate a random grass type pokemon, which yields in swadloon. However, swadloon's first type according to pokeAPI is bug which means it is printed on a bug type base card.

[swadloon](https://drive.google.com/file/d/14Z0iXgC6Qf84rWrQBb9_nqdq1YACV9u1/view?usp=sharing).

---

<u>Improvements</u>

- The final card produced does not show the damage that each attack deals (a crucial feature of pokemon cards), a feature that was missing with pokeAPI. A description of the move is also missing. 
- The hp of the pokemon is different from the one shown in the actual pokemon cards.
- The stage of the pokemon along with the previous stage's (if exists) sprite is mising.
- Small descriptions(text) of the pokemon are missing.
- The program also takes about 5-10 seconds to run. I want to reduce the run time.

In all honesty, I hope I can code (forge) the ultimate pokemon card one day :)

