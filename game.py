import pygame
import random
import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Smash The Bug!")

game_icon = pygame.image.load("./Resources/bug.png")
pygame.display.set_icon(game_icon)

# Set up starting position for player
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

score = 0
dt = 0

col_detected = False

# Spawn the bug randomly
bug_x = random.randint(0, 720)
bug_y = random.randint(0, 720)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player = pygame.draw.circle(screen, "red", player_pos, 40)

    # Load the image in the game
    img = pygame.image.load("./Resources/bug.png").convert()
    bug = pygame.Rect(bug_x, bug_y, img.get_width(), img.get_height())

    screen.blit(img, (bug_x,bug_y))

    # Programming the controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt
    if keys[pygame.K_SPACE]:
        pygame.draw.circle(screen, "green", player_pos, 40)

        if not col_detected:
            distance = math.sqrt((player_pos.x - (bug_x + img.get_width() // 2))**2 + (player_pos.y - (bug_y + img.get_height() // 2))**2)
            # Detecting collisions with an object
            if distance < 40 + max(img.get_width(), img.get_height()) / 2:
                col_detected = True
                score += 1

                # Reset the position of the bug 
                bug_x = random.randint(0, 720)
                bug_y = random.randint(0, 720)



    # Reseting value for collission detected
    if not keys[pygame.K_SPACE]:
        col_detected = False

    # Detecting wall collisions
    if player_pos.x >= 1280:
        player_pos.x = 1280
    if player_pos.x <= 0:
        player_pos.x = 0
    if player_pos.y >= 720:
        player_pos.y = 720
    if player_pos.y <= 0:
        player_pos.y = 0

    # Display Player's score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
            

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

    