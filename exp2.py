#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), December 08, 2014, at 14:45
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, gui,monitors
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
from constants import *

CONFIGURATION_FILE = u'data\\%s\\exp2-run%d.csv'
BLOCK_DURATION = 4.0
IMAGE2_TIME = 0.7
IMAGE_DURATION = 0.3
IMAGE1_TIME = 0
REFRESH_RATE = 60
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment 
expName = u'Adaptation'  # from the Builder filename that created this script
expInfo = {'participant':'', 'runNumber':'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
runNumber = int(expInfo['runNumber'])
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s/%s_run%i_%s' %(expInfo['participant'],expName, runNumber, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=False, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file
# Setup the Window
mon = monitors.Monitor(name='my-monitor',distance=SCREEN_DISTANCE_IN_CM,width=SCREEN_WIDTH_IN_CM)
mon.setSizePix(SCREEN_RESOLUTION)
win = visual.Window(SCREEN_RESOLUTION,fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor=mon, color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='deg'
    )
# store frame rate of monitor if we can measure it successfully
if(REFRESH_RATE==None):
    REFRESH_RATE = win.getActualFrameRate()
expInfo['frameRate']= REFRESH_RATE#win.getActualFrameRate()

# Initialize components for Routine "trial"
trialClock = core.Clock()

text = visual.TextStim(win=win, ori=0, name='text',
    text=u'.......',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
fixation = visual.TextStim(win=win, ori=0, name='fixation',
    text='+',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
logging.setDefaultClock(globalClock)
#------Prepare to start Routine "inst"-------
trials = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(CONFIGURATION_FILE % (expInfo['participant'],runNumber)),
    name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
# set up handler to look after randomisation of conditions etc
# while routineTimer.getTime() > 0:
#     continue
for i in range(trials.nTotal):
    thisTrial = trials.next()
    if(i==0):
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec (paramName + '= thisTrial.' + paramName)
            image.setImage(stim1)
            image_2.setImage(stim2)
        text.setAutoDraw(True)
        win.flip()
        keys = event.getKeys(keyList=['T','t','escape'])
        event.waitKeys(['return'])
        globalClock.reset()
        routineTimer.reset()
        routineTimer.add(BEGIN_TRIAL_DELAY+4)
        text.setAutoDraw(False)
        fixation.setAutoDraw(True)
        win.flip()
        if('escape' in keys):
            core.quit()

    trialComponents = []
    trialComponents.append(fixation)
    trialComponents.append(image)
    trialComponents.append(image_2)
    for thisComponent in trialComponents:
        thisComponent.status = NOT_STARTED
    t = 0
    #-------Start Routine "trial"-------
    continueRoutine = True
    isFirstFrame = True
    while routineTimer.getTime() > 0:
        continue
    trialClock.reset()  # clock
    routineTimer.add(BLOCK_DURATION)
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        # *ISI* period
        if t >= 1.4 and fixation.status == NOT_STARTED:
            thisExp.addData("start",globalClock.getTime())
            fixation.setAutoDraw(True)
            win.flip()
            if(i+1 < trials.nTotal):
                nextTrial = trials.getFutureTrial()
                for paramName in nextTrial.keys():
                    exec(paramName + '= nextTrial.' + paramName)
                image.setImage(stim1)
                if (stim2 != '' and stim2 != False):
                    image_2.setImage(stim2)

        if t >= IMAGE1_TIME and image.status == NOT_STARTED:

            thisExp.addData("start stim",globalClock.getTime())
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            fixation.setAutoDraw(False)
            fixation.status = NOT_STARTED
            image.setAutoDraw(True)
            win.flip()
        elif image.status == STARTED and t >= (IMAGE1_TIME + (IMAGE_DURATION)): #most of one frame period left
            image.setAutoDraw(False)
            win.flip()

            # *image_2* updates
        elif t >= IMAGE2_TIME and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.setAutoDraw(True)
            win.flip()
        elif image_2.status == STARTED and t >= (IMAGE2_TIME + (IMAGE_DURATION)): #most of one frame period left
            image_2.setAutoDraw(False)
            win.flip()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break

        if event.getKeys(keyList=RESPONSE_KEY):
            thisExp.addData("keyPressed",RESPONSE_KEY)
            thisExp.addData("keyRT",globalClock.getTime())
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()


    
    #-------Ending Routine "trial"-------
    fixation.setAutoDraw(False)
    win.flip()
    thisExp.nextEntry()
core.wait(END_TRIAL_DELAY)
win.close()
core.quit()
