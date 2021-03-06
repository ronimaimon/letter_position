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

CONFIGURATION_FILE = u'data\\%s\\loc.csv'
BLOCK_DURATION = 24.0
IMAGE12_TIME = 23.0
IMAGE11_TIME = 22.0
IMAGE10_TIME = 21.0
IMAGE9_TIME = 20.0
IMAGE8_TIME = 19.0
IMAGE7_TIME = 18.0
IMAGE6_TIME = 17.0
IMAGE5_TIME = 16.0
IMAGE4_TIME = 15.0
IMAGE3_TIME = 14.0
IMAGE2_TIME = 13.0
IMAGE1_TIME = 12.0
IMAGE_DURATION = 0.8

REFRESH_RATE = 60
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment 
expName = u'localizer'  # from the Builder filename that created this script
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
runNumber = 1
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s/%s_run%i_%s' %(expInfo['participant'],expName, runNumber, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
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
    text=u'......',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)
fixation = visual.TextStim(win=win, ori=0, name='text',
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
image_3 = visual.ImageStim(win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_5 = visual.ImageStim(win=win, name='image_5',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_6 = visual.ImageStim(win=win, name='image_6',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_7 = visual.ImageStim(win=win, name='image_7',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_8 = visual.ImageStim(win=win, name='image_8',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_9 = visual.ImageStim(win=win, name='image_9',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_10 = visual.ImageStim(win=win, name='image_10',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_11 = visual.ImageStim(win=win, name='image_11',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=STIMULI_SIZE,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_12 = visual.ImageStim(win=win, name='image_12',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=STIMULI_SIZE,
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
    trialList=data.importConditions(CONFIGURATION_FILE % expInfo['participant']),
    name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
# set up handler to look after randomisation of conditions etc
text.setAutoDraw(True)
win.flip()
keys = event.getKeys(keyList=['T','t','escape'])
event.waitKeys(['return'])
globalClock.reset()
routineTimer.reset()
routineTimer.add(BEGIN_TRIAL_DELAY)
text.setAutoDraw(False)
win.flip()
if('escape' in keys):
    core.quit()
while routineTimer.getTime() > 0:
    continue
for thisTrial in trials:
    trialComponents = []
    trialComponents.append(image)
    trialComponents.append(image_2)
    trialComponents.append(image_3)
    trialComponents.append(image_4)
    trialComponents.append(image_5)
    trialComponents.append(image_6)
    trialComponents.append(image_7)
    trialComponents.append(image_8)
    trialComponents.append(image_9)
    trialComponents.append(image_10)
    trialComponents.append(image_11)
    trialComponents.append(image_12)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    t = 0
    trialClock.reset()  # clock
    routineTimer.add(BLOCK_DURATION)
    #-------Start Routine "trial"-------
    continueRoutine = True
    isFirstFrame = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        # *ISI* period
        if isFirstFrame and t >= 0.0:
            thisExp.addData("start",globalClock.getTime())
            fixation.setAutoDraw(True)
            win.flip()
            isFirstFrame = False
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)
            image.setImage(stim1)
            image_2.setImage(stim2)
            image_3.setImage(stim3)
            image_4.setImage(stim4)
            image_5.setImage(stim5)
            image_6.setImage(stim6)
            image_7.setImage(stim7)
            image_8.setImage(stim8)
            image_9.setImage(stim9)
            image_10.setImage(stim10)
            image_11.setImage(stim11)
            image_12.setImage(stim12)

        if t >= IMAGE1_TIME and image.status == NOT_STARTED:
            thisExp.addData("start stim",globalClock.getTime())
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            fixation.setAutoDraw(False)
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (IMAGE1_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)

            # *image_2* updates
        elif t >= IMAGE2_TIME and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.setAutoDraw(True)
        elif image_2.status == STARTED and t >= (IMAGE2_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)

        # *image_3* updates
        elif t >= IMAGE3_TIME and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.setAutoDraw(True)
        elif image_3.status == STARTED and t >= (IMAGE3_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)

        # *image_4* updates
        elif t >= IMAGE4_TIME and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t  # underestimates by a little under one frame
            image_4.setAutoDraw(True)
        elif image_4.status == STARTED and t >= (IMAGE4_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_4.setAutoDraw(False)
            
        elif t >= IMAGE5_TIME and image_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_5.tStart = t  # underestimates by a little under one frame
            image_5.setAutoDraw(True)
        elif image_5.status == STARTED and t >= (IMAGE5_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_5.setAutoDraw(False)
            
        elif t >= IMAGE6_TIME and image_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_6.tStart = t  # underestimates by a little under one frame
            image_6.setAutoDraw(True)
        elif image_6.status == STARTED and t >= (IMAGE6_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_6.setAutoDraw(False)            

        elif t >= IMAGE7_TIME and image_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_7.tStart = t  # underestimates by a little under one frame
            image_7.setAutoDraw(True)
        elif image_7.status == STARTED and t >= (IMAGE7_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_7.setAutoDraw(False)
            
        elif t >= IMAGE8_TIME and image_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_8.tStart = t  # underestimates by a little under one frame
            image_8.setAutoDraw(True)
        elif image_8.status == STARTED and t >= (IMAGE8_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_8.setAutoDraw(False)
        
        elif t >= IMAGE9_TIME and image_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_9.tStart = t  # underestimates by a little under one frame
            image_9.setAutoDraw(True)
        elif image_9.status == STARTED and t >= (IMAGE9_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_9.setAutoDraw(False)
            
        elif t >= IMAGE10_TIME and image_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_10.tStart = t  # underestimates by a little under one frame
            image_10.setAutoDraw(True)
        elif image_10.status == STARTED and t >= (IMAGE10_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_10.setAutoDraw(False)
            
        elif t >= IMAGE11_TIME and image_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_11.tStart = t  # underestimates by a little under one frame
            image_11.setAutoDraw(True)
        elif image_11.status == STARTED and t >= (IMAGE11_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_11.setAutoDraw(False)
            
        elif t >= IMAGE12_TIME and image_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_12.tStart = t  # underestimates by a little under one frame
            image_12.setAutoDraw(True)
        elif image_12.status == STARTED and t >= (IMAGE12_TIME + (IMAGE_DURATION -win.monitorFramePeriod*0.75)): #most of one frame period left
            image_12.setAutoDraw(False)

        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break

        if event.getKeys(keyList=RESPONSE_KEY):
            thisExp.addData("keyPressed",RESPONSE_KEY)
            thisExp.addData("keyRT",trialClock.getTime())
        # check for quit (the Esc key)
        if event.getKeys(keyList=["escape"]):
            core.quit()
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    thisExp.nextEntry()
core.wait(END_TRIAL_DELAY)
win.close()
core.quit()
