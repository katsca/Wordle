from game import Game
import pygame as pg
import sys
from keyboard import KeyBoard
#SET OF COLOURS USED IN WORDLE


def draw_title(screen, width, height, colors):
    font_height = int(height)
    title_font = pg.font.SysFont('assets\fonts\DroidSansMono.ttf', font_height)
    title_surface = title_font.render('WORDLE', False, colors['LINES'])
    title_rect = title_surface.get_rect()
    title_rect.centerx = width // 2  
    title_rect.centery = height // 2  
    screen.blit(title_surface, title_rect)
    
    
def draw_squares(screen, window_width, title_box_height, keyboard_start, colors):
    #Draw the squares 
        segment_width = window_width // 7
        gap_width = int(0.05*segment_width)
        square_width = segment_width - gap_width*2     
        answer_box_height_array = [title_box_height, keyboard_start]
        answer_box_height = answer_box_height_array[1] - answer_box_height_array[0]   
        segment_height = answer_box_height // (game_state.MAX_GUESSES + 1)
        
        square_height = square_width
        
        gap_height = (segment_height - square_height) // 2
        
        displacement = int(0.05*square_width)
            
        #Put the squares in and the text
        answer_font = pg.font.SysFont('assets\fonts\DroidSansMono.ttf', (square_width - 2*displacement))
        for i in range(game_state.MAX_GUESSES):
            string_row_i = game_state.guesses[i][0]
            
            for j in range(0, 5):
                
                color_char = game_state.guesses[i][1][j]
            
                x_position = gap_width + (segment_width * (1+j))
                
                y_position = answer_box_height_array[0] + gap_height + segment_height*i
                
                pg.draw.rect(screen, colors['LINES'], (x_position, y_position, square_width, square_width))
                pg.draw.rect(screen, colors[color_char], (x_position + displacement, y_position + displacement, square_width - 2*displacement, square_width- 2*displacement))
            
                if j < len(string_row_i):
                    answer_surface = answer_font.render(string_row_i[j], False, colors['LINES'])
                    answer_rect = answer_surface.get_rect()
                    answer_rect.centerx = (x_position + displacement) + (square_width - 2*displacement)//2
                    answer_rect.centery = (y_position + displacement) + (square_width - 2*displacement)//2
                    screen.blit(answer_surface, answer_rect)
            
        #Draw the solution line
        y_position += segment_height
        
        for j in range(0, 5):
            x_position = gap_width + (segment_width * (1+j))
            pg.draw.line(screen, colors['LINES'], (x_position, y_position+square_width), (x_position+square_width, y_position+square_width), displacement)
            if game_state.end_game:
                solution = game_state.getSolution()
                answer_surface = answer_font.render(solution[j], False, colors['LINES'])
                answer_rect = answer_surface.get_rect()
                answer_rect.centerx = (x_position + displacement) + (square_width - 2*displacement)//2
                answer_rect.centery = (y_position + displacement) + (square_width - 2*displacement)//2
                screen.blit(answer_surface, answer_rect)

        #Need to know the end position
        




