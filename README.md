# Minimax_AI_connect4

An artificial intelligence that always beats you at Connect 4. The AI uses the minimax algorithm in the alpha-beta-pruning version.

### How does it work?

To create the interactive game board I used pygame. 
In order for the AI to analyze the board position, it is represented in code as a numpy matrix.
The AI sees the board and applies minimax algorithm to choose the best move.
The first move for both players is save in the "firstmove1" and "firstmove2" files.

### Let's play

To play you just have to install the requirements and run the _game_vs_ai.py_ file.
You can change the difficulty by going to the _game_vs_ai.py_ file in line 48 and set the _ai_depth_ to a different value. The higher the value, the more difficult the game will be.

You can also play with a friend by running the _game.py_ file.
