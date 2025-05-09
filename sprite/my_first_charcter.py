import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))  # Create a 50x50 square
        self.image.fill((0, 0, 255))  # Fill it with blue color
        self.rect = self.image.get_rect()  # Get the rectangle for positioning
        self.rect.center = (100, 100)  # Set initial position

    def update(self):
        self.rect.x += 5  # Move the sprite 5 pixels to the right
player1 = Player()
print("player position:", player1.rect.center)
print("Player rectangle:", player1.rect)       # Prints the rect object
print("Player image size:", player1.image.get_size())  # Prints the size of the image 

"""
    output: 
    pygame 2.6.1 (SDL 2.28.4, Python 3.12.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
player position: (100, 100)
Player rectangle: <rect(75, 75, 50, 50)>
Player image size: (50, 50)
    """
