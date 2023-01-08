import pygame


# Load the character sprite
character_sprite_right = pygame.image.load(r"C:\Users\MHD_K\Desktop\Gaming Station\FirstGame\src\designs\Facing_right.png")
# Resize the character sprite
character_sprite_right = pygame.transform.scale(character_sprite_right, (50, 100))  # New size (width, height)

character_sprite_left= pygame.image.load(r"C:\Users\MHD_K\Desktop\Gaming Station\FirstGame\src\designs\Facing_left.png")
# Resize the character sprite
character_sprite_left = pygame.transform.scale(character_sprite_left, (50, 100))  # New size (width, height)

# init state
character_sprite = character_sprite_right
# Define the obstacles as a list of rectangles
obstacles = [pygame.Rect(50, 400, 50, 50), pygame.Rect(200, 200, 75, 75)]