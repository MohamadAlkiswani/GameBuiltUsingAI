import pygame

class Bullet:
    def __init__(self, x, y):
        # Initialize the bullet's position and velocity
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = -10  # Set the vertical velocity to -10 to move upwards

        # Create a rectangle representing the bullet's hitbox
        self.hitbox = pygame.Rect(self.x, self.y, 8, 8)

    def update(self, camera, bullets):
        # Update the bullet's position based on its velocity
        self.x += self.vx
        self.y += self.vy
        self.hitbox.x = self.x
        self.hitbox.y = self.y  

        # Check if the bullet's y position is greater than the limit
        if self.y < 100:
            # Remove the bullet from the bullets list
            bullets.remove(self)