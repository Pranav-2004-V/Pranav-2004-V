import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 800
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PADDLE_WIDTH, PADDLE_HEIGHT = 100, 20
BALL_RADIUS = 20
PADDLE_SPEED = 10
BALL_SPEED = 1
FONT = pygame.font.Font(None, 36)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the ball")

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 2 * PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = random.choice((1, -1)) * BALL_SPEED
ball_speed_y = -BALL_SPEED

# Game variables
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update paddle position with mouse position
    mouse_x = pygame.mouse.get_pos()[0]
    paddle.centerx = mouse_x

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:  
        paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:  
        paddle.x += PADDLE_SPEED

    # Update the ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Ball collision with paddle
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -(BALL_SPEED + score * 0.1) # Increase speed as score increases.
        score += 1

    # Ball out of bounds
    if ball.bottom >= HEIGHT:
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the paddle and ball
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, BLUE, ball)

    # Draw the score
    score_text = FONT.render(f"Score: {score}", True, BLUE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

# Game over screen
game_over_text = FONT.render("Game Over", True, BLUE)
screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))
pygame.display.flip()

# Wait for a few seconds before closing
pygame.time.delay(2000)

# Quit Pygame
pygame.quit()
