import pygame
import sys

# main graphical parameters
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
CELL_SIZE = 10

assert ((WINDOW_WIDTH % CELL_SIZE == 0) and (WINDOW_HEIGHT % CELL_SIZE == 0)), "Change cell size"

# colors definition
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_grid(window_w, window_h, cell_size):
    for x in range(0, window_w, cell_size):
        pygame.draw.line(SCREENSURF, BLACK, (x, 0), (x, window_h))
    for y in range(0, window_h, cell_size):
        pygame.draw.line(SCREENSURF, BLACK, (0, y), (window_w, y))


def main():
    pygame.init()
    global SCREENSURF
    SCREENSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREENSURF.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

if __name__ == '__main__':
    main()
