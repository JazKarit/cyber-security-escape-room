import pygame
from pygame.sprite import Sprite

class Player(Sprite):
    
    def __init__(self, settings, screen):
        """Initialize the ship and set its strting position."""
        super().__init__()
        self.screen = screen
        
        # Load the ship image and get its starting position
        self.image = pygame.image.load('player.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.settings = settings
        
        # Start at the bottom center of the screen.
        self.rect.centerx = 75
        self.rect.bottom = 639
        
        # Store  a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False
        
    def update(self):
        """Update the ship's position based on the movement flags"""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right/2:
            self.centerx += self.settings.player_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.settings.player_speed
            
        # Update rect object from self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
    
    def center(self):
       """Center player on the screen."""
       self.centerx = self.screen_rect.centerx 
       self.centery = self.screen_rect.centery 