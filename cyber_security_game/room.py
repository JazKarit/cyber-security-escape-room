import pygame

from computer import Computer
class Room():
    def __init__(self, settings, screen):
        
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.width, self.height = int(self.screen_rect.right/2), self.screen_rect.bottom
        
        self.image = pygame.image.load('background2.bmp')
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.terminals = []
        
        self.draw()
    
    def draw(self):
        
        self.screen.blit(self.image, self.rect)
    
    def add_terminal(self,x,y,w,h,password,terminal_name,is_locked):
        terminal_rect = pygame.Rect(x, y, w, h)
        terminal = Computer(terminal_rect,password,terminal_name,is_locked)
        self.terminals.append(terminal)

