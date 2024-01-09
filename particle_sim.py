import pygame
import math
import random



# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

height, width = 1540, 800


window = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()

# Custom event to create a new particle
CREATE_PARTICLE_EVENT = pygame.USEREVENT + 1

# Set the timer for the custom event to trigger every 20 seconds (20000 milliseconds)
pygame.time.set_timer(CREATE_PARTICLE_EVENT, 2000)


'''Particle class
        Attributes:
            position: x and y coordinates of the particle
            velocity: x and y velocity of the particle
            radius: radius of the particle
'''
class Particle:
    def __init__(self, x, y, radius):
        self.position =[x, y]
        self.velocity = [0, 5]
        self.radius = radius
        
        
# List of particles        
particles = []


# Creates a new particle
def create():
    particles.append(Particle(random.randint(430,1000), random.randint(60,600), random.randint(10,30)))


# Updates the position of the particle
def update(particle):
    dt = clock.tick(120) / 1000
    gravity = 10
    dampingFactor = 0.8

    particle.velocity[1] += gravity * dt
    particle.position[0] += particle.velocity[0]
    particle.position[1] += particle.velocity[1] 

    if particle.position[0] - particle.radius < 411:
        particle.velocity[0] *= -1 * dampingFactor
        particle.position[0] = 411 + particle.radius  # Adjust position back to border
    elif particle.position[0] + particle.radius > 1108:
        particle.velocity[0] *= -1 * dampingFactor
        particle.position[0] = 1108 - particle.radius  # Adjust position back to border

    if particle.position[1] - particle.radius < 52:
        particle.velocity[1] *= -1 * dampingFactor
        particle.position[1] = 52 + particle.radius  # Adjust position back to border
    elif particle.position[1] + particle.radius > 750:
        particle.velocity[1] *= -1 * dampingFactor
        particle.position[1] = 750 - particle.radius  # Adjust position back to border

def main():
    running = True
    pygame.init()


    create()
    while running:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                '''
            particle_count = len(particles)

            if particle_count < 20 and event.type == CREATE_PARTICLE_EVENT:
                create()

            if particle_count >= 20 and event.type == CREATE_PARTICLE_EVENT:
                del particles[0]
                create()'''

        window.fill((0, 0, 0))

        # Draw the collision borders
        pygame.draw.rect(window, BLUE, pygame.Rect(410,50, 700, 700),2) # Collision borders = (top: 52, bottom:750, left: 411, right: 1108)

        # Draw the particles by iterating through the particles list
        for particle in particles:
            update(particle)
            pygame.draw.circle(window, RED, (particle.position[0], particle.position[1]), particle.radius)



        clock.tick(120)
        pygame.display.flip()


main()
