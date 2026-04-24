import pygame
import sys
from ball import Ball

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Moving Ball Game")
    
    # Use pygame.time.Clock() for smooth loop
    clock = pygame.time.Clock()
    
    # Start near the center, radius 25 (diameter 50)
    ball = Ball(width // 2, height // 2, 25)
    
    # Each key press moves the ball exactly 20 pixels
    move_distance = 20
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Handle keys correctly for all 4 arrows
                if event.key == pygame.K_UP:
                    ball.move(0, -move_distance, width, height)
                elif event.key == pygame.K_DOWN:
                    ball.move(0, move_distance, width, height)
                elif event.key == pygame.K_LEFT:
                    ball.move(-move_distance, 0, width, height)
                elif event.key == pygame.K_RIGHT:
                    ball.move(move_distance, 0, width, height)
                    
        # White background
        screen.fill((255, 255, 255))
        
        # Keep code split; drawing logic located in ball.py
        ball.draw(screen)
        
        pygame.display.flip()
        
        # Cap FPS smoothly
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
