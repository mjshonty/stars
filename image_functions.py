import pygame

def text_box(box_type, box_width, box_height):
    if box_type == "input_box":
        input_box = pygame.image.load('images\\text-box_M.gif')
        input_box = pygame.transform.scale( input_box, (box_width, box_height))
        return input_box
    elif box_type == "display_box":
        display_box = pygame.image.load('images\\text-box_LG.gif')
        display_box = pygame.transform.scale( display_box, (box_width, box_height))
        return display_box