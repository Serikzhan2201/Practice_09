import pygame
import sys
from clock import Clock

def main():
    # Initialize pygame
    pygame.init()
    width, height = 600, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Mickey's Clock Application")
    
    # Setup Clock object and frame rate
    game_clock = pygame.time.Clock()
    mickey_clock = Clock(width, height)
    
    running = True
    while running:
        # Event loop to handle quits or exits gracefully
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Draw clock each frame
        mickey_clock.draw(screen)
        pygame.display.flip()
        
        # Real-time synchronization at 60 FPS
        game_clock.tick(60)

    # Clean exit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
