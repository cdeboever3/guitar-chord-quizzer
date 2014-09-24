guitar-quizzer
====================

A simple command line guitar quizzer.

# Development

I'd like to be able to test several things.

* intervals
* chords
* arpeggios
* scale degrees
* chords in a key

## Notes

I'd like at least two quizzing modes. One mode waits for the correct answer
while the other mode has a set time interval and assumes one is practicing on a
guitar or something.  I'll call this continuous questioning. The second mode
should probably show the correct answer (if possible).  I'll call this
stop-and-go questioning.

### Class organization

I can have a general quizzer class and then different types of things
(intervals, chords, etc.) can implement some specific functions that the
quizzer will use.
