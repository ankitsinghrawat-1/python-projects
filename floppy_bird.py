import pygame
import random
import sys
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Floppy Bird")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GREEN = (0, 200, 0)
RED = (240, 0, 0)
FPS = 60
GRAVITY = 0.5
BIRD_JUMP_VELOCITY = -8
PIPE_SPEED = 4
PIPE_GAP = 150
PIPE_FREQUENCY = 1500
FONT = pygame.font.SysFont("Arial", 32)
class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.velocity = 0
        self.width = 34
        self.height = 24
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        self.velocity = BIRD_JUMP_VELOCITY

    def move(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = int(self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)
class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 52
        self.height = random.randint(50, SCREEN_HEIGHT - PIPE_GAP - 50)
        self.top_rect = pygame.Rect(self.x, 0, self.width, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, self.width, SCREEN_HEIGHT - (self.height + PIPE_GAP))

    def move(self):
        self.x -= PIPE_SPEED
        self.top_rect.x = int(self.x)
        self.bottom_rect.x = int(self.x)

    def draw(self, screen):
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

    def off_screen(self):
        return self.x + self.width < 0
def main():
    clock = pygame.time.Clock()
    bird = Bird()
    pipes = []
    score = 0
    running = True
    last_pipe_time = pygame.time.get_ticks()
    game_over = False

    while running:
        clock.tick(FPS)
        SCREEN.fill(SKY_BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not game_over:
                    bird.jump()
                if event.key == pygame.K_r and game_over:
                    main()
                    return

        if not game_over:
            bird.move()

          
            current_time = pygame.time.get_ticks()
            if current_time - last_pipe_time > PIPE_FREQUENCY:
                pipes.append(Pipe(SCREEN_WIDTH))
                last_pipe_time = current_time
            for pipe in pipes[:]:
                pipe.move()
                if pipe.off_screen():
                    pipes.remove(pipe)
                    score += 1
            for pipe in pipes:
                if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                    game_over = True
                    break
            if bird.y > SCREEN_HEIGHT - bird.height or bird.y < 0:
                game_over = True
        bird.draw(SCREEN)
        for pipe in pipes:
            pipe.draw(SCREEN)
        score_text = FONT.render(f"Score: {score}", True, BLACK)
        SCREEN.blit(score_text, (10, 10))

        if game_over:
            game_over_text = FONT.render("Game Over! Press R to Restart", True, BLACK)
            SCREEN.blit(game_over_text, (20, SCREEN_HEIGHT // 2 - 20))

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
