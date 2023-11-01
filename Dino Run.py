#install 'python -m pip install -U pygame --user' before attempting to run this game on new computers.

#Game Initialisation
#importing the necessary libraries.
import pygame
import random
pygame.init() #initialising the pygame library.

#Establishing global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creates screen surface to allow the game to be displayed.
pygame.display.set_caption('Dino Run') #Sets window name to Dino Run

#Character Sprite State Constants
RUNNING = [pygame.image.load("Assets\\Dino\\DinoRun1.png"), 
           pygame.image.load("Assets\\Dino\\DinoRun2.png")]

JUMPING = pygame.image.load("Assets\\Dino\\DinoJump.png")

DUCKING = pygame.image.load("Assets\\Dino\\DinoDuck1.png")

SMALL_CACTUS = [pygame.image.load("Assets\\Cactus\\SmallCactus1.png"), 
                pygame.image.load("Assets\\Cactus\\SmallCactus2.png"), 
                pygame.image.load("Assets\\Cactus\\SmallCactus3.png")]

LARGE_CACTUS = [pygame.image.load("Assets\\Cactus\\LargeCactus1.png"), 
                pygame.image.load("Assets\\Cactus\\LargeCactus2.png"), 
                pygame.image.load("Assets\\Cactus\\LargeCactus3.png")]

TERADACTYL = [pygame.image.load("Assets\\Teradactyl\\Bird1.png"), 
              pygame.image.load("Assets\\Teradactyl\\Bird2.png")]

CLOUD = pygame.image.load("Assets\\Other\\Cloud.png")

BACKGROUND = pygame.image.load("Assets\\Other\\Track.png")

