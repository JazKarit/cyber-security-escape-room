import pygame

class Terminal():
    def __init__(self, settings, screen, header):
        """Initialize scorekeepng attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.header = header
        self.left_edge = self.screen_rect.right/2 + 5
        self.width, self.height = self.screen_rect.right/2, self.screen_rect.bottom
        
        # Font settings for scoring information.
        self.header_color = (111, 206, 55)
        self.text_color = (255, 255, 255)
        self.text_color2 = (244, 191, 66)
        self.bg_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 30)
        self.line_height = 25
        self.rect = pygame.Rect(self.left_edge, 0, self.width, self.height)
        self.last_shown = 0
        
        self.text = ''
        
        txt_surface = self.font.render('You are a hacker who tried to hack into a government building.', True, self.text_color2)
        self.lines = [txt_surface]
        txt_surface = self.font.render('In the process you got locked inside the building. The objective', True, self.text_color2)
        self.lines.append(txt_surface)
        txt_surface = self.font.render('is to escape and get information. Start at the computer and type help.', True, self.text_color2)
        self.lines.append(txt_surface)
        txt_surface = self.font.render('>> ', True, self.text_color)
        self.lines.append(txt_surface)
        # Prepare the initial score images.
        self.header_image = self.font.render(self.header, True, self.text_color, 
                                                        self.bg_color)
        self.header_image_rect = pygame.Rect(self.left_edge, 10, self.width, 10)
        self.header_image_rect.left = self.left_edge
        
        self.draw()
    
    
    def get_input(self):
        return self.text
        
    def next_line(self,output):
        self.text = output
        output_height_mult = 0
        for line in output:
            output_height_mult = output_height_mult + 1
            txt_surface = self.font.render(line, True, self.text_color2)
            self.lines.append(txt_surface)
            self.check_at_end()
            self.text = ''
        txt_surface = self.font.render('>> ', True, self.text_color)
        self.lines.append(txt_surface)
        self.check_at_end()
        
    def check_at_end(self):
        if (len(self.lines)-self.last_shown)* self.line_height + 50 > self.height:
            self.last_shown = self.last_shown + 15
                
                
    def delete(self):
        self.text = self.text[:-1]
        self.lines[len(self.lines)-1] = self.font.render('>> ' + self.text, True, self.text_color)
        self.draw()
        
    def add_char(self,char):
        self.text += char
        self.lines[len(self.lines)-1] = self.font.render('>> ' + self.text, True, self.text_color)
        self.draw()
        
    
    def draw(self):
        self.header_image = self.font.render(self.header, True, self.header_color, 
                                                        self.bg_color)
        self.header_image_rect = pygame.Rect(self.left_edge, 0, self.width, 10)
        self.header_image_rect.left = self.left_edge
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.header_image, self.header_image_rect)
        i = 1
        height = 5 + self.line_height
        for j in range(self.last_shown,len(self.lines)):
            rect = (self.left_edge,i*self.line_height,10,10)
            self.screen.blit(self.lines[j], rect)
            i = i + 1
    
    def update_header(self,header):
        self.header = header
        
        
    
