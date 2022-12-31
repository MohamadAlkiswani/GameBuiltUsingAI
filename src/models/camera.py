class Camera:
    def __init__(self, x, y):
        # Initialize the camera position
        self.x = x
        self.y = y

    def update(self, character):
        # Update the camera position based on the character's position
        self.x = character.x - 250  # Adjust this value to control the camera's horizontal offset
        self.y = character.y - 250  # Adjust this value to control the camera's vertical offset

        # Limit the camera's movement to the boundaries of the map
        self.x = max(0, min(self.x, 1000 - 500))  # Adjust these values based on the size of your map
        self.y = max(0, min(self.y, 1000 - 500))
