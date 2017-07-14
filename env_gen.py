import pygame
import sys
import random

# main graphical parameters
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
CELL_SIZE = 10
START_CELL = (0, 0)
GOAL_CELL = (WINDOW_WIDTH-1, WINDOW_HEIGHT-1)

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


def create_blank_grid(cell_size):
    field_data = {}
    for x in range(cell_size):
        for y in range(cell_size):
            field_data[(x, y)] = 0
    return field_data


def fill_with_obstacles(grid):
    obstacle_num = WINDOW_WIDTH
    rarefaction_seed = 85000
    for cell in grid:
        if obstacle_num == 0:
            return grid
        else:
            # rollin' the dice
            dice = random.randint(0, 100000)
            grid[cell] = (1 if dice > rarefaction_seed else 0)
            obstacle_num -= (1 if gric[cell] == 1 else 0)
    grid[START_CELL] = 2
    grid[GOAL_CELL] = 2
    return grid


def main():
    pygame.init()
    global SCREENSURF
    SCREENSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREENSURF.fill(WHITE)

    field = create_blank_grid(CELL_SIZE)
    fill_with_obstacles(field)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        draw_grid(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


if __name__ == '__main__':
    main()
