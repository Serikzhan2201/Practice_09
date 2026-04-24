import pygame
import sys
from player import MusicPlayer

def main():
    # Handle pygame init, mixer init before Player context natively
    pygame.init()
    pygame.mixer.init()
    
    width, height = 800, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Music Player")
    
    player = MusicPlayer()
    
    # Use pygame.font for UI appropriately
    font = pygame.font.SysFont(None, 36)
    small_font = pygame.font.SysFont(None, 28)
    
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Mapped strictly to criteria
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.previous_track()
                elif event.key == pygame.K_q:
                    running = False

        screen.fill((30, 30, 50))
        
        instructions = [
            "Keyboard Controls:",
            "P = Play",
            "S = Stop",
            "N = Next track",
            "B = Previous track",
            "Q = Quit"
        ]
        
        # Draw instructions natively mapping explicit controls
        y_offset = 30
        for line in instructions:
            text_surface = small_font.render(line, True, (255, 255, 255))
            screen.blit(text_surface, (30, y_offset))
            y_offset += 40
            
        # Draw dynamic track metadata and playback parameters
        info_text = player.get_info_text()
        info_surface = font.render(info_text, True, (100, 255, 100))
        info_rect = info_surface.get_rect(center=(width // 2, height - 80))
        screen.blit(info_surface, info_rect)

        pygame.display.flip()
        clock.tick(30)

    # Perform tear down
    pygame.mixer.quit()
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
