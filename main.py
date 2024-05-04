import pygame

WIDTH: int = 400
HEIGHT: int = 300


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

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                print(mouse_pos)


        screen.fill("black")

        # draw lines
        pygame.draw.line(screen, "yellow", (150, 0), (150, 300))
        pygame.draw.line(screen, "yellow", (250, 0), (250, 300))
        pygame.draw.line(screen, "yellow", (0, 100), (400, 100))
        pygame.draw.line(screen, "yellow", (0, 200), (400, 200))




        # Render game
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

