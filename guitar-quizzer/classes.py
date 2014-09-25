import glob
import os
import pdb
from random import choice
import sys
import time

ROOT = os.path.sep.join(os.getcwd().split(os.path.sep)[0:-1])

# Directories for different types of things to quiz on.
QDIRS = {
    'chords' : os.path.join(ROOT, 'files', 'chords'),
    'intervals' : os.path.join(ROOT, 'files', 'intervals'),
    'arpeggios' : os.path.join(ROOT, 'files', 'arpeggios'),
    'scale degrees' : os.path.join(ROOT, 'files', 'scale_degress'),
    'chords in a key' : os.path.join(ROOT, 'files', 'chords_in_a_key'),
}

# QCLASSES = {
#     'chords' : Chords,
#     'intervals' : Intervals,
#     'arpeggios' : Arpeggios,
#     'scale degrees' : ScaleDegrees,
#     'chords in a key' : ChordsInAKey,
# }
# 
class ContinuousQuestions:
    def __init__(self, fn):
        with open(fn) as f:
            lines = [x.strip() for x in f.readlines()]
        self.questions = lines

class StopAndGoQuestions:
    def __init__(self):
        with open(fn) as f:
            lines = [x.strip().split('\t') for x in f.readlines()]
        self.questions = [x[0] for x in lines]
        self.answers = dict(zip(
            [x[0] for x in lines],
            [x[1] for x in lines]
        ))

# class Chords(ContinuousQuestions):
#     def __init__(self, fn):
#         """
#         Initialize Chords object from file fn
#         """
#         ContinuousQuestions.__init__(fn)
#         self.name = os.path.splitext(os.path.split(fn)[1])[0]
# 
#     def get_random_choice(self):
#         return choice(self.chords)

class Quizzer:
    def __init__(self, interval=5):
        # Time interval between questions for continuous questioning.
        self.interval = 5
        self.quiz_type = self.get_quiz_type()
        self.quizdir = QDIRS[self.quiz_type]
        self.question_set = self.get_question_set()
        self.set_questions()
        if self.question_type == 'continuous':
            self.current_time_interval = self.get_time_interval(interval)
        # self.chord_sets = self.make_chord_sets()
        # self.current_chord_set = self.get_chord_set()
        # self.quizzing = True
        # self.quiz()

    def set_questions(self):
        with open(self.question_set) as f:
            lines = [x.strip() for x in f.readlines()]
        if sum(['\t' in x for x in lines]) == len(lines):
            self.questions = [x[0] for x in lines]
            self.answers = dict(zip(
                [x[0] for x in lines],
                [x[1] for x in lines]
            ))
            self.question_type = 'stop_and_go'
        else:
            self.questions = lines
            self.question_type = 'continuous'
        
    def get_time_interval(self, interval):
        string = ('How many seconds would you like between questions?\n'
                  'Hit RETURN for the default: {:,}\n\n'.format(interval))
        interval = raw_input(string)
        try:
            interval = float(interval)
            assert interval > 0
            sys.stdout.write('\nInterval set for {:,} '
                             'seconds\n\n'.format(interval))
        except (ValueError, AssertionError):
            string = ('You didn\'t enter a valid number, setting interval '
                      'to {:,} seconds.\n\n'.format(interval))
            sys.stdout.write(string)
        return interval

    def _choice_from_numbered_list(self, vals):
        s = ''
        for i, v in enumerate(vals):
            s += '{}: {}\n'.format(i + 1, v)
        s += '\n'
        while True:
            response = raw_input(s)
            try:
                index = int(response) - 1
                assert index in range(len(vals))
                sys.stdout.write('\n')
                break
            except (ValueError, AssertionError):
                sys.stdout.write('You didn\'t enter a valid number, try '
                                 'again.\n\n')
        return index 

    def get_quiz_type(self):
        s = 'Enter the number of the type of quiz you\'d like to try.\n\n'
        sys.stdout.write(s)
        index = self._choice_from_numbered_list(QDIRS.keys())
        return QDIRS.keys()[index]

    def get_question_set(self):
        import glob
        s = 'Enter the number of the chord set you\'d like to practice\n\n'
        sys.stdout.write(s)
        question_sets = glob.glob(os.path.join(self.quizdir, '*.txt'))
        question_sets = dict(zip(
            [os.path.split(x)[1][:-4] for x in question_sets],
            question_sets
        ))
        index = self._choice_from_numbered_list(question_sets.keys())
        return question_sets[question_sets.keys()[index]]

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





