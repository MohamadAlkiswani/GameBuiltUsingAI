import pygame
from src.models import Character, Camera
pygame.init()
# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Set the window size
window_size = (800, 600)
# Create a camera object
camera = Camera(0, 0)
# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Super Mario Bros. Style Game")
# Create an instance of the Character class
character = Character(100, 500)  # Initial position (x, y)
# Load the character sprite
character_sprite_right = pygame.image.load("./src/designs/Facing_right.png")
# Resize the character sprite
character_sprite_right = pygame.transform.scale(character_sprite_right, (50, 100))  # New size (width, height)

character_sprite_left= pygame.image.load("./src/designs/Facing_left.png")
# Resize the character sprite
character_sprite_left = pygame.transform.scale(character_sprite_left, (50, 100))  # New size (width, height)
# Main game loop
while True:
    # Handle input
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if keys[pygame.K_w]:
        character.jump()
    # Update the game state
    character.update(camera)
    #camera.update(character) # TODO
    # Check if the W key is still being pressed
    if keys[pygame.K_w]:
        # Calculate the elapsed time since the jump started
        elapsed_time = pygame.time.get_ticks() - character.jump_timer
        # Adjust the character's upward velocity based on the elapsed time
        if elapsed_time < 100:  # Adjust this value to control the maximum jump height
            character.vy -= 1  # Apply an upward force to extend the jump
        # Slow down the character's upward velocity as it approaches the peak of the jump
        if character.vy < 0 and elapsed_time > 250:  # Adjust this value to control the delay
            character.vy *= 1
        print(elapsed_time)
    if keys[pygame.K_d]:
        character.vx = 5  # Set the horizontal velocity to a positive value to move the character right
        print(character.vx)

    if keys[pygame.K_a]:
        character.vx = -5
        print(character.vx)
    if not keys[pygame.K_d] and not keys[pygame.K_a]:
        character.vx = 0  # Reset the horizontal velocity to 0 when the D key is not pressed     
    
    # Render graphics to the screen
    screen.fill((0, 0, 0))  # Clear the screen
    # Draw the character to the screen, offset by the camera position
    # Determine which image to display based on the character's horizontal velocity and last direction
    if character.vx > 0:
        character_sprite = character_sprite_right
        character.last_direction = "right"
    elif character.vx < 0:
        character_sprite = character_sprite_left
        character.last_direction = "left"
    else:
        if character.last_direction == "right":
            character_sprite = character_sprite_right
        elif character.last_direction == "left":
            character_sprite = character_sprite_left
    screen.blit(character_sprite, (character.x - camera.x, character.y - camera.y))  # Draw the character sprite
    pygame.display.flip()  # Update the window
    # Limit the frame rate to 30 FPS
    clock.tick(60)
