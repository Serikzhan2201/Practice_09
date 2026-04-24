import pygame
import math
import datetime
import os

class Clock:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center = (width // 2, height // 2)
        self.radius = min(width, height) // 2 - 20
        
        # Look for mickey_hand.png
        self.image_path = os.path.join(os.path.dirname(__file__), "images", "mickey_hand.png")
        if os.path.exists(self.image_path):
            try:
                original_image = pygame.image.load(self.image_path).convert_alpha()
                self.has_image = True
                # Scale for Right Hand = minutes, Left Hand = seconds
                self.min_hand_image = pygame.transform.scale(original_image, (40, self.radius - 20))
                self.sec_hand_image = pygame.transform.scale(original_image, (20, self.radius + 10))
            except pygame.error:
                self.has_image = False
        else:
            self.has_image = False

    def get_angles(self):
        # Fetch current time
        now = datetime.datetime.now()
        minute = now.minute
        second = now.second
        
        # 60 seconds -> 360 degrees (6 degrees per second)
        sec_angle = second * 6
        # 60 minutes -> 360 degrees, adding gradual movement based on seconds
        min_angle = minute * 6 + (second * 0.1)

        return min_angle, sec_angle
        
    def draw(self, surface):
        # Fill background white
        surface.fill((255, 255, 255))
        
        # Draw the clock face
        pygame.draw.circle(surface, (0, 0, 0), self.center, self.radius, 5)
        for i in range(12):
            angle = math.radians(i * 30 - 90)
            x_start = self.center[0] + (self.radius - 15) * math.cos(angle)
            y_start = self.center[1] + (self.radius - 15) * math.sin(angle)
            x_end = self.center[0] + self.radius * math.cos(angle)
            y_end = self.center[1] + self.radius * math.sin(angle)
            pygame.draw.line(surface, (0, 0, 0), (x_start, y_start), (x_end, y_end), 3)

        min_angle, sec_angle = self.get_angles()
        
        if self.has_image:
            # Rotate hand images
            min_rotated = pygame.transform.rotate(self.min_hand_image, -min_angle)
            min_rect = min_rotated.get_rect(center=self.center)
            surface.blit(min_rotated, min_rect)

            sec_rotated = pygame.transform.rotate(self.sec_hand_image, -sec_angle)
            sec_rect = sec_rotated.get_rect(center=self.center)
            surface.blit(sec_rotated, sec_rect)
        else:
            # Fallback to simple lines if image is missing
            m_angle_rad = math.radians(min_angle - 90)
            min_x = self.center[0] + (self.radius - 40) * math.cos(m_angle_rad)
            min_y = self.center[1] + (self.radius - 40) * math.sin(m_angle_rad)
            pygame.draw.line(surface, (0, 0, 255), self.center, (min_x, min_y), 8)
            
            s_angle_rad = math.radians(sec_angle - 90)
            sec_x = self.center[0] + (self.radius - 20) * math.cos(s_angle_rad)
            sec_y = self.center[1] + (self.radius - 20) * math.sin(s_angle_rad)
            pygame.draw.line(surface, (255, 0, 0), self.center, (sec_x, sec_y), 4)

# Requirement check:
# - Displays minutes and seconds.
# - Can use image hands (right=min, left=sec).
# - Synchronized with system clock.
# - Fallbacks gracefully when missing image.
