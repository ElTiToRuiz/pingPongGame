# Ping Pong Game

This repository contains a simple Ping Pong game implemented using Python and the `pygame` and `tkinter` libraries. The game is designed for two players and includes a graphical user interface (GUI) for setting up the game and a game window for playing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Controls](#controls)
- [Files](#files)
- [Class and Method Descriptions](#class-and-method-descriptions)
  - [PingPong Class](#pingpong-class)
  - [Ball Class](#ball-class)
- [License](#license)

## Features

- **GUI Setup:** A user-friendly setup interface created with `tkinter` to enter player names and target score.
- **Game Window:** A real-time game window created with `pygame`, featuring moving paddles and a ball.
- **Score Tracking:** Real-time score updates and display.
- **Replay Option:** Option to replay the game after it ends.

## Requirements

- Python 3.x
- `pygame` library
- `tkinter` library (included in the standard Python installation)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/SrRuizIgor16/pingPongGame.git
   cd ping-pong-game
2. Create your own environment and activate it:
   ```sh
   python -m venv myenv
   source myenv/bin/activate
   ```
3. Install the required libraries:
    ```sh
   pip install requirements.txt
   ```

## USAGE
1. Run the gui.py script to start the game setup GUI:
   ```sh
   python gui.py
2. Enter the names of the two players and the target score.
3. Click "Start Game" to begin playing.

## Controls
- Player 1 (Top Paddle): Use arrow keys to move the paddle.
- Player 2 (Bottom Paddle): Use WASD keys to move the paddle.

## FILES
- gui.py: Contains the code for the GUI setup.
- pingpong.py: Contains the game logic and implementation using pygame.

## Class and Method Descriptions
### PingPong Class
#### Attributes
- user1_name: Name of player 1.
- user1: Rectangle representing player 1's paddle.
- user2_name: Name of player 2.
- user2: Rectangle representing player 2's paddle.
- screen: The game screen where all elements are drawn.
- ball: The ball used in the game.
- user1_score: Score of player 1.
- user2_score: Score of player 2.
- target: Target score to win the game.

#### Methods
- setup(name, screen_width, screen_height): Initializes the game window and elements.
- welcome(): Displays a welcome message at the start of the game.
- draw_screen(): Draws all game elements on the screen.
- move(): Handles the movement of the paddles based on user input.
- close(): Closes the game and quits the application.
- display_scores(): Displays the current scores of both players.
- final(): Checks if any player has reached the target score and displays the winner.
- ask_play_again(): Asks the players if they want to play again and returns their response.

### Ball Class
#### Attributes
- color: Color of the ball.
- s_w: Width of the screen.
- s_h: Height of the screen.
- ball_radius: Radius of the ball.
- ball_center: Coordinates of the ball's center.
- ball_speed: Speed of the ball in the x and y directions.

#### Methods
- draw_ball(screen): Draws the ball on the given screen.
- move_ball(user1, user2, game): Moves the ball and checks for collisions with the paddles and screen boundaries.
- reset_ball(game): Resets the ball to the center of the screen with a random initial speed.

## LICENSE
This project is licensed under the MIT License - see the LICENSE file for details.
This `README.md` file is now more detailed, covering all essential aspects of your project. Make sure to replace `"SrRuizIgor16"` with your actual GitHub username in the clone command.
