import pygame
from src.models import obstacles, character_sprite_right, character_sprite_left

character_sprite= None
class Character:
    def __init__(self, x, y):
        # Initialize the character's position and velocity
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        # Set the character's jump properties
        self.can_jump = False
        self.jump_velocity = -10
        self.last_direction = "right"  # Set the default direction to right
        # Create a rectangle representing the character's hitbox
        self.hitbox = pygame.Rect(self.x, self.y, 50, 100)
        # Initialize a list to store the bullets
        self.bullets = []
    def update(self, camera):
        # Update the character's position based on its velocity
        self.x += self.vx
        self.y += self.vy
        self.hitbox.x = self.x
        self.hitbox.y = self.y
        # Apply gravity
        self.vy += 0.5

        # Update the position of the bullets
        for bullet in self.bullets:
            bullet.update(camera, self.bullets)
            
        
       
        # Check if the character is on the ground
        if self.y > 500:  # Adjust this value based on your level design
            self.y = 500
            self.vy = 0
            self.can_jump = True


        # Determine which image to display based on the character's horizontal velocity and last direction
        if self.vx > 0:
            character_sprite = character_sprite_right
            self.last_direction = "right"
        elif self.vx < 0:
            character_sprite = character_sprite_left
            self.last_direction = "left"
        else:
            if self.last_direction == "right":
                character_sprite = character_sprite_right
            elif self.last_direction == "left":
                character_sprite = character_sprite_left
        
        # Check for collisions with the obstacles
        for obstacle in obstacles:
            if self.hitbox.colliderect(obstacle):
                # Reset the character's velocity to 0 to stop it from moving
                self.vx = 0
                self.vy = 0

        
    def jump(self):
        # Make the character jump if it is on the ground
        if self.can_jump:
            self.vy = self.jump_velocity
            self.can_jump = False
            # Start a timer to track how long the W key has been pressed
            self.jump_timer = pygame.time.get_ticks()