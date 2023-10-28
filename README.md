# **decks** - programmed by tobylockers

Programmed as part of a practice coursework project completed for Year 10 Computer Science, 
**decks** is a a simple terminal-based card game for two players including a set of rules and intergrated scoreboard.

A standard game follows this logic:
  - A deck features 30 cards, with three colours and numbers from 1 to 10 (they are all unique)
  
  - Both players take a card from the top of the deck, until the deck is empty.
  - At the end of each take,
    - If both players have a card of the same colour, the player with the highest number wins
    - If both players have cards with different colours, the winning colour is selected from a table:

      | Card 1 | Card 2 | Winner |
      | ------- | ------ | ------ |
      | Red  | Black  | Red  |
      | Yellow  | Red  | Yellow  |
      | Black  | Yellow  | Black  |

    - The winner takes the other player's card.

At the end of each game, the player with the most cards is the winner. The top players will be shwon on a leaderboard.

Player data can be found in the 'details.json' file.

