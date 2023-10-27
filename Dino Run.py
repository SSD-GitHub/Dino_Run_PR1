#install 'python -m pip install -U pygame --user' before attempting to run this game.

#importing the necessary libraries and initialising them.
import pygame
pygame.init()
import random

#Establishing global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Character Sprite State Constants
RUNNING = [pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoRun1.png"), 
           ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoRun2.png")]

JUMPING = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoJump.png")

DUCKING = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Dino\\DinoDuck1.png")

SMALL_CACTUS = [pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus1.png"), 
                ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus2.png"), 
                ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\SmallCactus3.png")]

LARGE_CACTUS = [pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus1.png"), 
                ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus2.png"), 
                ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Cactus\\LargeCactus3.png")]

TERADACTYL = [pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Teradactyl\\1.png"), 
              ("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Teradactyl\\2.png")]

CLOUD = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Other\\Cloud.png")

BACKGROUND = pygame.image.load("C:\\Users\\22308693\\OneDrive - Buckinghamshire New University\\Cyber Security BSc Course Folder\\Programming Concepts\\PR1 Project Resources\\Assets\\Other\\Track.png")

#Creating classes
class Dinosaur:
    x = 80
    y = 310
    y_duck = 340
    JUMP_VEL = 8.5

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
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0] #to set the dinosaur's inital sprite state.
        self.dino_rect = self.image.get_rect() #establishes the player's hitbox to allow for the implementation of object collision detection and handling.
        self.dino_rect.x = self.x #aligns the hitbox with the dinosaur's x coordinate.
        self.dino_rect.y = self.y #aligns the hitbox with the dinosaur's y coordinate.
        #self.duck_image = self.duck_img[self.step_index // 5]
        #self.runner_image = self.run_img[self.step_index // 5]

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
    def duck(self):
        #self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.duck_img.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y_duck
        self.step_index += 1

    def run(self):
        #self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.runner_image.get_rect()
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(50, 100)
        self.image = CLOUD
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEEN):
        SCREEN.blit(self.image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
         self.image = image
         self.type = type
         self.rect = self.image[self.type].get_rect()
         self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x <-self.rect.width:
             obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class smallcactus(Obstacle):
     def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325


class Largecactus(Obstacle):
     def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300


class Bird(Obstacle):
     def __init__(self, image):
        self.type = 0
        super().__init__(image,self.type)
        self.rect.y = 250
        self.index = 0

     def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1

#Creating Game Loop
def main():
    global game_speed, x_bg, y_bg, points, obstacles
    run = True
    clock = pygame.time.Clock() #to maintain the pace of the game.
    player = Dinosaur() #Created player object from class Dinosaur
    cloud = Cloud() #Created an object of the cloud class
    game_speed = 14
    x_bg = 0
    y_bg = 380
    points = 0 
    font= pygame.font.Font('freesansbold.ttf',20)
    obstacles = [] #establishes an array for all of the obstacles

    def score():
        global points, game_speed
        points += 1 
        if points % 100 == 0: 
            game_speed += 1
            text = font. render ("points: "+ str(points), True, (0, 0 ,0))
            textRect = text.get_rect ()
            textRect.center = (1000, 40)
            SCREEN.blit(text,textRect)                      
                   
    def background():
        global x_bg, y_bg 
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_bg, y_bg))
        SCREEN.blit(BG, (image_width + x_bg, y_bg)), 
        if x_bg <= -image_width:
            SCREEN.blit(BG, (image_width + x_bg, y_bg))
            x_bg = 0
            x_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #When close button pressed, close the program.
                pygame.quit()
                run = False

        SCREEN.fill((255, 255, 255)) #You have to pass in a tuple to represent RGB values in pygame.
        userInput = pygame.key.get_pressed() #stores the user input.

        player.draw(SCREEN)
        player.update(userInput)

        if len(obstacles) == 0:
           if random.randint(0,2) == 0:
            obstacles.append(smallcactus(SMALL_CACTUS))
           elif random.randint(0,2) == 1:
               obstacles.append(Largecactus(LARGE_CACTUS))
           elif random.randint(0,2) == 2:
               obstacles.append(Bird(TERADACTYL))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.draw.rect(SCREEN, (255, 0, 0), player.dino_rect,2)

        cloud.draw(SCREEN)
        cloud.update()

        clock.tick(30)
        pygame.display.update()

main()