import pygame

WIDTH: int = 800 
HEIGHT: int = 600


def main() -> None:

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    running: bool = True
    while running:

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill("orange")
        # pygame.draw.rect(screen, color="white", rect=(50, 100, 150, 150))
        # pygame.draw.rect(screen, color="white", rect=(300, 100, 150, 150))
        # pygame.draw.rect(screen, color="white", rect=(550, 100, 150, 150))

        


        # Render game
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

