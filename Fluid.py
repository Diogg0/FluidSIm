import pygame
import math

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

height, width = 500, 500

window = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()

def SmoothingKernel(radius, dst):
    value = max(0, radius*radius - dst * dst)
    return value * value * value

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speedX = 0
        self.speedY = 1
        self.bounce = 0


balls = []


def create():
    j = 0
    k = 0
    for i in range(1,11):
        balls.append(Ball(180+j, 250+k))
        j += 40
        if i % 5 == 0 and i != 0:
            k += 40
            j = 0


def collisions(i):
    ball_radius = 20
    gravity = 0.5
    ball = balls[i]
    dampingFactor = 1

    ball.x += math.floor(ball.speedX)

    if ball.bounce < 5:
        ball.speedY += gravity
        ball.y += math.floor(ball.speedY)

    if ball.x - ball_radius < 0 or ball.x + ball_radius > width:
        ball.speedX *= -1 * dampingFactor

    if ball.y + ball_radius+1 > height or ball.y + ball_radius > width:
        ball.speedY *= -1 * dampingFactor
        


def main():
    running = True
    pygame.init()

    create()

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill((0, 0, 0))
        for i in range(10):
            ball = balls[i]
            pygame.draw.circle(window, RED, (ball.x, ball.y), 20)
            collisions(i)

        clock.tick(60)
        pygame.display.flip()


main()