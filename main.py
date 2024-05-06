import pygame

WIDTH: int = 300
HEIGHT: int = 300
SCREEN_COLOR = "black"

GRID_WIDTH = WIDTH // 3
GRID_HEIGHT = HEIGHT // 3

# Define player constants
PLAYER_X = 1
PLAYER_O = 2

# Define game grid
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

def main() -> None:

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tic Tac Toe")
    clock = pygame.time.Clock()
    running: bool = True

    def draw_grid():
        # Vertical lines (Y axis)
        for y in range(1, 3):
            pygame.draw.line(screen, "yellow", (y*GRID_WIDTH, 0), (y*GRID_WIDTH, HEIGHT), 2)

        # Horizontal lines (X axis)
        for x in range(1, 3):
            pygame.draw.line(screen, "red", (0, x*GRID_HEIGHT), (WIDTH, x*GRID_HEIGHT), 2)

    def draw_symbols():
        for row in range(3):
            for col in range(3):
                if grid[row][col] == PLAYER_X:
                    pygame.draw.line(screen, "yellow", (col * GRID_WIDTH + 30, row * GRID_HEIGHT + 30),
                                     ((col + 1)*GRID_WIDTH - 30, (row+1) * GRID_HEIGHT - 30), 3)
                    pygame.draw.line(screen, "yellow", ((col+1)*GRID_WIDTH-30, row*GRID_HEIGHT+30), 
                                     (col*GRID_WIDTH+30, (row+1)*GRID_HEIGHT-30), 3)
                elif grid[row][col] == PLAYER_O:
                    pygame.draw.circle(screen, "red", (col*GRID_WIDTH+GRID_WIDTH // 2, row*GRID_HEIGHT+GRID_HEIGHT//2), 
                                       (GRID_WIDTH//3), 3)

    def check_winner():
        # check rows
        for row in grid:
            if row[0] == row[1] == row[2] and row[0] != 0:
                return row[0]
            
        # check columns
        for col in range(3):
            if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != 0:
                return grid[0][col]
            
        # check diagonals
        if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 0:
            return grid[0][2]
        
        # No winner
        return 0

    def make_moves(row, col, player):
        if grid[row][col] == 0:
            grid[row][col] = player

    current_player = PLAYER_X

    while running:

        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x//GRID_WIDTH
                row = y//GRID_HEIGHT
                if current_player == PLAYER_X:
                    make_moves(row, col, PLAYER_X)
                    # change player
                    current_player = PLAYER_O
                elif current_player == PLAYER_O:
                    make_moves(row, col, PLAYER_O)
                    # change player
                    current_player = PLAYER_X


        screen.fill(SCREEN_COLOR)

        # draw grid lines
        draw_grid()

        # Draw X and O
        draw_symbols()

        # check for winner
        winner = check_winner()
        if winner != 0:
            print("Player", winner, "Wins!")
            running = False
        
        # Render game
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()

