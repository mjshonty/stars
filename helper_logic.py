import pygame
from pygame_gui import *
import sys
import palette
import screen_setup
import image_functions

clock = pygame.time.Clock() # keeps track of time for use with refresh rate

width, height, scale = screen_setup.screen_setup() # returns intial values for screen setup and scaling

input_box_width, input_box_height = screen_setup.sizing("input_box", width, height) # returns values for the height and width of the input box for the user appears
display_box_width, display_box_height = screen_setup.sizing("display_box", width, height) # returns values for the height and width of the input box for the user appears

new_width, new_height = screen_setup.scaling(width, height, scale) # returns the new width and height for sclaing map images

screen, background = screen_setup.inital_screen(width, height) # gives us our surfaces the main screen and a background

screen.fill(palette.color_palette("background")) #set the backgroudn color of our screen to the background color


screen_rect = screen.get_rect() # gives us the size of our screen as a rectangle and passes it into screen_rect

input_box = image_functions.text_box("input_box", input_box_width, input_box_height)
display_box = image_functions.text_box("display_box", display_box_width, display_box_height)


display_box_rect = display_box.get_rect() # gives us the size of our scaled map as a rectangle and passes it into map_rect
display_box_rect.topleft = screen_rect.topleft # sets the map to the right side of the screen

input_box_rect = input_box.get_rect() # gives us the size of our scaled map as a rectangle and passes it into map_rect
input_box_rect.bottomleft = screen_rect.bottomleft # sets the map to the right side of the screen

# typing_rect = input_box_rect #creates a slightly smaller rectangle for the user's typing field

# typing_rect = typing_rect.inflate(-25, -25)

typing_rect = screen_setup.typing_area("input_box",input_box_rect)


# font = pygame.font.Font('fonts\\dogicapixel.ttf', 20) # setting font type and font size
# text = font.render('''This is the text I'm rendering to show\n
#  it wrapping''', True, palette.color_palette("text")) # setting text to the message we want to display

input_box_manager = UIManager((width, height), 'line_entry.JSON')
text_input_box = elements.UITextEntryLine(relative_rect=pygame.Rect(typing_rect), manager = input_box_manager)
text_input_box.set_allowed_characters("numbers")

story_box_manager = UIManager((width, height), 'text_box_theme.JSON')
story_box_rect = screen_setup.typing_area("story_box", display_box_rect)
story_box = elements.UITextBox('hello! <br><br>', relative_rect=pygame.Rect(story_box_rect), manager = story_box_manager)

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
        screen.blit(display_box, story_box_rect)
        screen.blit(screen, (0,0))
        input_box_manager.draw_ui(screen)
        story_box_manager.draw_ui(screen)
        pygame.display.update()
 