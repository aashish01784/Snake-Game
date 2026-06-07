import pygame
import sys
import random
import Display
import Start_screen

# from Initial_Conditions import snake_size as snake_size

# Initialize Pygame
pygame.init()
pygame.mixer.init()


# Window settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game 🐍")

# Load Sounds
eat_sound = pygame.mixer.Sound("food.mp3")
gameover_sound = pygame.mixer.Sound("gameover.wav")

#fonts
font = pygame.font.SysFont("Segoe UI Emoji", 20)

# Game constants
snake_size = 20
snake_color = (0, 255, 0)
food_color = (255, 0, 0)
bg_color = (0, 0, 0)

clock = pygame.time.Clock()

# Snake and food setup
snake_pos = [[100, 40]]
direction = 'RIGHT'
food_x = random.randint(0, (Display.WIDTH - snake_size) // snake_size) * snake_size
food_y = random.randint(0, (Display.HEIGHT - snake_size) // snake_size) * snake_size

# Game state
score = 0
h_score = 0
game_state = "start"

#helper func's

def show_score():
    font_small = pygame.font.SysFont("Courier New", 15)
    text = font_small.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, [10, 10])

def show_pause_screen():
    pause_Font = pygame.font.SysFont("Arial", 40)
    pause_text = pause_Font.render("Paused - Press R to Resume", True, (255, 255, 255))
    screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - pause_text.get_height() // 2))
    pygame.display.update()


def show_game_over():
    global game_state, score, snake_pos, direction, food_x, food_y, h_score
    gameover_sound.play()
    screen.blit(Start_screen.start_bg,(0,0))
    over_Font = pygame.font.SysFont("Comic Sans MS", 50)
    msga = over_Font.render("_________", True, (255, 0,0)) 
    msg1 = over_Font.render("|Game Over|", True, (255, 0,0))
    msgb = over_Font.render("_________", True, (255, 0,0))
    msg2 = font.render(f"Score: {score}", True, (0, 255, 255))
    msg3 = font.render(f"🏆High score: {h_score}", True, (0, 255, 255))
    msg4 = font.render("Press SPACE to Restart or ESC to Quit", True, (255, 255, 255))
    screen.blit(msga, msga.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
    screen.blit(msg1, msg1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
    screen.blit(msga, msga.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50)))
    screen.blit(msg2, msg2.get_rect(center=(WIDTH // 2, HEIGHT // 2 +10)))
    screen.blit(msg3, msg3.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 38)))
    screen.blit(msg4, msg4.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 85)))
    pygame.display.update()
    waiting=True
    while waiting:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    score = 0
                    snake_pos = [[100, 40]]
                    direction = 'RIGHT'
                    food_x = random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size
                    food_y = random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size
                    game_state = "play"
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


# Game starts #
running = True
while running:
    Display.draw_background_grid()

    if game_state == "start":
        Start_screen.show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state = "play"

    elif game_state == "pause":
        Start_screen.show_pause_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                game_state = "play"

    elif game_state == "play":
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_p:
                    game_state = "pause"

        # Move snake
        head_x, head_y = snake_pos[0]
        if direction == 'RIGHT':
            head_x += snake_size
        elif direction == 'LEFT':
            head_x -= snake_size
        elif direction == 'UP':
            head_y -= snake_size
        elif direction == 'DOWN':
            head_y += snake_size
        new_head = [head_x, head_y]

        # Collision detection
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake_pos
        ):
            if score > h_score:
                h_score = score
            show_game_over()
            game_state = "start"
            score = 0
            snake_pos = [[100, 40]]
            direction = 'RIGHT'
            food_x = random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size
            food_y = random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size
            continue

        snake_pos.insert(0, new_head)

        # Food check
        if head_x == food_x and head_y == food_y:
            score += 1
            eat_sound.play()
            food_x = random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size
            food_y = random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size
        else:
            snake_pos.pop()

        # Draw snake
        for segment in snake_pos:
            pygame.draw.rect(screen, snake_color, pygame.Rect(segment[0], segment[1], snake_size, snake_size))

        # Draw food as emoji
        food_emoji = font.render("🍎", True, (255, 255, 255))
        screen.blit(food_emoji, (food_x-3.5, food_y ))

        show_score()
        pygame.display.update()

pygame.quit()
sys.exit()
