import pygame
from typing import Optional

WIDTH: int = 400
HEIGHT: int = 300


def main() -> None:

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    running: bool = True

    # Button class

    # class Button:

    #     def __init__(self, x: int, y: int, width: int, height: int, text: Optional[str]=None, action=None) -> None:
    #         self.rect = pygame.Rect(x, y, width, height)
    #         self.color = (0, 0, 0)
    #         self.text = text
    #         self.action = action

    #     def draw(self, screen) -> None:
    #         pygame.draw.rect(screen, self.color, self.rect)
    #         # font = pygame.font.SysFont(None, 20)
    #         # text = font.render(self.text, True, WHITE)
    #         # text_rect = text.get_rect(center=self.rect.center)
    #         # screen.blit(text, text_rect)

    #     def is_clicked(self, pos) -> bool:
    #         return self.rect.collidepoint(pos)
        
    #     # create buttons

    # top_left = Button(50, 50, 70, 50)
    # top_middle = Button(150, 50, 70, 50)
    # top_right = Button(250, 50, 70, 50)
    # middle_left = Button(50, 120, 70, 50)
    # middle = Button(150, 120, 70, 50)
    # middle_right = Button(250, 120, 70, 50)
    # bottom_left = Button(50, 190, 70, 50)
    # bottom_middle = Button(150, 190, 70, 50)
    # bottom_right = Button(250, 190, 70, 50)

    while running:

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     mouse_pos = event.pos  # gets mouse position

            #     # checks if mouse position is over the button

            #     if button.collidepoint(mouse_pos):
            #         # prints current location of mouse
            #         print(f'button was pressed at {mouse_pos}')


        screen.fill("black")
        
        # create buttons
        # top_left.draw(screen)
        # top_middle.draw(screen)
        # top_right.draw(screen)
        # middle_left.draw(screen)
        # middle.draw(screen)
        # middle_right.draw(screen)
        # bottom_left.draw(screen)
        # bottom_middle.draw(screen)
        # bottom_right.draw(screen)

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

