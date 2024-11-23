import pygame

class PhyisicalDrawer:
    
    def __init__(self):
        pygame.init()
        white = (255, 255, 255)
        black = (0, 0, 0)
        
        
        self.screen = pygame.display.set_mode((1000, 1000))
        pygame.display.set_caption("Graph Drawer")
        
        self.font = pygame.font.Font(None, 36)
        
        self.screen.fill(white)
        pygame.display.update()     
    
    def get_size(self, value):
        black = (0, 0, 0)    
        font = pygame.font.Font(None, 36)        
        text_surface = font.render(str(value), True, black)
        
        
        return text_surface.get_size() #w,h
    
    def draw_text(self,value,x,y):
        
        text_surface = self.font.render(str(value), True, (0, 0, 0))   
     
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
         
        self.screen.blit(text_surface, text_rect)

        pygame.display.update()    
        
    def draw_line(self, x1,y1,x2,y2):
        pygame.draw.line(self.screen, (0, 0, 0), (x1, y1), (x2, y2), 2)  
        pygame.display.update()    

    def draw_circle(self, x, y, radius=30, color=(0, 0, 0)):  
            pygame.draw.circle(self.screen, (255,255,255), (x, y), radius) 
            pygame.draw.circle(self.screen, color, (x, y), radius, 2)  
            pygame.display.update()

