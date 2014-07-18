import glob
import os
import pdb
import sys

class ChordSet:
    def __init__(self, fn):
        """
        Initialize ChordSet object from file fn
        """
        self.name = os.path.splitext(os.path.split(fn)[1])[0]
        with open(fn) as f:
            lines = [ x.strip() for x in f.readlines() ]
        self.chords = lines            

class Quizzer:
    def __init__(self):
        self.chord_sets = self.make_chord_sets()
        self.current_chord_set = self.get_chord_set_from_user()
        self.quizzing = True

    def get_chord_set_from_user(self):
        string = ('Enter the number of the chord set you\'d like to practice.'
                  '\n\n')
        for i, v in enumerate(self.chord_sets):
            string += '{}: {}\n'.format(i + 1, v.name)
        string += '\n'
        while True:
            current_chord_set = raw_input(string)
            try:
                index = int(current_chord_set) - 1
                assert index >= 0
                assert index < len(self.chord_sets)
                break
            except (ValueError, AssertionError):
                sys.stdout.write('You didn\'t enter a valid number, try '
                                 'again.\n\n')
        return self.chord_sets[index]

    def make_chord_sets(self):
        root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        chords_files = glob.glob(os.path.join(root, 'chords', '*'))
        chord_sets = [ChordSet(fn) for fn in chords_files]
        return chord_sets
