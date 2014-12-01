import os

__author__ = 'Roni'
from psychopy.visual import SimpleImageStim
os.chdir(os.path.dirname(__file__))

from psychopy import visual, core, logging
globalClock=core.Clock()
logging.setDefaultClock(globalClock)
lastLog=logging.LogFile(f="..\\lastRun.log", level=logging.EXP, filemode='w')
win=visual.Window(fullscr=True)
print os.getcwd()

im1 = SimpleImageStim(win, image=os.path.join('..','stimuli', '1.bmp'), units='', pos=(0.0, 0.0), flipHoriz=False, flipVert=False, name='PW1',
                autoLog=True)
im1.draw()
win.flip()

core.wait(8.0)

