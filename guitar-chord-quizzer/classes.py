import glob
import os
import pdb
from random import choice
import sys
import time

# Time interval between chords
INTERVAL = 5.0

class ChordSet:
    def __init__(self, fn):
        """
        Initialize ChordSet object from file fn
        """
        self.name = os.path.splitext(os.path.split(fn)[1])[0]
        with open(fn) as f:
            lines = [ x.strip() for x in f.readlines() ]
        self.chords = lines

    def get_random_choice(self):
        return choice(self.chords)

class Quizzer:
    def __init__(self):
        self.chord_sets = self.make_chord_sets()
        self.current_chord_set = self.get_chord_set_from_user()
        self.current_time_interval = self.get_time_interval_from_user()
        self.quizzing = True
        self.quiz()
        
    def get_time_interval_from_user(self):
        string = ('How many seconds would you like between chords?\n'
                  'Hit RETURN for the default: {:,}\n\n'.format(INTERVAL))
        interval = raw_input(string)
        try:
            interval = float(interval)
            assert interval > 0
            sys.stdout.write('\nInterval set for {:,} '
                             'seconds\n\n'.format(interval))
        except (ValueError, AssertionError):
            string = ('You didn\'t enter a valid number, setting interval '
                      'to {:,} seconds.\n\n'.format(INTERVAL))
            sys.stdout.write(string)
            interval = INTERVAL
        return interval

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
                sys.stdout.write('\n')
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

    def quiz(self):
        from select import select
        sys.stdout.write('Beginning quiz\n\n')
        time.sleep(2)
        sys.stderr.write("\x1b[2J\x1b[H")
        while True:
            # time.sleep(self.current_time_interval)
            # chord = self.current_chord_set.get_random_choice()
            # in = raw_input('\n{}\n'.format(chord))
            # if in != '':
            #     break
            chord = self.current_chord_set.get_random_choice()
            sys.stdout.write('{}\n\n'.format(chord))
            rlist, _, _ = select([sys.stdin], [], [], 
                                 self.current_time_interval)
            if rlist:
                break





