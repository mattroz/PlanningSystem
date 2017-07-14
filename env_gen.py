import pygame
import sys
import random

# main graphical parameters
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640
CELL_SIZE = 10
CELL_AMOUNT_X = WINDOW_WIDTH // CELL_SIZE
CELL_AMOUNT_Y = WINDOW_HEIGHT // CELL_SIZE
START_CELL = (0, 0)
GOAL_CELL = (CELL_AMOUNT_X-1, CELL_AMOUNT_Y-1)

assert ((WINDOW_WIDTH % CELL_SIZE == 0) and (WINDOW_HEIGHT % CELL_SIZE == 0)), "Change cell size"

# colors definition
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


# fill cells with colors
def draw_grid(field, window_w, window_h, cell_size):
    for i in range(0, CELL_AMOUNT_X):
        for j in range(0, CELL_AMOUNT_Y):
            current_cell = (i, j)
            if field[current_cell] == 0:
                color_cell(current_cell, WHITE)
            elif field[current_cell] == 1:
                color_cell(current_cell, BLUE)
            elif field[current_cell] == 2:
                color_cell(current_cell, RED)


# generate blank grid
def create_blank_grid():
    field_data = {}
    for i in range(CELL_AMOUNT_X):
        for j in range(CELL_AMOUNT_Y):
            field_data[(i, j)] = 0
    return field_data


# TODO: should call constants either as arguments or as global variables!
def fill_with_obstacles(grid, rarefaction):
    obstacle_num = WINDOW_WIDTH
    for cell in grid:
        if obstacle_num == 0:
            return grid
        else:
            # rollin' the dice
            dice = random.randint(0, 100000)
            grid[cell] = (1 if dice > rarefaction else 0)
            obstacle_num -= (1 if grid[cell] == 1 else 0)
    grid[START_CELL] = 2
    grid[GOAL_CELL] = 2
    return grid


def color_cell(cell, color):
    _x = cell[0] * CELL_SIZE
    _y = cell[1] * CELL_SIZE
    pygame.draw.rect(SCREENSURF, color, (_x, _y, CELL_SIZE, CELL_SIZE))


def main():
    pygame.init()
    global SCREENSURF
    SCREENSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREENSURF.fill(WHITE)

    field = create_blank_grid()
    fill_with_obstacles(field, 85000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        draw_grid(field, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)


if __name__ == '__main__':
    main()
