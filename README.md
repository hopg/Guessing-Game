# Guessing Game
Simple game where the computer will attempt to guess the player's number. 

The computer's programatic guessing is influenced by [binary searching](https://en.wikipedia.org/wiki/Binary_search_algorithm).  

## How to Play
- The player will first be asked to input a higher bound for their guess. This is the highest number the computer can guess up to. 
- Next, the player will input the number the computer will have to guess, this must be 0 or greater and below the higher bound.
- The computer will now present a guess and the player will be asked to input whether their number is higher or lower.
- The game will continue in this fashion until the computer guesses the number correctly.

## Game Mechanics
- The game will function correctly for a higher bound b that is an integer satisfying b > 0, that is, choosing a very large higher bound will not cause the game to break. Higher numbers however, have the ability for the game to run for a longer period of time.
- The player will be notified if they have incorrectly input higher or lower when it was indeed the opposite.
- The number of guesses and the guesses themselves will be presented to the player at the end. 
- For inputs requiring a positive integer, there is error handling so as to ensure the game does not break in case of a bad input.
- There is debugging code contained at the bottom of the script that allows the user to see what guess corresponds to which turn. 
