from collections import defaultdict
import random

class Game:
    def __init__(self):
        
        #Set up the data set of words
        self.__word_collection, self.__total_number_words = self.__loadWords()
        
        #initialize a solution
        self.__solution = self.__generateSolution()
        
        #Max number of guesses
        self.MAX_GUESSES = 6
        
        #What the guesses are
        self.guesses = [['', ['u', 'u', 'u', 'u', 'u']] for _ in range(6)]
        self.guess_count = 0
        
        #Default window height and width
        self.width = 600
        self.height = 800
        self.ASPECT_RATIO = self.width / self.height
        
        #End of game state
        self.end_game = False
        
        #Used letters
        self.used_letters = defaultdict()
        
        self.dark = True
        
        
    def __loadWords(self):
        #Load the words from text file into dictionary where each i is a integer number
        word_collection = defaultdict()
        total = 0
        with open("data\words.txt", "r") as textfile:
            for i, line in enumerate(textfile):
                word_collection[i] = line.strip().upper()
            total = i
        return word_collection, total
                
    def __generateSolution(self):
        #Pick a random number associated with a word from the database
        position = random.randint(0, self.__total_number_words)
        return self.__word_collection[position]
        
        
    def compareGuess(self, word_to_check):
        #Create an empty array to represent the colours for this row
        colours = [None] * 5
        
        for i in range(len(word_to_check)):
            
            #Correct position and correct letter - set to green and update used letters and associated color to green
            if self.__solution[i] == word_to_check[i]:
                colours[i] = 'g'
                self.used_letters[word_to_check[i]] = 'g'
                    
            else:
                #Correct letter but wrong place - update to orange
                if word_to_check[i] in self.__solution:
                    
                    colours[i] = 'o'
                    
                    #If the letter is already used and not green update to orange
                    if (word_to_check[i] in self.used_letters.keys()):
                        if self.used_letters[word_to_check[i]] != 'g':
                            self.used_letters[word_to_check[i]] = 'o'
                    
                    #Else if not used add to used letters with associted color orange
                    else:
                        self.used_letters[word_to_check[i]] = 'o'
                
                else:
                    #Wrong word and wrong position set color to WRONG
                    colours[i] = 'w'
                    self.used_letters[word_to_check[i]] = 'w'
        
        #Update guess list with word and associated colors for each character    
        self.guesses[self.guess_count] = ([word_to_check, colours])
        
        #Update the number of guesses made
        self.guess_count += 1
        
        #If we got the solution end the game or If we run out of guesses end the game
        if word_to_check == self.__solution or self.guess_count == self.MAX_GUESSES:
            self.end_game = True        
        
    #Reset the game
    def reset(self):
        self.guesses = [['', ['u', 'u', 'u', 'u', 'u']] for _ in range(6)]
        self.guess_count = 0
        self.__solution = self.__generateSolution()
        self.end_game = False
        self.used_letters.clear()
        
    def validWord(self, word_to_check):
        #Check word exists
        if word_to_check in self.__word_collection.values():
            
            #Check not already made the guess - return false if have
            for i in range(0,self.guess_count):
                if self.guesses[i][0] == word_to_check:
                    return False   
                
            #Return true if all satisfied
            return True
    
        return False
    
    def getSolution(self):
        #return private solution variable
        return self.__solution