import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class that fires bullets"""
    def __init__(self, ai_game):
        super().__init__()
        
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #create a bullet at rect at 0,0 and set the position correctly
        self.rect = pygame.Rect(
            0,
            0,
            self.settings.bullet_width,
            self.settings.bullet_height,
        )
        self.rect.midtop = ai_game.ship.rect.midtop
        
        self.y = float(self.rect.y)
    
    def update(self):
        """move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = int(self.y)
        
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        