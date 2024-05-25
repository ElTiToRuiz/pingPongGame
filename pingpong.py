import pygame
import sys
import random

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


class PingPong:
	"""
    A class to represent the Ping Pong game.

    Attributes
    ----------
    user1_name : str
        Name of player 1.
    user1 : pygame.Rect
        Rectangle representing player 1's paddle.
    user2_name : str
        Name of player 2.
    user2 : pygame.Rect
        Rectangle representing player 2's paddle.
    screen : pygame.Surface
        The game screen where all elements are drawn.
    ball : Ball
        The ball used in the game.
    user1_score : int
        Score of player 1.
    user2_score : int
        Score of player 2.
    target : int
        Target score to win the game.

    Methods
    -------
    setup(name='Ping Pong Game', screen_width=800, screen_height=700):
        Initializes the game window and elements.
    welcome():
        Displays a welcome message at the start of the game.
    draw_screen():
        Draws all game elements on the screen.
    move():
        Handles the movement of the paddles based on user input.
    close():
        Closes the game and quits the application.
    display_scores():
        Displays the current scores of both players.
    final():
        Checks if any player has reached the target score and displays the winner.
        Returns True if the game is over, otherwise False.
    ask_play_again():
        Asks the players if they want to play again and returns their response.
    """

	def __init__(self, user1='user1', user2='user2', target=1):
		"""
        Constructs all the necessary attributes for the Ping Pong object.

        Parameters
        ----------
        user1 : str
            Name of player 1 (default is 'user1').
        user2 : str
            Name of player 2 (default is 'user2').
        target : int
            Target score to win the game (default is 1).
        """
		self.user1_name = user1
		self.user1 = None
		self.user2_name = user2
		self.user2 = None
		self.screen = None
		self.ball = None
		self.user1_score = 0
		self.user2_score = 0
		self.target = target

	def setup(self, name='Ping Pong Game', screen_width=800, screen_height=700):
		"""
        Sets up the game window, ball, paddles, and other game elements.

        Parameters
        ----------
        name : str
            Title of the game window (default is 'Ping Pong Game').
        screen_width : int
            Width of the game window (default is 800).
        screen_height : int
            Height of the game window (default is 700).
        """
		pygame.init()
		self.screen = pygame.display.set_mode((screen_width, screen_height))
		self.ball = Ball(screen_width, screen_height)
		pygame.display.set_caption(name)
		width = screen_width * 0.75 / 2
		self.user1 = pygame.Rect(width, 50, screen_width * 0.25, 20)
		self.user2 = pygame.Rect(width, screen_height - 70, screen_width * 0.25, 20)
		self.line1 = pygame.Rect(0, screen_height - 2, screen_width, 2)
		self.line2 = pygame.Rect(0, 0, screen_width, 2)
		self.side1 = pygame.Rect(0, 0, screen_width, screen_height / 2)
		self.side2 = pygame.Rect(0, screen_height / 2, screen_width, screen_height / 2)

	def welcome(self):
		"""
        Displays a welcome message at the start of the game.
        """
		font = pygame.font.Font(None, 74)
		reset_text = font.render("Starting...", True, BLACK)
		self.screen.blit(reset_text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 37))
		pygame.display.flip()

	def draw_screen(self):
		"""
        Draws all game elements on the screen.
        """
		self.screen.fill(WHITE)

		# Draw side1 with alpha transparency
		side1_surface = pygame.Surface((self.side1.width, self.side1.height), pygame.SRCALPHA)
		side1_surface.fill((*BLUE, 98))
		self.screen.blit(side1_surface, (self.side1.x, self.side1.y))

		side2_surface = pygame.Surface((self.side2.width, self.side2.height), pygame.SRCALPHA)
		side2_surface.fill((*RED, 98))
		self.screen.blit(side2_surface, (self.side2.x, self.side2.y))

		pygame.draw.rect(self.screen, RED, self.user1)
		pygame.draw.rect(self.screen, BLUE, self.user2)
		self.ball.draw_ball(self.screen)
		pygame.draw.rect(self.screen, GREEN, self.line1)
		pygame.draw.rect(self.screen, GREEN, self.line2)

		self.display_scores()

		pygame.display.flip()

	def move(self):
		"""
        Handles the movement of the paddles based on user input.
        """
		keys = pygame.key.get_pressed()

		# Move user1 (arrow keys)
		if keys[pygame.K_LEFT] and self.user1.left > 0:
			self.user1.move_ip(-1, 0)
		if keys[pygame.K_RIGHT] and self.user1.right < self.screen.get_width():
			self.user1.move_ip(1, 0)
		if keys[pygame.K_UP] and self.user1.top > 0:
			self.user1.move_ip(0, -1)
		if keys[pygame.K_DOWN] and self.user1.bottom < self.screen.get_height() / 2 - 20:
			self.user1.move_ip(0, 1)

		# Move user2 (WASD keys)
		if keys[pygame.K_a] and self.user2.left > 0:
			self.user2.move_ip(-1, 0)
		if keys[pygame.K_d] and self.user2.right < self.screen.get_width():
			self.user2.move_ip(1, 0)
		if keys[pygame.K_w] and self.user2.top > self.screen.get_height() / 2 + 20:
			self.user2.move_ip(0, -1)
		if keys[pygame.K_s] and self.user2.bottom < self.screen.get_height():
			self.user2.move_ip(0, 1)

	def close(self):
		"""
        Closes the game and quits the application.
        """
		pygame.quit()
		sys.exit()

	def display_scores(self):
		"""
        Displays the current scores of both players.
        """
		font = pygame.font.Font(None, 74)
		user1_score_text = font.render(str(self.user1_score), True, BLACK)
		user2_score_text = font.render(str(self.user2_score), True, BLACK)

		self.screen.blit(user1_score_text, (20, self.screen.get_height() // 2 - 84))
		self.screen.blit(user2_score_text, (20, self.screen.get_height() // 2 + 84))

	def final(self):
		"""
        Checks if any player has reached the target score and displays the winner.

        Returns
        -------
        bool
            True if the game is over, otherwise False.
        """
		if self.user1_score >= self.target:
			text = f'{self.user1_name} won!'
		elif self.user2_score >= self.target:
			text = f'{self.user2_name} won!'
		else:
			return False  # Continue the game

		font = pygame.font.Font(None, 74)
		reset_text = font.render(text, True, BLACK)
		self.screen.blit(reset_text, (self.screen.get_width() // 2 - 100, self.screen.get_height() // 2 - 37))
		pygame.display.flip()
		pygame.time.wait(3000)
		return True  # Game over

	def ask_play_again(self):
		"""
        Asks the players if they want to play again and returns their response.

        Returns
        -------
        bool
            True if players choose to play again, otherwise False.
        """
		font = pygame.font.Font(None, 74)
		ask_text = font.render("Play again? (Y/N)", True, BLACK)
		self.screen.fill(WHITE)
		self.screen.blit(ask_text, (self.screen.get_width() // 2 - 200, self.screen.get_height() // 2 - 37))
		pygame.display.flip()

		waiting = True
		while waiting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.close()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_y:
						return True
					elif event.key == pygame.K_n:
						return False


class Ball:
	"""
    A class to represent the ball in the Ping Pong game.

    Attributes
    ----------
    color : tuple
        Color of the ball.
    s_w : int
        Width of the screen.
    s_h : int
        Height of the screen.
    ball_radius : int
        Radius of the ball.
    ball_center : list
        Coordinates of the ball's center.
    ball_speed : list
        Speed of the ball in the x and y directions.

    Methods
    -------
    draw_ball(screen):
        Draws the ball on the given screen.
    move_ball(user1, user2, game):
        Moves the ball and checks for collisions with the paddles and screen boundaries.
        Updates scores and resets the ball if a point is scored.
    reset_ball(game):
        Resets the ball to the center of the screen with a random initial speed.
    """

	def __init__(self, screen_width, screen_height, ball_radius=10, color=BLACK):
		"""
        Constructs all the necessary attributes for the Ball object.

        Parameters
        ----------
        screen_width : int
            Width of the game screen.
        screen_height : int
            Height of the game screen.
        ball_radius : int
            Radius of the ball (default is 10).
        color : tuple
            Color of the ball (default is BLACK).
        """
		self.color = color
		self.s_w = screen_width
		self.s_h = screen_height
		self.ball_radius = ball_radius
		self.ball_center = [(self.s_w - self.ball_radius) / 2 + random.randrange(0, 6),
		                    (self.s_h - self.ball_radius) / 2 + random.randrange(0, 6)]
		self.ball_speed = [random.choice([-1, 1]), random.choice([-1, 1])]

	def draw_ball(self, screen):
		"""
        Draws the ball on the given screen.

        Parameters
        ----------
        screen : pygame.Surface
            The game screen where the ball is drawn.
        """
		pygame.draw.circle(screen, self.color, self.ball_center, self.ball_radius)

	def move_ball(self, user1, user2, game):
		"""
        Moves the ball and checks for collisions with the paddles and screen boundaries.
        Updates scores and resets the ball if a point is scored.

        Parameters
        ----------
        user1 : pygame.Rect
            Rectangle representing player 1's paddle.
        user2 : pygame.Rect
            Rectangle representing player 2's paddle.
        game : PingPong
            The Ping Pong game instance.

        Returns
        -------
        bool
            True if the game is over, otherwise False.
        """
		self.ball_center[0] += self.ball_speed[0]
		self.ball_center[1] += self.ball_speed[1]

		ball_rect = pygame.Rect(self.ball_center[0] - self.ball_radius, self.ball_center[1] - self.ball_radius,
		                        self.ball_radius * 2, self.ball_radius * 2)

		# Check for collision with the screen boundaries
		if self.ball_center[0] <= self.ball_radius or self.ball_center[0] >= self.s_w - self.ball_radius:
			self.ball_speed[0] = -self.ball_speed[0]
		if self.ball_center[1] <= self.ball_radius:
			game.user2_score += 1
			if game.final():
				return True
			self.reset_ball(game)
		if self.ball_center[1] >= self.s_h - self.ball_radius:
			game.user1_score += 1
			if game.final():
				return True
			self.reset_ball(game)

		if ball_rect.colliderect(user1):
			self.ball_speed[1] = -self.ball_speed[1]
			self.ball_speed[0] += random.choice([-1, 1])

		if ball_rect.colliderect(user2):
			self.ball_speed[1] = -self.ball_speed[1]
			self.ball_speed[0] += random.choice([-1, 1])
		return False

	def reset_ball(self, game):
		"""
        Resets the ball to the center of the screen with a random initial speed.

        Parameters
        ----------
        game : PingPong
            The Ping Pong game instance.
        """
		font = pygame.font.Font(None, 74)
		reset_text = font.render("Resetting...", True, BLACK)
		game.screen.blit(reset_text, (game.screen.get_width() // 2 - 100, game.screen.get_height() // 2 - 37))
		pygame.display.flip()

		pygame.time.wait(3000)

		self.ball_center = [(self.s_w - self.ball_radius) / 2 + random.randint(0, 6),
		                    (self.s_h - self.ball_radius) / 2 + random.randint(0, 6)]
		self.ball_speed = [random.choice([-1, 1]), random.choice([-1, 1])]


def start(user1='user1', user2='user2', target=5):
	"""
    Starts the Ping Pong game with the given user names and target score.
    Sets up the game, displays the welcome message, and runs the game loop.

    Parameters
    ----------
    user1 : str
        Name of player 1 (default is 'user1').
    user2 : str
        Name of player 2 (default is 'user2').
    target : int
        Target score to win the game (default is 5).
    """
	game = PingPong(user1=user1, user2=user2, target=target)
	game.setup()
	game.draw_screen()
	game.welcome()
	pygame.time.wait(1500)
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		game.move()
		if game.ball.move_ball(game.user1, game.user2, game):
			again = game.ask_play_again()
			if again:
				game.user1_score = 0
				game.user2_score = 0
				game.setup()
			else:
				running = False
		game.draw_screen()

	game.close()


def main():
	"""
    The main function to initialize the game.
    """
	pass


if __name__ == '__main__':
	main()