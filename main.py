import sys, pygame

WIDTH = 400
HEIGHT = 300
BACKGROUND = "#6292d1"


def game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for evant in pygame.event.get():
            if evant.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BACKGROUND)
        pygame.display.flip()

        clock.tick(60)  # FPS


if __name__ == '__main__':
    game()
