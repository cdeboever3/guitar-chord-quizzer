import os
import sys

class ChordSet:
    def __init__(self, fn):
        """
        Initialize ChordSet object from file fn
        """
        self.name = os.path.splitext(fn)[0]
        with open(fn) as f:
            lines = [ x.strip() for x in f.readlines() ]
        self.chords = lines            

class Quizzer:
    def __init__(self):
        self.alive = True
        string = 'Enter the number of the chord set you\'d like to practice.\n'
        raw_input(string)
        # show chord sets and number them
        # gather input, check if correct, proceed
        raw_input

        
        self.quizzing = True
