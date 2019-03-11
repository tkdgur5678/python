import pygame

def main(width,height):
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Colorkey blit")
    
    screen = pygame.display.set_mode((width,height))
    image = pygame.image.load("01_image.png")
    image.set_colorkey((255,0,255))
    bgd_image = pygame.image.load("background.png")
    #screen.fill((255,125,0))
    screen.blit(bgd_image, (0,0))
    screen.blit(image,(50,50))
     
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main(400,300)
    
