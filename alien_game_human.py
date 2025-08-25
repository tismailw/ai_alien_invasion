import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Manage game assests and behaviors."""
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        
        self.Ship = Ship(self)
        
        
        #background color
        self.bg_color = (230, 230, 230)
        
    def run_game(self):
        """Starts the main loop of the game"""
        while True: 
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.Ship.blitme()
        pygame.display.flip()
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit

    
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()