import pygame
from src.models import character_sprite_left, character_sprite_right, character_sprite, obstacles
from src.models.character import Character
from src.models.camera import Camera
from src.models.bullet import Bullet
pygame.init()
# Create a clock object to control the frame rate
clock = pygame.time.Clock()
# Set the window size
window_size = (800, 600)
# Create a camera object
camera = Camera(0, 0)
# Create the window
screen = pygame.display.set_mode(window_size)
# Load the map image
map_image = pygame.image.load("./src/designs/example.png")
# Set the window title
pygame.display.set_caption("Super Mario Bros. Style Game")
# Create an instance of the Character class
character = Character(100, 500)  # Initial position (x, y)

# Define the font and text color
font = pygame.font.Font(None, 36)  # Use the default font with a size of 36
color = (255, 255, 255)  # Use white as the text color


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
    if keys[pygame.K_d]:
        character.vx = 5  # Set the horizontal velocity to a positive value to move the character right
    if keys[pygame.K_a]:
        character.vx = -5
    if not keys[pygame.K_d] and not keys[pygame.K_a]:
        character.vx = 0  # Reset the horizontal velocity to 0 when the D key is not pressed     
    if keys[pygame.K_SPACE]:
        if len(character.bullets) <= 10:
            # Create a new bullet and add it to the character's bullets list
            bullet = Bullet(character.x, character.y)
            character.bullets.append(bullet)
    # Render graphics to the screen
    screen.fill((0, 0, 0))  # Clear the screen
    # Draw the character to the screen, offset by the camera position
    if character.last_direction == "right":
        character_sprite = character_sprite_right
    elif character.last_direction == "left":
        character_sprite = character_sprite_left
    
    screen.blit(map_image, (0, 0))  # Draw the map image to the screen
    screen.blit(character_sprite, (character.x - camera.x, character.y - camera.y))  # Draw the character sprite
    # Draw the obstacles to the screen
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)  # Fill the rectangle with red

    # Render the text as a surface
    text_surface = font.render(f"Bullets: {10 - len(character.bullets)}", True, color)
    screen.blit(text_surface, (10, 10)) # Draw the text at the (10, 10) position

    # Draw the bullets to the screen
    for bullet in character.bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet.hitbox)  # Fill the rectangle with white
    pygame.display.flip()  # Update the window
    # Limit the frame rate to 30 FPS
    clock.tick(60)
