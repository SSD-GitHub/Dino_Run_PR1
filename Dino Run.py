#install 'python -m pip install -U pygame --user' before attempting to run this game.


#importing the pygame library and initialising it.
import pygame
pygame.init()

#Establishing global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Character Sprite State Constants
RUNNING = [pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoRun1.png"), 
           ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoRun2.png")]

JUMPING = pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoJump.png")

DUCKING = [pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoDuck1.png"), 
           ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoDuck2.png")]

SMALL_CACTUS = [pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus1.png"), 
                ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus2.png"), 
                ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus3.png")]

LARGE_CACTUS = [pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus1.png"), 
                ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus2.png"), 
                ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus3.png")]

TERADACTYL = [pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Teradactyl\\1.png"), 
              ("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Teradactyl\\2.png")]

CLOUD = pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Other\\Cloud.png")

BACKGROUND = pygame.image.load("C:\\Users\\shawn\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Other\\Track.png")

#Creating classes
class Dinosaur:
    x = 80
    y = 310

    def __init__(self):
        #Linking the sprite states to variables for easy referencing later on.
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        #gives the dinosaur different states and establishes its default state.
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0 #to help animate the dinosaur
        self.image = self.run_img[0] #to set the dinosaur's inital sprite state.
        self.dino_rect = self.image.get_rect() #establishes the player's hitbox to allow for the implementation of object collision detection and handling.
        self.dino_rect.x = self.x #aligns the hitbox with the dinosaur's x coordinate.
        self.dino_rect.y = self.y #aligns the hitbox with the dinosaur's y coordinate.

    def update(self, userInput):
        if self.dino_duck: #ensures that the Dinosaur ducks when it is supposed to.
            self.duck()
        if self.dino_run: #ensures that the Dinosaur runs when it is supposed to.
            self.run()
        if self.dino_jump: #ensures that the Dinosaur jumps when it is supposed to.
            self.jump()
        
        if self.step_index >= 10: #to help animate the dinosaur.
            self.step_index = 0
        
        #Player Controls Definition
        if userInput[pygame.K_UP or pygame.K_SPACE] and not self.dino_jump: #if the up arrow or space bar is pressed and the dinosaur is not jumping, the dinosaur will jump.
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump: #if the down arrow is pressed and the dinosaur is not jumping, then the dinosaur will duck.
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]): #if the dinosaur is not jumping and the down arrow is not pressed, then the dinosaur will simply run.
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False

        
#Creating Game Loop
def main():
    run = True
    clock = pygame.time.Clock() #to maintain the pace of the game.
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #When close button pressed, close the program.
                pygame.quit()
                run = False

        SCREEN.fill((255, 255, 255)) #You have to pass in a tuple to represent RGB values in pygame.
        userInput = pygame.key.get_pressed() #stores the user input.

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(30)
        pygame.display.update()

main()