from psychopy import visual, core, data, event, logging, sound, gui
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import *  # things like STARTED, FINISHED
from numpy.random import random, randint, normal, shuffle
import pandas as pd
import random

FILE= 'check.csv'
# gui requesting participant info
participant_id = gui.Dlg(title="WORDS experiment",size=1) 
participant_id.addText('Subject Info')
participant_id.addField('Participant:')

participant_id.show()

if participant_id.OK:
    Participant = participant_id.data[0]                     #saves data from dialogue box into the variable 'ID'
else:
    core.quit()

columnss = ['Participant', 'Word', 'Validity']
indexs = np.arange(0)
DATA = pd.DataFrame(columns=columnss, index = indexs) 

win = visual.Window(fullscr=True, color='grey', colorSpace='rgb', units = 'pix', allowStencil=True)


text = '''Welcome to this new experiment!! \


The task is rather simple: Write as many words as you can. There are only a few rules: \


1. You can only use the letters that will appear on top of the screen.
2. Do not use capital letters.
3. Write only English words spelled in their standard form.
4. Each letter can only be used ONCE within each word.
5. Derived words count too: that is, you can write both "dog" and "dogs".
6. Press ENTER when you have written a word and want to continue
7. Have fun!

Press SPACE to continue
'''

words = '''
The ONLY letters you can use are

     E - S - W - T - L - B - A
     
Press ENTER after every word you writes
'''
escape = '''Press ESCAPE when you are done writing words or the time is over'''
letters = ['e','s','w','t','l','b','a']

exit = '''The experiment is now over. Please press SPACE to exit'''
mouse = event.Mouse()
def msg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center') # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
    win.flip() # flip the screen to reveal the stimulus
def mesg(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center', pos =(0,((win.size[1]/2)-100))) # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
def msge(txt):
    instructions = visual.TextStim(win, text=txt, color = 'white', height = 20,alignHoriz='center', pos =(0,-((win.size[1]/2)-100))) # create an instruction text
    instructions.draw() # draw the text stimulus in a "hidden screen" so that it is ready to be presented 
input = ''

msg(text)
event.waitKeys(keyList = 'space')

while True:
    mesg(words)
    msge(escape)
    msg(input)
    key = event.waitKeys()
    if key[0] == 'return':
        DATA = DATA.append({
            'Participant': Participant,
            'Word': input,
            'Validity':'nan'}, ignore_index=True)
        DATA.to_csv('data/WORDS_'+Participant+'.csv')
        input = ''
    elif key[0] == 'backspace':
        input = input[0:-1]
        msg(input)
    elif key[0] == 'escape':
        break
    else:
        input = input+str(key[0])

STIM = pd.read_csv(FILE, sep = ';')
Words = STIM.Words.tolist() 

t=-1
while t != len(DATA)-1:
    msg('Preliminary analysis going on. Please wait :-)')
    for t in range(len(DATA)):
        output = DATA['Word'][t]
        if output in Words:
            DATA['Validity'][t]=1
        else:
            DATA['Validity'][t]=0
        DATA.to_csv('data/WORDS_'+Participant+'.csv')
    if event.getKeys():
        break
DATA.to_csv('data/WORDS_'+Participant+'.csv')
msg(exit)
event.waitKeys(keyList = 'space')
