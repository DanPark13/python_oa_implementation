# python_oa_implementation
Daniel Park's Implementation of the Original Sorting Algorithm

To give some context for implementing the original algorithm (OA) for the project, I’ve attached a Perspectives article I wrote for Science.   

An earlier paper that summarizes my 1995 MIT PhD thesis gives detailed explanations for making the variations and implementing the algorithm.  I’ve attached it as well. 

CantoVario has moved much farther from the original algorithm of 1995, but working with the original algorithm and MIDI will give you an idea of what’s ahead. 

Your first step is to implement in python the original algorithm detailed in the attached Chaos paper “Musical Variations from a Chaotic Mapping.”  Cantovario is programmed in python, but for your work right now, what’s most important is understanding how the OA produces variations.

I’ve attached MIDI files of the following so you can check your results:

    Bach prelude mm 1-11 (first 2 phrases = 176 notes)
    35-measure Bach prelude
    Gershwin prelude

Best approach is to start with the Bach 176 MIDI file and try to duplicate Variations 1 and 2 in the paper.  You can send these 2 variations to me when you’ve made them.

I’ve also attached a python implementation of the runge-kutta algorithm, as well as instructions on how the sort is done in the OA (original algorithm explained in the Chaos journal paper:  Musical Variations from a Chaotic Mapping).  You’ll want to implement that sort in order to reproduce the variations shown in the paper.  Also, the Lorenz parameter b (beta) has to be set to 2.  
