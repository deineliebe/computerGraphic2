import pygame
import numpy as np
import sys

# Colors' initialization
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREY = (230, 231, 232)

# There are parameters of our window (initialization)
WIDTH = 600
HEIGHT = 600
# Set title
pygame.display.set_caption("Second lab (group: 0323, team: 4)")
# Set window's parameters
window = pygame.display.set_mode((WIDTH, HEIGHT))

points = []

def connectPoints(points, color):
    for i in range(0, len(points) - 1):
        pygame.draw.line(window, color, (points[i][0][0], points[i][1][0]), (points[i + 1][0][0], points[i + 1][1][0]))

def displayPoints():
    for point in points:
        x = int(point[0][0])
        y = int(point[1][0])
        pygame.draw.circle(window, BLACK, (x, y), 2)

def bezier():
    if (len(points) > 3):
        beziePoints = []
        newPoints = []
        for i in range(len(points)):
            newPoints.append(points[i])
            if (((len(newPoints) - 1) % 3 == 2) & (len(points) > i + 2)):
                newPoints.append([[(np.float32(points[i][0][0]) + points[i + 1][0][0]) / 2], [(np.float32(points[i][1][0]) + points[i + 1][1][0]) / 2]])
        if (len(newPoints) % 3 == 0):
            newPoints.append(points[-1])
        for i in range(0, len(newPoints) - 3, 3):
            for j in range(101):
                    t = j / 100.
                    temp = np.float32(newPoints[i]) * (1 - t) * (1 - t) * (1 - t)
                    temp += np.float32(newPoints[i + 1]) * (1 - t) * (1 - t) * t * 3
                    temp += np.float32(newPoints[i + 2]) * (1 - t) * t * t * 3
                    temp += np.float32(newPoints[i + 3]) * t * t * t
                    beziePoints.append(temp)
        connectPoints(beziePoints, BLUE)

clock = pygame.time.Clock()
while True:
    window.fill(WHITE)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                points.append([[i.pos[0]], [i.pos[1]]])
                print(points)
            elif i.button == 3:
                if (points):
                    points.pop()
                print(points)
    displayPoints()
    connectPoints(points, GREY)
    bezier()
    pygame.display.update()