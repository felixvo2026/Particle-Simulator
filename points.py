import pygame

class Point:
    def __init__(self, game, color, speed : tuple, position : tuple):
        self.position = pygame.Vector2(position)
        self.game = game
        self.surface = game.window
        self.color = pygame.Color(color)
        self.speed = pygame.Vector2(speed)

    def update(self):
        self.move(self.speed)
        self.draw()

    def move(self, speed):
        # 1. Position wie gewohnt aktualisieren
        self.position += speed 

        # 2. Fenstergröße dynamisch vom Game-Objekt holen
        # (Angenommen, dein Fenster wurde mit pygame.display.set_mode((width, height)) erstellt)
        screen_width = self.game.window.get_width()
        screen_height = self.game.window.get_height()
        
        radius = 5  # Der Radius deines Kreises

        # 3. Kollision mit dem linken oder rechten Rand
        if self.position.x - radius <= 0:
            self.position.x = radius  # Verhindert, dass der Punkt im Rand stecken bleibt
            self.speed.x *= -1        # Richtung umkehren
        elif self.position.x + radius >= screen_width:
            self.position.x = screen_width - radius
            self.speed.x *= -1

        # 4. Kollision mit dem oberen oder unteren Rand
        if self.position.y - radius <= 0:
            self.position.y = radius
            self.speed.y *= -1
        elif self.position.y + radius >= screen_height:
            self.position.y = screen_height - radius
            self.speed.y *= -1

    def draw(self):
        pygame.draw.circle(self.surface, self.color, (int(self.position.x), int(self.position.y)), 5)