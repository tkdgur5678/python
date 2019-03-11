import pygame

def main(width,height):
    pygame.init()
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("First blit")
    
    screen = pygame.display.set_mode((width,height))
    image = pygame.image.load("01_image.png")
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
    
