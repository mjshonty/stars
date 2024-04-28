import pygame

pygame.init()
pygame.display.set_caption('Testing') # set the name of the window
width = 1600 # set width to the current width of the user's display
height = 1024 # set height to the current height of the user's display

### Color Palette Hex to RGBA
      # eeffcc = 238, 255, 204, 1
      # bedc7f = 190, 220, 127, 1
      # 89a257 = 137, 162, 87, 1
      # #4d8061 = 77, 128, 97, 1
      # 305d42 = 48, 93, 66, 1
      # 1e3a29 = 30, 58, 41, 1
      # background color - 040c06 = 4, 12, 6, 1 

    

background_color = (4, 12, 6, 1)
text_color = (190, 220, 127, 1)
line_color = (238, 255, 204, 1)

scale = .1

text_box_width = int(width* .4)
text_box_height = int (height * .2)

new_width = int(width * scale) # create a new width based on scale
new_height = int(height * scale) # create a new heigh based on scale

screen = pygame.display.set_mode((width, height), pygame.SCALED|pygame.FULLSCREEN)

screen.fill(background_color)


imp = pygame.image.load('images\\text-box_LG.gif')
imp = pygame.transform.scale( imp, (text_box_width, text_box_height))
screen_rect = screen.get_rect() # gives us the size of our screen as a rectangle and passes it into screen_rect

imp3 = imp.get_rect() # gives us the size of our scaled map as a rectangle and passes it into map_rect
imp3.bottomleft = screen_rect.bottomleft # sets the map to the right side of the screen

map1 = pygame.image.load('images\icon-label_01_deep-space.gif')
map2 = pygame.image.load('images\icon-label_02_silk-road-trading-route.gif')
map3 = pygame.image.load('images\icon-label_03_astroid-mining-fields.gif') #far left of screen
map4 = pygame.image.load('images\icon-label_04_lawless_lands.gif')
map5 = pygame.image.load('images\icon-label_05_dying-sun-p1075.gif')
map6 = pygame.image.load('images\icon-label_06_imperial-garrison.gif')
map7 = pygame.image.load('images\icon-label_07_battle-for-freedom-graveyard.gif')
map8 = pygame.image.load('images\icon-label_08_the-hive.gif')
map9 = pygame.image.load('images\icon-label_09_trade-guild-outpost.gif')

map1 = pygame.transform.scale( map1, (new_width,new_height))
map2 = pygame.transform.scale( map2, (new_width,new_height))
map3 = pygame.transform.scale( map3, (new_width,new_height))
map4 = pygame.transform.scale( map4, (new_width,new_height))
map5 = pygame.transform.scale( map5, (new_width,new_height))
map6 = pygame.transform.scale( map6, (new_width,new_height))
map7 = pygame.transform.scale( map7, (new_width,new_height))
map8 = pygame.transform.scale( map8, (new_width,new_height))
map9 = pygame.transform.scale( map9, (new_width,new_height))

map1_rect = map1.get_rect()
map2_rect = map2.get_rect()
map3_rect = map3.get_rect()
map4_rect = map4.get_rect()
map5_rect = map5.get_rect()
map6_rect = map6.get_rect()
map7_rect = map7.get_rect()
map8_rect = map8.get_rect()
map9_rect = map9.get_rect()

map1_rect.bottomright = screen_rect.bottomright
map2_rect.bottomright = screen_rect.bottomright
map3_rect.bottomright = screen_rect.bottomright
map4_rect.bottomright = screen_rect.bottomright
map5_rect.bottomright = screen_rect.bottomright
map6_rect.bottomright = screen_rect.bottomright
map7_rect.bottomright = screen_rect.bottomright
map8_rect.bottomright = screen_rect.bottomright
map9_rect.bottomright = screen_rect.bottomright


map1_rect.x -= (750)
map1_rect.y -= (50)

map2_rect.x -= (725)
map2_rect.y -= (275)

map3_rect.x -= (350)
map3_rect.y -= (75) 

map4_rect.x -= (450)
map4_rect.y -= (450)

map5_rect.x -= (785)
map5_rect.y -= (550)

map6_rect.x -= (750)
map6_rect.y -= (850)

map7_rect.x -= (475)
map7_rect.y -= (775)

map8_rect.x -= (50)
map8_rect.y -= (500)

map9_rect.x -= (50)
map9_rect.y -= (900)





screen.blit(map1, map1_rect)
screen.blit(map2, map2_rect)
screen.blit(map3, map3_rect)
screen.blit(map4, map4_rect)
screen.blit(map5, map5_rect)
screen.blit(map6, map6_rect)
screen.blit(map7, map7_rect)
screen.blit(map8, map8_rect)
screen.blit(map9, map9_rect)

screen.blit(imp, imp3)

font = pygame.font.Font('fonts\dogicapixel.ttf', 20) # setting font type and font size
text = font.render('''This is the text I'm rendering to show\n
 it wrapping''', True, text_color) # setting text to the message we want to display
text_rect = text.get_rect()
text_rect.bottomleft = screen_rect.bottomleft
text_rect.x += 10
text_rect.y -= 120

# Update the display
pygame.display.flip()

done = False # main loop of the game
while not done:
    for event in pygame.event.get(): # for loop to check events
        if event.type == pygame.KEYDOWN: # if the key is pressed down
            if event.key == pygame.K_ESCAPE: # and if that key is the ESCAPE key
                done = True # set done to True and
                break # break out of the for loop
            elif event.key == pygame.K_1: # press the one key to make the following happen
                screen.blit(text,(text_rect.x+20, text_rect.y-5))
                pygame.draw.line(screen, line_color, (map5_rect.x+100, map5_rect.y+75), (map4_rect.x+10, map4_rect.y+25), width=5) # Basically the two coordinates are the X,Y start point to the X,Y end point
                pygame.draw.line(screen, line_color, (map4_rect.x+100, map4_rect.y+60), (map3_rect.x+50, map3_rect.y), width=5) # Basically the two coordinates are the X,Y start point to the X,Y end point
                pygame.draw.line(screen, line_color, (map9_rect.x+50, map9_rect.y+60), (map3_rect.x+50, map3_rect.y), width=5) # Basically the two coordinates are the X,Y start point to the X,Y end point
                pygame.display.flip()
        elif event.type == pygame.QUIT:
            done = True
            break # break out of the for loop
    if done:
        break # to break out of the while loop
 
pygame.quit() # deactivates the pygame library