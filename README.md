**Snake Game
**

A Python-based Snake game implemented with Pygame, featuring both AI and manual gameplay modes. This project is part of a group assignment to develop a game incorporating pathfinding algorithms, specifically Breadth-First Search (BFS), for academic evaluation. The game includes a user-friendly interface, real-time statistics, and performance analysis, developed incrementally to demonstrate individual contribution.

Features





**Gameplay Modes:
**




AI Mode: Uses BFS for pathfinding to the apple, with virtual snake simulation to avoid collisions.



Manual Mode: Player-controlled movement using arrow keys or WASD.



User Interface: Menu system with buttons for mode selection, statistics view, and game controls (pause/resume, restart).



Statistics: Tracks session and all-time stats (games played, wins, scores, efficiency) with comparative analysis between AI and manual modes.



Game Mechanics: Snake growth, apple generation, collision detection, and win/timeout conditions.



Performance Analysis: Comprehensive metrics including win rate, average score, and efficiency, presented in a dedicated statistics screen.

Project Structure





setting.py: Contains game constants (dimensions, colors, settings) and pathfinding utilities (grid, neighbors, distance).



snake.py: Implements the Square and Snake classes for game logic, including movement, AI pathfinding, and apple handling.



play.py: Manages the game loop, UI (menu, buttons, stats display), and performance analysis via SnakeGame, Button, GameStats, and GameAnalyzer classes.









**Prerequisites:**





Python 3.6+



Pygame library: Install with pip install pygame



Clone the Repository:

git clone https://github.com/your-username/snake-game.git
cd snake-game



Run the Game:

python play.py



Controls:





Manual Mode: Use arrow keys or WASD to move the snake.



Menu: Click buttons to select mode, view stats, or quit.



Game: Click "Pause/Resume" to pause, "Restart" to reset, or "Menu" to return.
