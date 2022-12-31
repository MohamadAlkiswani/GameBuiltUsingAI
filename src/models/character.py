import pygame
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
    def update(self, camera):
        # Update the character's position based on its velocity
        self.x += self.vx
        self.y += self.vy

        # Apply gravity
        self.vy += 0.5

        

        # Check if the character is on the ground
        if self.y > 500:  # Adjust this value based on your level design
            self.y = 500
            self.vy = 0
            self.can_jump = True


        
        
    def jump(self):
        # Make the character jump if it is on the ground
        if self.can_jump:
            self.vy = self.jump_velocity
            self.can_jump = False
            # Start a timer to track how long the W key has been pressed
            self.jump_timer = pygame.time.get_ticks()