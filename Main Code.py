import pygame
from sys import exit

def display_score():
  current_time = int(pygame.time.get_ticks() / 1000) - start_time
  score_surf = my_Font.render(f'Score: {current_time}',False,(64,64,64))
  score_rect = score_surf.get_rect(center = (400,50))
  screen.blit(score_surf,score_rect)
  return current_time

pygame.init()
#display surface w/ a width of 800 and a length of 400
screen = pygame.display.set_mode((800,400))
#name of game
pygame.display.set_caption("Life of a block")

#used to set fps
clock = pygame.time.Clock()
my_Font = pygame.font.Font('platformer/Pixel Font/Minecraft.ttf',45)
game_active = False
start_time = 0
score = 0
scores_list = [score]
print(scores_list)



#backgrounds surfaces
Sky = pygame.image.load("platformer/Backgrounds/Mario empty background sky.png").convert()
Floor = pygame.image.load("platformer/Backgrounds/Mario empty background floor Updated.png").convert()


#character 
enemy_surf = pygame.image.load("platformer/Enemy.png").convert_alpha()
enemy_rect = enemy_surf.get_rect(midbottom = (800,310))


#player
player = pygame.image.load("platformer/Player.png").convert_alpha()
player_rect = player.get_rect(midbottom = (40,310))
player_gravity = 0


#intro screen
player_stand = pygame.image.load("platformer/Standing player.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,45,2.5)


player_stand_rect = player_stand.get_rect(center = (400,300))
game_name = my_Font.render("Life of a Block" , False, 'Yellow')
game_name_rect = game_name.get_rect(center = (400,50))
game_message = my_Font.render("press 'r' to run  ", False, 'Yellow')
game_message_rect = game_message.get_rect(center = (400,100))


#obstacle
obstacle = pygame.image.load("platformer/Obstacle.png").convert_alpha()
obstacle_rect = obstacle.get_rect(midbottom = (250,350))


#while loop that includes all code
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    if game_active:
      if event.type == pygame.KEYDOWN and player_rect.bottom >= 310:
        if event.key == pygame.K_SPACE:
          player_gravity = -20
      if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 310:
        if player_rect.collidepoint(event.pos):
          player_gravity = -20
          start_time = int(pygame.time.get_ticks() / 1000)
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
        game_active = True
        enemy_rect.left = 800
        start_time = int(pygame.time.get_ticks() / 1000)

  #background
  if game_active:
    screen.blit(Sky, (0,0))
    screen.blit(Floor, (0,310))
    score = display_score()

  
    #enemy
    original_speed = 7
    # calculate_level = current_time % 5 
    enemy_rect.x -= original_speed
    if enemy_rect.right <= 0: enemy_rect.left = 800
    screen.blit(enemy_surf,enemy_rect)
    # while current_time >= calculate_level:
    # enemy_rect.x -= original_speed
    #   enemy_rect.x -= original_speed + 3
    
    #player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 310: player_rect.bottom = 310
    screen.blit(player, player_rect)

    #quit function if player and enemy collide
    if enemy_rect.colliderect(player_rect):
      game_active = False
  else:
    screen.fill((94,129,162))
    screen.blit(game_name,game_name_rect)
    screen.blit(player_stand,player_stand_rect)
    current_score = my_Font.render(f"score: {score}", False, 'Yellow')
    current_score_rect = current_score.get_rect(center = (400,110))
    if score == 0:
      screen.blit(game_message,game_message_rect)
    else:
      screen.blit(current_score, current_score_rect)



  pygame.display.update()
  clock.tick(60)
  
  
