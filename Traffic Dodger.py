import random
import pygame
from time import sleep



class CarRacing:
    pygame.mixer.init()
    enginesound = pygame.mixer.Sound("car-acceleration.mp3")
    enginesound.play(loops=-1)
    

    def __init__(self):
        pygame.init()
        self.display_width = 850
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.initialize()


    
    def initialize(self):
        self.crashed = False
        self.carImg = pygame.image.load(r'7.png')
        self.x = (self.display_width * 0.45)
        self.y = (self.display_height * 0.8)
        self.car_width = 49
        

        self.enemy_car = pygame.image.load(r'6.png')  # You should specify the correct path to the enemy car image.
        self.enemy_car_startx = random.randrange(210, 480)
        self.enemy_car_starty = -600
        self.enemy_car_speed = 3
        self.enemy_car_speed_increment=0.02
        self.enemy_car_width = 49
        self.enemy_car_height = 100

        self.bgImg = pygame.image.load(r'road.png')
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 5

        self.count = 0
        self.high_score = self.load_high_score()  # Initialize the high score
    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                high_score_str=file.read().strip()
                if high_score_str:
                    return int(high_score_str)
                else:
                    return 0
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))
    def car(self, x, y):
        self.gameDisplay.blit(self.carImg, (x, y))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Traffic Dodger")
        self.run_car()

    def run_car(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.x -= 40
                    if event.key == pygame.K_RIGHT:
                        self.x += 40

            self.gameDisplay.fill(self.black)
            self.back_ground_road()
            self.run_enemy_car(self.enemy_car_startx, self.enemy_car_starty)
            self.enemy_car_starty += self.enemy_car_speed
            self.enemy_car_speed+=self.enemy_car_speed_increment
            if self.enemy_car_starty > self.display_height:
                self.enemy_car_starty = 0 - self.enemy_car_height
                self.enemy_car_startx = random.randrange(210, 480)

            self.car(self.x, self.y)
    
            if self.check_collision():
                self.crashed = True
                brakesound = pygame.mixer.Sound("car crash.mp3")
                brakesound.play()
                
                if self.count > self.high_score:
                    self.high_score = self.count  # Update high score if needed
                self.display_message("Game Over!!")
            if self.x < 210 or self.x > 480:
                self.crashed = True
                if self.count > self.high_score:
                    self.high_score = self.count  # Update high score if needed
                self.display_message("Game Over!!")
            if not self.crashed:
                self.count += 1

            self.highscore(self.count,self.high_score)    
            pygame.display.update()
            self.clock.tick(60)

    def check_collision(self):
        if self.y < self.enemy_car_starty + self.enemy_car_height and self.y + self.car_width > self.enemy_car_starty:
            if self.x > self.enemy_car_startx and self.x < self.enemy_car_startx + self.enemy_car_width:
                return True
                
            if self.x + self.car_width > self.enemy_car_startx and self.x + self.car_width < self.enemy_car_startx + self.enemy_car_width:
                return True
        return False

    def display_message(self, msg):
        font = pygame.font.SysFont("Comic Sans MS", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height()))
        font = pygame.font.SysFont("Comic Sans MS", 36)
        high_score_text = font.render("High Score: " + str(self.high_score), True, (255, 255, 255))
        self.gameDisplay.blit(high_score_text, (400 - high_score_text.get_width() // 2, 320))

        self.display_credit()
        
        pygame.display.update()
        self.clock.tick(60)
        sleep(2)
        self.save_high_score()
        self.initialize()
        self.racing_window()

    def back_ground_road(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))
        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600
        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_enemy_car(self, thingx, thingy):
        self.gameDisplay.blit(self.enemy_car, (thingx, thingy))

    def highscore(self, count,high_score):
        font = pygame.font.SysFont("Comic Sans MS", 20)
        text = font.render("Score: " + str(count), True, self.white)
        high_score_text=font.render("High Score:" + str(high_score),True,self.white)
        self.gameDisplay.blit(text, (0, 0))
        self.gameDisplay.blit(high_score_text,(180,0))


    def display_credit(self):
        font = pygame.font.SysFont("Comic Sans MS", 16)
        text = font.render("Thanks for playing this game", True, self.white)
        self.gameDisplay.blit(text, (600, 500))
        text = font.render("By", True, self.white)
        self.gameDisplay.blit(text, (600, 520))
        text = font.render("Rishon D Souza", True, self.white)
        self.gameDisplay.blit(text, (600, 540))

if __name__ == "__main__":
    Car_racing = CarRacing()
    Car_racing.racing_window()

