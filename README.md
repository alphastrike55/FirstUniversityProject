# Map Guessing Game by Gleb Tretiakov

## Introduction

## File and directory structure

  Launch main.py
-map.py handles the map window
-gui.py handles the main menu
-gamemode_outline.py handles the game window

## Installation instructions

  Used libraries: PyQt6, sys, random
  - Installation instructions for the libraries:
      - Install python 3
      - Open cmd
      - write "pip install PyQt6"

## User instructions

  launch main.py
After it you can press "Open map" to enter the interactive map and find information about countries.
Also, you can press "Play" to open a window with a game. To start game press "Start game", after it the button will be disabled while you are playing.
You will be provided with an outline on which you should answer using a radio buttons. If you answer incorrectly you will be provided with a hint.
Depending on how many incorrect answers you gave, the points for the correct answer will be deducted. 0 incorrect answer - 1 point, 1 incorrect answer - 0.75 points, 2 incorrect answer - 0.5, 3+ incorrect answer - 0 points
After the game you will be provided with a map with only enabled countries which were in the game session.

After finishing you can either play again, open the map again, or press "Exit" to close the app