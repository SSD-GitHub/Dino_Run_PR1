#install 'python -m pip install -U pygame --user' before attempting to run this game.

#importing the pygame library and initialising it.
import pygame
pygame.init()

#Creating the player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, image_path):
        super().__init__()
        self.x = x
        self.y = y
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        self.image = pygame.image.load(image_path)
    
    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
    
    def draw(self, surface):
        surface.blit(self.image, self.position)
    
    def move_right(self):
        self.velocity = (1, self.velocity[1])
    
    def jump(self):
        self.position = (self.x+100, self.y-250) #jumps up in the air by a significant amount (anything under 100 is barely noticeable).
        self.image = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Documentation\\Dead Dinosaur.png")
    
    def crouch(self):
        self.position = (self.x+100, self.y+160)
        self.image = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Documentation\\dead dinosaur mini.png")

# Set the window size
window_size = (1920, 750)

# Create a window
window = pygame.display.set_mode(window_size)

# Create a player sprite
player = Player(320, 250, 0, 0, "C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Documentation\\Dead Dinosaur.png")

# Main game loop
while True:
    #Input handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #When close button pressed, close the program.
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: #when right arrow key pressed, move forward.
                player.move_right()
            elif event.key == pygame.K_UP or event.key == pygame.K_SPACE: #space and upper arrow key to jump
                player.jump()
            elif event.key == pygame.K_DOWN: #down arrow key to crouch
                player.crouch()
            elif event.key == pygame.K_ESCAPE: #When escape key pressed, quit the program.
                pygame.quit()
    
    # Update the player sprite
    player.update()
    
    # Clear the window
    window.fill((255, 255, 255))
    
    # Draw the player sprite
    player.draw(window)
    
    # Update the display
    pygame.display.update()