#Creating the Dinosaur class
class Dinosaur:
    x = 80
    y = 310
    y_duck = 340
    JUMP_VEL = 8.5

    def __init__(self):
        #Linking the sprite states to variables for easy referencing later on.
        self.duck_img = [DUCKING]
        self.run_img = RUNNING
        self.jump_img = JUMPING
        #gives the dinosaur different states and establishes its default state.
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0 #to help animate the dinosaur
        self.jump_vel = self.JUMP_VEL #to ensure that the dinosaur jumps properly.
        self.image = self.run_img[0] #to set the dinosaur's inital sprite state.
        self.dino_rect = self.image.get_rect() #establishes the player's hitbox to allow for the implementation of object collision detection and handling.
        self.dino_rect.x = self.x #aligns the hitbox with the dinosaur's x coordinate.
        self.dino_rect.y = self.y #aligns the hitbox with the dinosaur's y coordinate.

    #ensures the Dinosaur remains up to date with the player inputs.
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

    #Makes the dinosaur duck
    def duck(self):
        if self.step_index // 5 < len(self.duck_img):
            self.image = self.duck_img[self.step_index // 5]
        self.step_index += 1
        if self.step_index >= len(self.duck_img) * 5:
            self.step_index = 0
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y_duck
        
    #makes the Dinosaur run
    def run(self):
        if self.step_index // 5 < len(self.run_img):
            self.image = self.run_img[self.step_index // 5]
        self.step_index += 1
        if self.step_index >= len(self.run_img) * 5:
            self.step_index = 0
        self.dino_rect.x = self.x
        self.dino_rect.y = self.y
       
    #makes the Dinosaur jump
    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < - self.JUMP_VEL:
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    #Draws the Dinosaur on the screen.
    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

#Defining the Cloud class
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

    #Draws obstacles on the screen.
    def draw(self, SCREEEN):
        SCREEN.blit(self.image, (self.x, self.y))

#Creates the Obstacle class
class Obstacle:
    def __init__(self, image, type):
         self.image = image
         self.type = type
         self.rect = self.image[self.type].get_rect()
         self.rect.x = SCREEN_WIDTH

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x <-self.rect.width: #Ensures that Obstacles are removed as they disappear off the screen.
             obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class smallcactus(Obstacle): #creates the small cactus class to allow for multiple cacti to be spawned.
     def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 325

class Largecactus(Obstacle): #creates the large cactus class to allow for multiple cacti to be spawned.
     def __init__(self, image):
        self.type = random.randint(0,2)
        super().__init__(image, self.type)
        self.rect.y = 300

#Creating the Teradactyl class (called Bird for simplicity sake)
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

#Creating the Game Loop
def main():
    global game_speed, x_bg, y_bg, points, obstacles #makes the specified variables global in scope (they can be accessed throughout the program)
    run = True
    clock = pygame.time.Clock() #to maintain the pace of the game.
    player = Dinosaur() #Created player object from class Dinosaur
    cloud = Cloud() #Created an object of the cloud class
    game_speed = 14 #sets game speed.
    x_bg = 0
    y_bg = 380
    points = 0 #sets points to 0.
    font= pygame.font.Font('freesansbold.ttf',20)
    obstacles = [] #establishes an array for all of the obstacles
    death_count = 0 #stores the number of times the player dies.

    def score():
        global points, game_speed #makes points and game_speed global in scope.
        points += 1 #increments points by 1.
        if points % 100 == 0: #if points divided by 100 has 0 as a remainder then do the following code.
            game_speed += 1 
            text = font.render ("points: "+ points, True, (0, 0 ,0))
            textRect = text.get_rect ()
            textRect.center = (1000, 40) #centers the text.
            SCREEN.blit(text,textRect) #prints text to the screen.                     
                   
    def background():
        global x_bg, y_bg 
        image_width = BACKGROUND.get_width() #Gets the width of the background image.
        SCREEN.blit(BACKGROUND, (x_bg, y_bg)) #Displays the background
        SCREEN.blit(BACKGROUND, (image_width + x_bg, y_bg)), 
        if x_bg <= -image_width:
            SCREEN.blit(BACKGROUND, (image_width + x_bg, y_bg)) #makes the background image move.
            x_bg = 0
            x_bg -= game_speed

    while run: #whilst the game is running.
        for event in pygame.event.get():
            if event.key == pygame.K_ESCAPE: #When escape button pressed, close the program.
                pygame.quit()
                run = False

        SCREEN.fill((255, 255, 255)) #You have to pass in a tuple to represent RGB values in pygame.
        userInput = pygame.key.get_pressed() #stores the user input.

        player.draw(SCREEN) #draws the player character (the dinosaur) to the screen.
        player.update(userInput)

        #Ensures that obstacles spawn and get added to the obstacle list for easy management.
        if len(obstacles) == 0:
           if random.randint(0,2) == 0:
            obstacles.append(smallcactus(SMALL_CACTUS))
           elif random.randint(0,2) == 1:
               obstacles.append(Largecactus(LARGE_CACTUS))
           elif random.randint(0,2) == 2:
               obstacles.append(Bird(TERADACTYL))

        #Ensures obstacles get drawn to the screen
        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect): #detects collisions between the player and obstacles
                pygame.time.delay(500) #pauses the game for 500 miliseconds.
                death_count += 1 #increments the death counter variable by one. (+= 1 increments whichever variable it is assigned to by 1)
                menu(death_count)
           
        #Ensures that clouds get drawn to the screen.
        cloud.draw(SCREEN)
        cloud.update()

        clock.tick(30)
        pygame.display.update() #updates the display.

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255)) #makes the game background white.
        font = pygame.font.Font("freesansbold.ttf", 30) #sets the font for the game
 
        if death_count == 0: #if the game has just started, then display "press any key to start".
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0: #if the player has died before and the game hasn't just started, then display "press any key to restart".
            text = font.render("Press any key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0)) #Prints your score to the screen after you die.
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50) #centers your score.
            SCREEN.blit(score, scoreRect) #prints your score to the screen.
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2) #centers the text.
        SCREEN.blit(text, textRect) #outputs the text to the screen.
        SCREEN.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN: #if any key pressed, start the game.
                main()
 
menu(death_count=0) #starts the game by initially calling the main function in the game loop.