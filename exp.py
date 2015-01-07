#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.81.02), December 08, 2014, at 14:45
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment 
expName = u'exp'  # from the Builder filename that created this script
expInfo = {'participant':'', 'runNumber':'1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
runNumber = int(expInfo['runNumber'])
# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_run%i_%s' %(expInfo['participant'], runNumber, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1440, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, units='deg'
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']= 60#win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "inst"
instClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'The experiment will begin shortly',    font=u'Arial',
    pos=[0, 0], height=1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[8, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-1.0)
image_2 = visual.ImageStim(win=win, name='image_2',
    image='sin', mask=None,
    ori=0, pos=[0,0], size=[8, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-2.0)
image_3 = visual.ImageStim(win=win, name='image_3',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[8, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-3.0)
image_4 = visual.ImageStim(win=win, name='image_4',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[8, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    interpolate=True, depth=-4.0)
memory_inst = visual.ImageStim(win=win, name='memory_inst',
    image='stimuli\\memory_inst.bmp', mask=None,
    ori=0, pos=[0, 4],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 
logging.setDefaultClock(globalClock)
#------Prepare to start Routine "inst"-------
t = 0
instClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
scan_t = event.BuilderKeyResponse()  # create an object of type KeyResponse
scan_t.status = NOT_STARTED
# keep track of which components have finished
instComponents = []
instComponents.append(text)
instComponents.append(scan_t)
for thisComponent in instComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
trials = data.TrialHandler(nReps=1, method='sequential',
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'Scripts\\run%d.csv' % runNumber),
    name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
  # so we can initialise stimuli with some values
#-------Start Routine "inst"-------
continueRoutine = True


# set up handler to look after randomisation of conditions etc
text.setAutoDraw(True)
win.flip()
keys = event.getKeys(keyList=['T','t','escape'])
event.waitKeys(['return'])
globalClock.reset()
routineTimer.reset()
routineTimer.add(24.000000)
text.setAutoDraw(False)
win.flip()
if('escape' in keys):
    core.quit()
while routineTimer.getTime() > 0:
    continue
for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)

    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    routineTimer.add(12.000000)
    # update component parameters for each repeat


    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(image)
    trialComponents.append(image_2)
    trialComponents.append(image_3)
    trialComponents.append(image_4)
    trialComponents.append(memory_inst)
    key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_2.status = NOT_STARTED
    trialComponents.append(key_resp_2)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED


    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *image* updates
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            thisExp.addData("start",globalClock.getTime())
            thisTrial = trials.trialList[0]
            # keep track of start time/frame for later
            # ISI.tStart = t  # underestimates by a little under one frame
            # ISI.frameNStart = frameN  # exact frame index
            # ISI.start(8.0)
            ISI.status = STARTED
            if thisTrial != None:
                for paramName in thisTrial.keys():
                    exec(paramName + '= thisTrial.' + paramName)
            image.setImage(stim1)
            if (stim2 != '' and stim2 != False):
                image_2.setImage(stim2)
            if (stim3 != '' and stim3 != False):
                image_3.setImage(stim3)
                image_4.setImage(stim4)


        if t >= 8.0 and image.status == NOT_STARTED:
            thisExp.addData("start stim",globalClock.getTime())
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (8.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)

            # *image_2* updates
        elif t >= 9.0 and image_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_2.tStart = t  # underestimates by a little under one frame
            image_2.frameNStart = frameN  # exact frame index
            image_2.setAutoDraw(True)
        elif image_2.status == STARTED and t >= (9.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_2.setAutoDraw(False)

        # *image_3* updates
        elif t >= 10.0 and image_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_3.tStart = t  # underestimates by a little under one frame
            image_3.frameNStart = frameN  # exact frame index
            image_3.setAutoDraw(True)
        elif image_3.status == STARTED and t >= (10.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_3.setAutoDraw(False)

        # *image_4* updates
        elif t >= 11.0 and image_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_4.tStart = t  # underestimates by a little under one frame
            image_4.frameNStart = frameN  # exact frame index
            image_4.setAutoDraw(True)
        elif image_4.status == STARTED and t >= (11.0 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            image_4.setAutoDraw(False)


        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
            
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
            
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('rt', key_resp_2.rt)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
print event.getKeys()
core.wait(20)
win.close()
core.quit()
