from psychopy import visual, core, data, event, logging, sound, gui
import numpy as np  # whole numpy lib is available, prepend 'np.'
from psychopy.constants import *  # things like STARTED, FINISHED
from numpy.random import random, randint, normal, shuffle
import pandas as pd
import random

FILE= 'check3.csv'
# gui requesting participant info
participant_id = gui.Dlg(title="WORDS experiment") 
participant_id.addText('Subject Info')
participant_id.addField('Group number:')
participant_id.addField('Type:', choices=['Type_1', 'Type_0'])
participant_id.addField('Participant:')

participant_id.show()

if participant_id.OK:
    Group = participant_id.data[0]                     #saves data from dialogue box into the variable 'Participant'
    Condition = participant_id.data[1]                     #saves data from dialogue box into the variable 'Condition'
    Participant = participant_id.data[2]                     #saves data from dialogue box into the variable 'Condiion'

else:
    core.quit()

columnss = ['Group', 'Word', 'Validity', 'Condition','Participant']
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

     T - E - M - S - H - C - A
     
Press ENTER after every word you write
'''
escape = '''Press ESCAPE when you are done writing words or the time is over'''
letters = ['t','e','m','s','h','c','a']

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
            'Group': Group,
            'Word': input,
            'Validity':'nan',
            'Condition':Condition,
            'Participant': Participant}, ignore_index=True)
        DATA.to_csv('data3/WORDS_'+Participant+'.csv')
        input = ''
    elif key[0] == 'backspace':
        input = input[0:-1]
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
        DATA.to_csv('data3/WORDS_'+Participant+'.csv')
    if event.getKeys():
        break
DATA.to_csv('data3/WORDS_'+Participant+'.csv')
msg(exit)
event.waitKeys(keyList = 'space')
