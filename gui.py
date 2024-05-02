import pygame
from pygame_gui import *
import sys
from pygame_gui.core.text import *

pygame.init()
pygame.display.set_caption('Testing') # set the name of the window
width = 1600 # set width to the current width of the user's display
height = 1024 # set height to the current height of the user's display

clock = pygame.time.Clock()



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

text_box_width = int(width* .5)
text_box_height = int (height * .125)

display_box_width= int(width* .4)
display_box_height = int (height * .2)

new_width = int(width * scale) # create a new width based on scale
new_height = int(height * scale) # create a new heigh based on scale

screen = pygame.display.set_mode((width, height), pygame.SCALED|pygame.FULLSCREEN)
background = pygame.Surface((width, height))

screen.fill(background_color)

text_box = pygame.image.load('text-box_M.gif')
text_box = pygame.transform.scale( text_box, (text_box_width, text_box_height))
screen_rect = screen.get_rect() # gives us the size of our screen as a rectangle and passes it into screen_rect

imp = pygame.image.load('images\\text-box_LG.gif')
imp = pygame.transform.scale( imp, (display_box_width, display_box_height))
imp3 = imp.get_rect() # gives us the size of our scaled map as a rectangle and passes it into map_rect
imp3.topleft = screen_rect.topleft # sets the map to the right side of the screen

text_box_rect = text_box.get_rect() # gives us the size of our scaled map as a rectangle and passes it into map_rect
text_box_rect.bottomleft = screen_rect.bottomleft # sets the map to the right side of the screen

typing_rect = text_box_rect

typing_rect = typing_rect.inflate(-25, -25)

font = pygame.font.Font('fonts\\dogicapixel.ttf', 20) # setting font type and font size
text = font.render('''This is the text I'm rendering to show\n
 it wrapping''', True, text_color) # setting text to the message we want to display

text_box_manager = UIManager((width, height), 'line_entry.JSON')
test_text_entry = elements.UITextEntryLine(relative_rect=pygame.Rect(typing_rect), manager = text_box_manager)
test_text_entry.set_allowed_characters("numbers")

# Update the display
pygame.display.flip()


def get_user_name():
    is_running = True
    while is_running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    break
            elif event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

            text_box_manager.process_events(event)

        text_box_manager.update(time_delta)

        screen.blit(text_box, text_box_rect)
        screen.blit(imp,imp3)
        screen.blit(text, (imp3.x + 10, imp3.y + 50 ))
        screen.blit(screen, (0,0))
        text_box_manager.draw_ui(screen)

        pygame.display.update()
get_user_name()
 
pygame.quit() # deactivates the pygame library
sys.exit()