import pygame

def screen_setup():
    pygame.init()
    pygame.display.set_caption('Stars') # set the name of the window
    width = 1600 # set width to the current width of the user's display
    height = 1024 # set height to the current height of the user's display
    scaele = .1
    return [width,height,scaele]

def sizing(box_type, width, height):
    if box_type == "input_box":
        input_box_width = int(width* .5)
        input_box_height = int (height * .125)
        return input_box_width ,input_box_height
    elif box_type == "display_box":
        display_box_width = int (width * .4)
        display_box_height = int (height * .2)
        return display_box_width, display_box_height

def scaling(width, height, scale):
    new_width = int(width * scale) # create a new width based on scale
    new_height = int(height * scale) # create a new heigh based on scale
    return new_width, new_height

def inital_screen(width, height):    
    screen = pygame.display.set_mode((width, height), pygame.SCALED|pygame.FULLSCREEN)
    background = pygame.Surface((width, height))
    return screen, background

def typing_area(box_type, box_rect):
    if box_type == "input_box":
        typing_rect = box_rect #creates a slightly smaller rectangle for the user's typing field
        typing_rect = typing_rect.inflate(-25, -25)
        return typing_rect
    elif box_type == "story_box":
        story_box_rect = box_rect
        story_box_rect = story_box_rect.inflate(-25, -25)
        return story_box_rect