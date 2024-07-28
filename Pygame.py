import pygame
from sys import exit
from random import randint, choice


#Sprite Class for Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.player_index = 0
        #Images loading
        self.player_walk = [pygame.image.load('Images/Player/run/tile000.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile001.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile002.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile003.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile004.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile005.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile006.png').convert_alpha(),
               pygame.image.load('Images/Player/run/tile007.png').convert_alpha()]
        self.player_idle = [pygame.image.load('Images/Player/idle/tile000.png'),
               pygame.image.load('Images/Player/idle/tile001.png'),
               pygame.image.load('Images/Player/idle/tile002.png'),
               pygame.image.load('Images/Player/idle/tile003.png'),
               pygame.image.load('Images/Player/idle/tile004.png'),
               pygame.image.load('Images/Player/idle/tile005.png'),
               pygame.image.load('Images/Player/idle/tile006.png'),
               pygame.image.load('Images/Player/idle/tile007.png'),
               pygame.image.load('Images/Player/idle/tile008.png'),
               pygame.image.load('Images/Player/idle/tile009.png')]
       
        self.player_jump = [pygame.image.load('Images/Player/jump/tile000.png').convert_alpha(),
               pygame.image.load('Images/Player/jump/tile001.png').convert_alpha(),
               pygame.image.load('Images/Player/jump/tile002.png').convert_alpha()]
        self.player_attack = [pygame.image.load('Images/Player/attack/attack (1).png'),
                              pygame.image.load('Images/Player/attack/attack (2).png'),
                              pygame.image.load('Images/Player/attack/attack (3).png'),
                              pygame.image.load('Images/Player/attack/attack (4).png'),
                              pygame.image.load('Images/Player/attack/attack (5).png'),
                              pygame.image.load('Images/Player/attack/attack (6).png'),
                              pygame.image.load('Images/Player/attack/attack (7).png')]

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (90,530))
        self.gravity = 0
        self.is_alive = True
        
    #Player Movements
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 530:
            self.gravity = -20

        elif keys[pygame.K_UP] and self.rect.bottom >= 530:
            self.gravity = -20

        elif keys[pygame.K_RIGHT]:
            self.rect.x += 5
            if self.rect.x > 900:
                self.rect.x = 0
                
        elif keys[pygame.K_LEFT]:
            self.rect.x -=5
            if self.rect.x < 0:
                self.rect.x = 0

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 530:
            self.rect.bottom = 530

    #Player Animation
    def animation_state(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT] and self.rect.bottom == 530) or (keys[pygame.K_LEFT] and self.rect.bottom == 530):
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk):self.player_index = 0 
            self.image = self.player_walk[int(self.player_index)]
        
        elif keys[pygame.K_z]:
            self.player_index += 0.1
            if self.player_index >= len(self.player_attack):self.player_index = 0 
            self.image = self.player_attack[int(self.player_index)]

        elif self.rect.bottom == 530:
            self.player_index += 0.1
            if self.player_index >= len(self.player_idle):self.player_index = 0
            self.image = self.player_idle[int(self.player_index)]
        
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_jump):self.player_index = 0
            self.image = self.player_jump[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

#Sprite Class for enemies
class Enemies(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        #enemies animation
        if type == 'demon':
            self.frames = [pygame.image.load('Images/demon_fly/tile000.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile000.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile001.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile002.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile003.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile004.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/tile005.png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack02 (2).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack02 (3).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack02 (6).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack02 (7).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack02 (8).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack03 (5).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack03 (6).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack03 (7).png').convert_alpha(),
                    pygame.image.load('Images/demon_fly/attack03 (8).png').convert_alpha()]
                    
            y_pos = randint(390,430)
        else:
            self.frames = [pygame.image.load('Images/Slime/Individual Sprites/slime-move-0.png').convert_alpha(),
                  pygame.image.load('Images/Slime/Individual Sprites/slime-move-1.png').convert_alpha(),
                  pygame.image.load('Images/Slime/Individual Sprites/slime-move-2.png').convert_alpha(),
                  pygame.image.load('Images/Slime/Individual Sprites/slime-move-3.png').convert_alpha()]

            y_pos = 530
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):self.animation_index = 0 
        self.image = self.frames[int(self.animation_index)]
    def update(self):
        self.animation_state()
        self.rect.x -= 4
        self.destroy()
    def destroy(self):
        if self.rect.x <= -50:
            self.kill()


def display_score():
    
    current_time = round((pygame.time.get_ticks()/1000)) - start_time
    score_surface = test_font.render('Score:  ' + str(current_time), False, '#03AC13')
    score_rectangle = score_surface.get_rect(center = (464,100))
    screen.blit(score_surface, score_rectangle)
    return current_time

def gameOver():
    screen.fill((94,129,162))
    screen.blit(player_gameOver_scaled, player_gameOver_rect)
    screen.blit(game_name, game_name_rect)
    player_gravity = 0
    score_message = test_font.render(f'Your score: {score}', False, (111,196,169))
    score_message_rect = score_message.get_rect(center=(464, 390))
    if score == 0: 
        screen.blit(game_message, game_message_rect)
        screen.blit(game_maker, game_maker_rect)
    else:
        screen.blit(score_message, score_message_rect)
lives = 3

def collision():
    keys = pygame.key.get_pressed()
    if pygame.sprite.spritecollide(player.sprite,enemies_group,False):
        player.sprite.rect.x = 80  
        player.sprite.rect.y = 530
        enemies_group.empty()
        return False
    else: return True


pygame.init()
screen = pygame.display.set_mode((928, 590))
pygame.display.set_caption("Runners")
clock = pygame.time.Clock()
game_active = False
background = pygame.image.load('Images/Background.png').convert()
test_font = pygame.font.Font('font/Pixeltype.ttf',40)
start_time = 0
score = 0

#Music
bg_music = pygame.mixer.Sound('music.wav')
bg_music.play(loops = -1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
enemies_group = pygame.sprite.Group()



#Intro screen 
player_gameOver = pygame.image.load('Images/Player/tile012.png').convert_alpha() 
player_gameOver_scaled = pygame.transform.rotozoom(player_gameOver,0,2.8)
player_gameOver_rect = player_gameOver_scaled.get_rect(center = (464, 300))

#Game over screen
game_name = test_font.render('Runners',False, (111,196,169))
game_name_rect = game_name.get_rect(center=(464,200))
game_message = test_font.render('Press space to play', False, (111,196,169))
game_message_rect = game_message.get_rect(center=(464,390))
game_maker = test_font.render('Made by: AcFerrer', False,(111,196,169))
game_maker_rect = game_maker.get_rect(center=(464, 80))

#Timer for enemy spawn
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1300)

slime_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(slime_animation_timer, 500)

demon_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(demon_animation_timer, 200)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == obstacle_timer:
            enemies_group.add(Enemies(choice(['demon','slime', 'slime'])))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = round(pygame.time.get_ticks()/1000)


    if game_active:
        screen.blit(background, (0, -200))
        score = display_score()
        game_active = collision()
        player.draw(screen)
        enemies_group.draw(screen)
        enemies_group.update()
        player.update()
                
    else:
        gameOver()
    pygame.display.update()
    clock.tick(60)

#Attack
#Some helpful ramp
#Lives