if __name__ == "__main__":
    colors = {"LINES":(207, 202, 194), 'u': (12, 12, 13), 'g': (17, 184, 17), 'o': (204, 125, 6), 'w': (105,103,99), "BG" : (12, 12, 13)}
    game_state = Game()
    dark = True
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((game_state.width, game_state.height), pg.RESIZABLE)
    pg.display.set_caption('Wordle')
    running = True
    key_down = False
    
    title_box_height = int(0.1*game_state.height)
    keyboard_start = int(0.8*game_state.height)
    
    keyboard_object = KeyBoard(game_state.width, game_state.height,  keyboard_start, colors)
    
    
    while running:
        pg.event.pump()
        event = pg.event.wait()
        if event.type == pg.QUIT:
            running = False
        
        #GETTING AN INPUT FOR THE LETTERS
        #Allowed input alpha only
        elif event.type == pg.KEYDOWN:        
            if not key_down:
                
                #If we type a letter make it upper case and if length of guess is smaller than 5 add it to the end
                if event.unicode.isalpha() and not game_state.end_game:
                    current_word = game_state.guesses[game_state.guess_count][0]
                    letter = event.unicode.upper()
                    key_down = True
                    #If the length of the guess is less than 5 letters, then add the letter to the current guess we are on
                    if len(current_word) < 5:
                        game_state.guesses[game_state.guess_count][0] = current_word + letter  
                
                #Delete last character
                elif event.key == pg.K_BACKSPACE and not game_state.end_game:
                    current_word = game_state.guesses[game_state.guess_count][0]
                    key_down = True
                    game_state.guesses[game_state.guess_count][0] = current_word[:-1]
                
                #Check the guess is valid and update the colours
                elif event.key == pg.K_RETURN and not game_state.end_game:
                    current_word = game_state.guesses[game_state.guess_count][0]
                    key_down = True
                    if len(current_word) == 5:   
                        #Word needs to be in our dictionary
                        if game_state.validWord(current_word):
                            #Then we check our result to get the coloursdf
                            game_state.compareGuess(current_word)       
                
                #RESET BUTTON WHEN GAME ENDED WHEN GAME PLAYING
                elif event.key == pg.K_ESCAPE:
                    key_down = True
                    game_state.reset()
                elif event.key == pg.K_LSHIFT:
                    key_down = True
                    if dark:
                        dark = False
                        colors = {"LINES":(12, 12, 13), 'u': (207, 202, 194), 'g': (17, 184, 17), 'o': (204, 125, 6), 'w': (105,103,99), "BG": (207, 202, 194)}
                    else:
                        dark = True
                        
                        colors = {"LINES":(207, 202, 194), 'u': (12, 12, 13), 'g': (17, 184, 17), 'o': (204, 125, 6), 'w': (105,103,99), "BG" : (12, 12, 13)}

        #Check for key up so cannot hold keys down to type                                                     
        elif event.type == pg.KEYUP:
            key_down = False
          
        #Update the window size if altered but ensure the aspect ratio stays the same no matter what  
        elif event.type == pg.VIDEORESIZE:
            w, h = event.w, event.h
            if w / h > game_state.ASPECT_RATIO:
                w = int(h*game_state.ASPECT_RATIO)
            else:
                h = int(w / game_state.ASPECT_RATIO)
            screen = pg.display.set_mode((w, h), pg.RESIZABLE)
            game_state.width = w
            game_state.height = h
            title_box_height = int(0.1*game_state.height)
            keyboard_start = int(0.8*game_state.height)
            keyboard_object.height = game_state.height - keyboard_start
            keyboard_object.width = game_state.width
            keyboard_object.start_height = keyboard_start
        
        #Check for mouse clicks        
        elif event.type == pg.MOUSEBUTTONDOWN and not game_state.end_game:
            #Check for the left click on the keyboard
            if pg.mouse.get_pressed()[0]:
                mouse_x, mouse_y = pg.mouse.get_pos()
                #Work out if it has clicked on a square on the keyboard
                result = keyboard_object.validClick(mouse_x, mouse_y)
                
                #If valid click - update accordingly 
                if result[0] == True:
                    current_word = game_state.guesses[game_state.guess_count][0]
                    letter = result[1]
                    if letter == "ENTER":
                        if len(current_word) == 5:   
                            #Word needs to be in our dictionary
                            if game_state.validWord(current_word):
                                #Then we check our result to get the coloursdf
                                game_state.compareGuess(current_word)   
                    elif letter == "DEL":
                        #Apply backspace
                        game_state.guesses[game_state.guess_count][0] = current_word[:-1]
                    else:
                        if len(current_word) < 5:
                                game_state.guesses[game_state.guess_count][0] = current_word + letter
                        
                
        
        
        #RENDERER
        
        #Set background
        screen.fill(colors["BG"])
        
        #TITLE OF THE GAME PUT THAT IN
        draw_title(screen, game_state.width, title_box_height, colors)
        
        #Draw the answers in
        draw_squares(screen, game_state.width, title_box_height ,keyboard_start, colors)
        
        #Draw keyboard
        keyboard_object.draw_keyboard(screen, game_state.used_letters, colors)
        
        pg.display.flip()
    #Game loop
        


    
