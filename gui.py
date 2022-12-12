import pygame


def render(drawing):
    pygame.init()
    BLOCK_SIZE = 5  # Set the size of the grid block
    grid_size = (len(drawing[0]), len(drawing))
    WINDOW_WIDTH = grid_size[0] * BLOCK_SIZE
    WINDOW_HEIGHT = grid_size[1] * BLOCK_SIZE

    # Set up the drawing window
    screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

    # Run until the user asks to quit
    running = True
    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))


        for x in range(0, grid_size[0]):  # WINDOW_WIDTH, BLOCK_SIZE):
            for y in range(0, grid_size[1]):  # WINDOW_HEIGHT, BLOCK_SIZE):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(screen, (220, 220, 220), rect, width=1)
                if drawing[y][x] == '\\':
                    pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE), (x * BLOCK_SIZE + BLOCK_SIZE, y * BLOCK_SIZE + BLOCK_SIZE),
                                     width=2)
                elif drawing[y][x] == '/':
                    pygame.draw.line(screen, (0, 0, 0), (x * BLOCK_SIZE, y * BLOCK_SIZE + BLOCK_SIZE),
                                     (x * BLOCK_SIZE + BLOCK_SIZE, y * BLOCK_SIZE), width=2)

        # Flip the display
        pygame.display.flip()

    # Done! Time to quit.
    pygame.quit()
