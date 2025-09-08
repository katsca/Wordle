import pygame as pg
from collections import defaultdict
class KeyBoard:
    
    #Constructor
    def __init__(self, width, end_height, start_height, color):
        #Height of the keyboard segment
        self.height = end_height - start_height
        #Width of keyboard segment
        self.width = width
        #Start height of the keyboard on the screen
        self.start_height = start_height
        #The characters used on the keyboard
        self.keyboard_characters = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"], ["A", "S", "D", "F", "G", "H", "J", "K", "L"], ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "DEL"]]
        #Set of coordinates [top left, top right, width, height] : relate to a letter
        self.keys_coords = defaultdict()
      
    #Check if mouse click was valid and return the letter it clicked on if it was  
    def validClick(self, x, y):
        
        #Check the position the mouse clicked on exists between any of the button coordinates and return the associated letter or Nothing and whether the click was valid or not
        for coords in self.keys_coords.keys():
            
            if ( x > coords[0] and x < coords[0]+coords[2]):
                
                if (y > coords[1] and y < coords[1]+coords[3]):
                    
                    return True, self.keys_coords[coords]
                
        return False, None
        
        
    #Draw the keyboard out onto the screen
    def draw_keyboard(self, screen, used_letters, color):
        #Indent from the top of the key board segment start
        outer_indent_height = 0.1*self.height
        #Area where we put a key height      
        segment_height = (self.height - 2*outer_indent_height) / 3
        #The indent between the keys - height
        inner_indent_height = 0.05*segment_height
        #The height of the bordering rectangles of keys
        rectangle_height = segment_height - 2*inner_indent_height
        
        #Indent from the left of the key board segment start
        outer_indent_width = 0.1*self.width
        #Area where we put a key width   
        segment_width = (self.width - 2* outer_indent_width) / 10 
        #The indent between the keys - width    
        inner_indent_width = 0.05*segment_width
        #The width of the bordering rectangles of keys
        rectangle_width = segment_width - 2*inner_indent_width
        #The size of the border of the rectangles
        displacement_width = rectangle_width * 0.05
        displacement_height = rectangle_height * 0.05
        
        #Font for the letters - single
        keyboard_font_1 = pg.font.SysFont('assets\fonts\DroidSansMono.ttf', int(rectangle_height))
        #Font for the letters - enter and del
        keyboard_font_2 = pg.font.SysFont('assets\fonts\DroidSansMono.ttf', int(0.5*rectangle_height))
        
        #For each row in the keyboard
        for i in range(0, 3):
            #The top height of each segment
            y_position = self.start_height + outer_indent_height + segment_height*i
            
            
            if i == 0: # row 0
                
                #Starting x position of row 0
                x_position = outer_indent_width
                
                #Iterate over 10 keys
                for j in range(0, 10):
                    
                    #Draw the bordering rectangle accounting for the indent in the segments
                    pg.draw.rect(screen , color["LINES"], (x_position + inner_indent_width, y_position+inner_indent_height, rectangle_width, rectangle_height))
                    
                    #Choose the color of the inside rectangle
                    color_char = 'u'
                    if self.keyboard_characters[i][j] in used_letters.keys():
                        color_char = used_letters[self.keyboard_characters[i][j]]
                    
                    #Draw the inside rectangle
                    pg.draw.rect(screen , color[color_char], (x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height))
                    
                    #Add this rectangle coords and the letter to the dictionary to keep track of keyboard coords
                    self.keys_coords[x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height] = self.keyboard_characters[i][j]
                    
                    #Add the letter ontop of the rectangle - centred
                    letter_surface = keyboard_font_1.render(self.keyboard_characters[i][j], False, color["LINES"])
                    letter_rect = letter_surface.get_rect()
                    letter_rect.centerx = x_position + inner_indent_width + (rectangle_width - 2*displacement_width )/2 + displacement_width
                    letter_rect.centery = y_position + inner_indent_height + (rectangle_height - 2*displacement_height)/2  + displacement_height    
                    screen.blit(letter_surface, letter_rect)
                    
                    #Update the x position
                    x_position += segment_width
                    
            elif i == 1: # row 1
                
                #Starting x position of row 1
                x_position = outer_indent_width + 0.5*segment_width
                
                #Iterate over 9 keys
                for j in range(0, 9): 
                    
                    #Draw the bordering rectangle accounting for the indent in the segments
                    pg.draw.rect(screen , color["LINES"], (x_position + inner_indent_width, y_position+inner_indent_height, rectangle_width, rectangle_height))
                    
                    #Choose the color of the inside rectangle
                    color_char = 'u'
                    if self.keyboard_characters[i][j] in used_letters.keys():
                        color_char = used_letters[self.keyboard_characters[i][j]]
                    
                    #Draw the inside rectangle
                    pg.draw.rect(screen , color[color_char], (x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height))
                    
                    #Add this rectangle coords and the letter to the dictionary to keep track of keyboard coords
                    self.keys_coords[x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height] = self.keyboard_characters[i][j]
                    
                    #Add the letter ontop of the rectangle - centred
                    letter_surface = keyboard_font_1.render(self.keyboard_characters[i][j], False, color["LINES"])
                    letter_rect = letter_surface.get_rect()
                    letter_rect.centerx = x_position + inner_indent_width + (rectangle_width - 2*displacement_width )/2 + displacement_width
                    letter_rect.centery = y_position + inner_indent_height + (rectangle_height - 2*displacement_height)/2  + displacement_height
                    screen.blit(letter_surface, letter_rect)
                    
                    #Update the x position
                    x_position += segment_width
                    
            else: # row 2
                
                #Starting x position of row 2
                x_position = outer_indent_width
                
                #Iterate over 9 keys
                for j in range(0, 9):
                    
                    #Default the shift in x to segment width like previously
                    x_addition = segment_width
                    
                    #If the keys is (enter = 0) or (delete = 8)
                    if j == 0 or j == 8:
                        
                        #Use a bigger rectangle width
                        rectangle_width_big = 1.5*(rectangle_width)
                        
                        #Draw the bordering rectangle accounting for the indent in the segments
                        pg.draw.rect(screen , color["LINES"], (x_position + inner_indent_width, y_position+inner_indent_height, rectangle_width_big, rectangle_height))
                        
                        #Draw the inside rectangle
                        pg.draw.rect(screen , color['u'], (x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width_big - 2*displacement_width, rectangle_height-2*displacement_height))
                        
                        #Add this rectangle coords and the letter to the dictionary to keep track of keyboard coords
                        self.keys_coords[x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width_big - 2*displacement_width, rectangle_height-2*displacement_height] = self.keyboard_characters[i][j]
                        
                        #Choose the correct font for the keys
                        letter_surface = keyboard_font_2.render(self.keyboard_characters[i][j], False, color["LINES"])
               
                        #Set the rectangle width for this key
                        rectangle_width_temp = rectangle_width_big
                        
                        #Change the addition in x to 1 and half segment widths
                        x_addition = 1.5* segment_width
                    
                    else:
                        
                        #Draw the bordering rectangle accounting for the indent in the segments
                        pg.draw.rect(screen , color["LINES"], (x_position + inner_indent_width, y_position+inner_indent_height, rectangle_width, rectangle_height)) 
                        
                        #Choose the color of the inside rectangle
                        color_char = 'u'
                        if self.keyboard_characters[i][j] in used_letters.keys():
                            color_char = used_letters[self.keyboard_characters[i][j]]
                        
                        #Draw the inside rectangle
                        pg.draw.rect(screen , color[color_char], (x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height))
                        
                        #Add this rectangle coords and the letter to the dictionary to keep track of keyboard coords
                        self.keys_coords[x_position + inner_indent_width + displacement_width, y_position+inner_indent_height+displacement_height, rectangle_width - 2*displacement_width, rectangle_height-2*displacement_height] = self.keyboard_characters[i][j]
                        
                        #Choose the correct font for the keys
                        letter_surface = keyboard_font_1.render(self.keyboard_characters[i][j], False, color["LINES"])
                        
                        #Set the rectangle width for this key
                        rectangle_width_temp = rectangle_width
                        
                    #Add the letter ontop of the rectangle - centred
                    letter_rect = letter_surface.get_rect()   
                    letter_rect.centerx = x_position + inner_indent_width + (rectangle_width_temp - 2*displacement_width )/2 + displacement_width
                    letter_rect.centery = y_position + inner_indent_height + (rectangle_height - 2*displacement_height)/2  + displacement_height
                    screen.blit(letter_surface, letter_rect)
                    
                    #Update the x position
                    x_position += x_addition