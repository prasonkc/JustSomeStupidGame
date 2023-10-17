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

hammar = pygame.image.load("./Resources/hammar_up.png").convert_alpha()

score = 0
dt = 0

col_detected = False

# Spawn the bug randomly
bug_x = random.randint(30, 670)
bug_y = random.randint(30, 670)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    # Load the image in the game
    img = pygame.image.load("./Resources/bug.png").convert_alpha()

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
        if not col_detected:
            distance = math.sqrt((player_pos.x - (bug_x + img.get_width() // 2))**2 + (player_pos.y - (bug_y + img.get_height() // 2))**2)
            # Detecting collisions with an object
            if distance < 40 + max(img.get_width(), img.get_height()) / 2:
                col_detected = True
                score += 1

                # Reset the position of the bug 
                bug_x = random.randint(30, 670)
                bug_y = random.randint(30, 670)
                
                hammar = pygame.image.load("./Resources/hammar_down.png").convert_alpha()
    else:
        hammar = pygame.image.load("./Resources/hammar_up.png").convert_alpha()

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

    # Moving the enemy
    bug_displacement = score/10
    bug_y += bug_displacement
    if bug_y > 670:
        game_over_text = font.render(f'GAME OVER!', True, (255, 255, 255))
        screen.blit(game_over_text, (500, 360))

        # Rectangle parameters
        x, y = 480, 410  # Position of the top-left corner of the rectangle
        width, height = 200, 100  # Width and height of the rectangle
        color = (0, 255, 0)  # RGB color 
        rect = pygame.draw.rect(screen, color, (x, y, width, height))

        replay_text = font.render("Replay!", True, (255,255,255))
        screen.blit(replay_text, (520, 450))

        if keys[pygame.K_SPACE]:
            distance = math.sqrt((player_pos.x - (x + width // 2))**2 + (player_pos.y - (y + height// 2))**2)
            if distance < 40 + max(width, height) / 2:
                color = (255, 0, 0)
                score = 0

                screen.fill("black")
                bug_x = random.randint(30, 670)
                bug_y = random.randint(30, 670)
                continue
        


        
    # Draw the player
    screen.blit(hammar, (player_pos.x, player_pos.y))


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

    