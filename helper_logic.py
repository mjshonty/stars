# # # Majority of the code is currently housed here

import pygame
from pygame_gui import *
import sys
import palette
import screen_setup
import image_functions

clock = pygame.time.Clock() # keeps track of time for use with refresh rate

width, height, scale = screen_setup.screen_setup() # returns intial values for screen setup and scaling
                                                   # takes no arguments, but returns 3 values -
                                                   # screen width, screen height, and scale

input_box_width, input_box_height = screen_setup.sizing("input_box", width, height) # returns values for the height and width of the input box for the user appears
                                                                                    # takes 3 arguments -
                                                                                    # box_type which informs if the box is for the input or the story display
                                                                                    # height and width to size the boxes
                                                                                    # returns new values for scaling

display_box_width, display_box_height = screen_setup.sizing("display_box", width, height) # returns values for the height and width of the input box for the user appears
                                                                                          

new_width, new_height = screen_setup.scaling(width, height, scale) # returns the new width and height for sclaing map images
                                                                   # takes 3 arguments -
                                                                   # width, height, scale

screen, background = screen_setup.inital_screen(width, height) # returns surfaces the main screen and a background

screen.fill(palette.color_palette("background")) #set the backgroudn color of our screen to the background color
                                                 # currently 3 possible values: background, text, and line


screen_rect = screen.get_rect() # gives us the size of our screen as a rectangle and passes it into screen_rect

input_box = image_functions.text_box("input_box", input_box_width, input_box_height) # returns a text box image scaled to size for user input
                                                                                     # takes 3 arguments
                                                                                     # box_type which can be input_box or display_box
                                                                                     # the box height and width which are set up earlier on in the program

display_box = image_functions.text_box("display_box", display_box_width, display_box_height) # returns a text box image scaled to size for user input


display_box_rect = display_box.get_rect() # returns the size of the scaled story display as a rectangle
display_box_rect.topleft = screen_rect.topleft # sets the story display to the top left of the screen

input_box_rect = input_box.get_rect() # returns the size of the scaled input box as a rectangle
input_box_rect.bottomleft = screen_rect.bottomleft # sets the input box to the left side of the screen


typing_rect = screen_setup.typing_area("input_box",input_box_rect) # returns a rect used to place the input or output of a box
                                                                   # takes 2 arguments
                                                                   # input_box or story_box based to know if it's for input or output
                                                                   # the rect set up in the .get_rect() method above


input_box_manager = UIManager((width, height), 'line_entry.JSON') # UI manager for the input_box. Needs to have whole screen size, 
                                                                  # takes a JSON styling file for use on UI components

text_input_box = elements.UITextEntryLine(relative_rect=pygame.Rect(typing_rect), placeholder_text="Awaiting your decision... ", manager = input_box_manager)
text_input_box.set_allowed_characters("numbers")

story_box_manager = UIManager((width, height), 'text_box_theme.JSON')
story_box_manager.add_font_paths("dogica","fonts\\dogicapixel.ttf")

story_box_manager.preload_fonts([{'name': 'dogica', 'pixel_size': 24, 'style': 'regular'}])

story_box_rect = screen_setup.typing_area("story_box", display_box_rect)
story_box = elements.UITextBox('<font face=dogica pixel_size=20 color=#bedc7f>'
                               ''
    'This is a a very long message to display how some of this stuff works so please enjoy!'
    'As I continue to tell you the tale of a million years, but unfortuantely I forgot'
    'so I will contintue to say things and type', relative_rect=pygame.Rect(story_box_rect), manager = story_box_manager)
story_box.set_active_effect(TEXT_EFFECT_TYPING_APPEAR)
# Update the display
pygame.display.flip()


def draw_screen(): # current main loop
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

            input_box_manager.process_events(event)
            story_box_manager.process_events(event)

        input_box_manager.update(time_delta)
        story_box_manager.update(time_delta)

        screen.blit(input_box, input_box_rect)
        screen.blit(display_box, (story_box_rect.x -10, story_box_rect.y - 25))
        screen.blit(screen, (0,0))
        input_box_manager.draw_ui(screen)
        story_box_manager.draw_ui(screen)
        pygame.display.update()
 