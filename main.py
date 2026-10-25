import pygame
import random
from points import Point

class Main:

    RGB_FARBEN = [
    (173, 255, 47),    # Razer-Grün
    (224, 0, 0),      # ROG-Rot
    (0, 112, 243),    # PlayStation-Blau
    (249, 158, 26),   # Overwatch-Orange
    (0, 186, 255),    # Portal-Blau
    (145, 71, 255),   # Twitch-Lila
    (88, 101, 242),   # Discord-Blurple
    (0, 255, 242),    # Plasma-Cyan
    (186, 0, 255),    # Energie-Violett
    (214, 255, 0)     # Toxisches Gelb
]

    def __init__(self):
        pygame.init()
        self.HEIGHT = 600
        self.WIDTH = 800
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Particle Simulator")
        self.clock = pygame.time.Clock()
        self.delta_time = 0
        self.points = []
        self.run()

    def run(self) -> None: 
        self.create_points()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60) / 1000
            self.window.fill((10, 10, 10))
            for point in self.points:
                point.update()
            pygame.display.update()

        pygame.quit()

    def create_points(self):
        for i in range(2000):
            point = Point(game=self, 
                color=random.choice(self.RGB_FARBEN), 
                position=(random.uniform(0, 800), (random.uniform(0, 600))),
                speed=(random.uniform(-2, 2), random.uniform(-2, 2)))

            self.points.append(point)
            
Game = Main()