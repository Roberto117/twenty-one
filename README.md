# Twenty-one

Python project for the game twenty-one,
which implements a tmall data gatherer.

```
.
├── README.md
├── twenty-one.py
├── Assigment-ENG.pdf
├── Player
|   ├── __init__.py
|   ├── player.py
|   ├── hand.py
|   └── Test
|         └── __init__.py
└── Deck
    ├── __init__.py
    ├── card.py
    ├── deck.py
    └── Test
          ├── __init__.py
          └──__main__.py

```


## Run

To run the  script you cd into the twenty-one directory and run the following command

```
python3 twenty-one.py
```
This will run the code in `./twenty-one.py`.

Alternatively to do a unit test on the Deck module you can the following command
```
 python3 -m Deck.Test
```
This will run the code at `./Deck/Test/__main__.py`



## Todo
-Create unit test for the player class and the hand class
-allow for more then 3 players, will need to increase deck size(and edit the unit test to fit the new deck once modified)

