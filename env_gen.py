import pygame
import sys
import random
import os
from time import sleep

# main graphical parameters
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 900
CELL_SIZE = 10
CELL_AMOUNT_X = WINDOW_WIDTH // CELL_SIZE
CELL_AMOUNT_Y = WINDOW_HEIGHT // CELL_SIZE
START_CELL = (1, 1)
GOAL_CELL = (CELL_AMOUNT_X - 2, CELL_AMOUNT_Y - 2)

assert ((WINDOW_WIDTH % CELL_SIZE == 0) and (WINDOW_HEIGHT % CELL_SIZE == 0)), "Change cell size"

# colors definition
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
TURQUOISE = (102, 255, 255)


# fill cells with colors
def draw_grid(field, window_w, window_h, cell_size):
    for i in range(0, CELL_AMOUNT_X):
        for j in range(0, CELL_AMOUNT_Y):
            current_cell = (i, j)
            if field[current_cell] == 0:
                color_cell(current_cell, WHITE)
            elif field[current_cell] == 1:
                color_cell(current_cell, BLUE)
            elif field[current_cell] == 2 or field[current_cell] == 3:
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
    obstacle_num = WINDOW_WIDTH**2 - WINDOW_HEIGHT
    # generate obstacles according to rarefaction seed
    for cell in grid:
        # make some kind of border for the field
        if (cell[0] == 0) or (cell[0] == CELL_AMOUNT_X - 1) \
                or (cell[1] == 0) or (cell[1] == CELL_AMOUNT_Y - 1):
            grid[cell] = 1
        elif obstacle_num == 0:
            return grid
        else:
            # rollin' the dice
            dice = random.randint(0, 100000)
            grid[cell] = (1 if dice > rarefaction else 0)
            obstacle_num -= (1 if grid[cell] == 1 else 0)

    grid[START_CELL] = 2
    grid[GOAL_CELL] = 3
    return grid


def color_cell(cell, color):
    _x = cell[0] * CELL_SIZE
    _y = cell[1] * CELL_SIZE
    pygame.draw.rect(SCREENSURF, color, (_x, _y, CELL_SIZE, CELL_SIZE))


def depth_first_search(field, visits_grid, parents_grid, current_cell, goal_cell):
    sleep(0.03)
    pygame.display.update()
    if field[current_cell[0], current_cell[1]] == field[goal_cell[0], goal_cell[1]]:
        print("Goal've been achieved")
        path_recovery(parents_grid, current_cell, START_CELL)
        exit()
    # down, right, up, left
    x_direction = [0, 1, 0, -1]
    y_direction = [1, 0, -1, 0]
    directions = len(x_direction)
    visits_grid[current_cell[0], current_cell[1]] = 1
    color_cell(current_cell, TURQUOISE)
    for step in range(directions):
        neighbour = (current_cell[0] + x_direction[step], current_cell[1] + y_direction[step])
        if (field[neighbour] == 0 or field[neighbour] == 3) \
                and visits_grid[neighbour] != 1:
            parents_grid[neighbour] = current_cell
            depth_first_search(field, visits_grid, parents_grid, neighbour, goal_cell)


# recover path from goal cell to the start cell
def path_recovery(parents_grid, current_cell, dest_cell):
    color_cell(current_cell, RED)
    sleep(0.03)
    pygame.display.update()
    if current_cell == dest_cell:
        sleep(3)
        exit(0)
    path_recovery(parents_grid, parents_grid[current_cell], dest_cell)


def main():
    pygame.init()
    sys.setrecursionlimit(1500)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0, 0)
    global SCREENSURF
    SCREENSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    SCREENSURF.fill(WHITE)

    visits = {}
    parents = {}
    for x in range(CELL_AMOUNT_X):
        for y in range(CELL_AMOUNT_Y):
            visits[(x, y)] = 0
            parents[(x, y)] = [0, 0]
    field = create_blank_grid()
    fill_with_obstacles(field, 65000)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        draw_grid(field, WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
        depth_first_search(field, visits, parents, START_CELL, GOAL_CELL)

if __name__ == '__main__':
    main()
