import pygame
import sys
import random

BLACK = (0,0,0)
CYAN = (0,255,255)
GRAY = (96,96,96)

MAZE_W = 11
MAZE_H = 9
maze = []
for y in range(MAZE_H):
    maze.append([0] * MAZE_W)

DUNGEON_W = MAZE_W * 3
DUNGEON_H = MAZE_H * 3
dungeon = []
for y in range(DUNGEON_H):
    maze.append([0] * MAZE_W)

imgWall = pygame.image.load("wall.png")
imgFloor = pygame.image.load("floor.png")

def make_maze():
    xp = [0,1,0,-1]
    yp = [-1,0,1,0]

    for x in range(MAZE_W):
        maze[0][x] = 1
        maze[MAZE_H - 1][x] = 1
    for y in range(1, MAZE_H - 1):
        maze[y][0] = 1
        maze[y][MAZE_W - 1] = 1

    for y in range(1,MAZE_H-1):
        for x in range(1, MAZE_W-1):
            maze[y][x] = 0

    for y in range(2, MAZE_H -2, 2):
        for x in range(2, MAZE_W - 2, 2):
            maze[y][x] = 1

    for y in range(2, MAZE_H -2, 2):
        for x in range(2, MAZE_W - 2, 2):
            d = random.randint(0,3)
            if x > 2:
                d = random.randint(0,2)
            maze[y+yp[d]][x+xp[d]] = 1

    for y in range(DUNGEON_H):
        for x in range(DUNGEON_W):
            dungeon[y][x] = 9

def main():
    pygame.init()
    pygame.display.set_caption("미로 생성")
    screen = pygame.display.set_mode((528,432))
    clock = pygame.time.Clock()

    make_maze()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_maze()

        for y in range(MAZE_H):
            for x in range(MAZE_W):
                w = 48
                h = 48
                X = x * w
                Y = y * w
                if maze[y][x] == 0:
                    pygame.draw.rect(screen, CYAN, [X,Y,w,h])
                if maze[y][x] == 1:
                    pygame.draw.rect(screen, GRAY, [X,Y,w,h])

        pygame.display.update()
        clock.tick(2)

if __name__ == '__main__':
    main()
