from psychopy.visual import SimpleImageStim
import os, random, cPickle
import csv
from psychopy import gui
from constants import *
os.chdir(os.path.dirname(__file__))
expName = u'generate_sequences'  # from the Builder filename that created this script
expInfo = {'participant':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
data_path = os.path.join('data',expInfo['participant'])
os.mkdir(data_path)

NO_OF_RUNS = 2
class PWBlocks:
    def __init__(self, path,second_path,block_len):
        self.block_len = block_len
        self.root = path
        self.second_root = second_path

    def splitToRuns(self,runs=[]):
        random.shuffle(runs)
        all_blocks = []
        for root, dirs, files in os.walk(self.root, topdown=False):
            random.shuffle(files)

            for j in range(len(files)/self.block_len):
                names1 = []
                names2 = []
                for i in range(self.block_len):
                    file_name = files.pop()
                    names1.append(os.path.join(self.root,file_name))
                    names2.append(os.path.join(self.second_root,file_name))
                all_blocks.append(names1)
                all_blocks.append(names2)
        random.shuffle(all_blocks)
        for i in range(len(runs)):
            runs[i] = runs[i]+ all_blocks[int(len(all_blocks)*((i+0.0)/len(runs))):int(len(all_blocks)*((i+1.0)/len(runs)))]


class Triplets:
    def __init__(self, path):
        self.root = path
    def splitToRuns(self,runs=[]):
        types = ['base','sub','trans']
        all_blocks = []
        for root, dirs, files in os.walk(self.root, topdown=False):
            for name in dirs:
                random.shuffle(types)
                path = os.path.join(root, name)
                for i in range(len(types)):
                    all_blocks.append([os.path.join(self.root,name,'base'+'.png'),(os.path.join(self.root,name,types[i]+'.png'))])
        random.shuffle(all_blocks)
        for i in range(len(runs)):
            print i ," from: ",len(all_blocks)*((i+0.0)/len(runs))," to: ",len(all_blocks)*((i+1.0)/len(runs))
            runs[i] = runs[i]+ all_blocks[int(len(all_blocks)*((i+0.0)/len(runs))):int(len(all_blocks)*((i+1.0)/len(runs)))]


class LocalizerBlocks:
    def __init__(self, path,second_path,block_len):
        self.block_len = block_len
        self.root = path
        self.second_root = second_path

    def getRun(self):
        random.shuffle(runs)
        all_blocks = []
        for root, dirs, files in os.walk(self.root, topdown=False):
            random.shuffle(files)
            for j in range(len(files)/self.block_len):
                names1 = []
                names2 = []
                for i in range(self.block_len):
                    file_name = files.pop()
                    names1.append(os.path.join(self.root,file_name))
                    names2.append(os.path.join(self.second_root,file_name))
                all_blocks.append(names1)
                all_blocks.append(names2)
        random.shuffle(all_blocks)
        return all_blocks


def generateMVPARuns():
    global z2, runs, run, i, index, catch_trial, flat_run, word, word2, word3, loc, file, header, wr
    z2 = PWBlocks(os.path.join( 'stimuli', 'Z2'), os.path.join('stimuli', 'Z3'), 4)
    runs = [[], [],[],[]]
    z2.splitToRuns(runs)
    catch_trials = os.listdir(os.path.join('stimuli', 'Catch'))
    catch_trials = map(lambda file: os.path.join('stimuli', 'Catch',file),catch_trials)
    random.shuffle(catch_trials)
    for run in runs:
        random.shuffle(run)
        for i in range(len(run) / 5):
            index = (5 * (i + 1)) - random.randrange(3) + i
            flat_run = sum(run[:index], [])
            word = flat_run[random.randrange(len(flat_run))]
            word2 = flat_run[random.randrange(len(flat_run))]
            word3 = flat_run[random.randrange(len(flat_run))]
            catch_block = [word, word2, word3]
            catch_block.insert(random.randrange(4),catch_trials[i])
            run.insert(index, catch_block)
    for i in range(len(runs)):
        file = open(os.path.join(data_path,'exp1-run' + str(i + 1) + '.csv'), 'wb')
        header = ['stim1', 'stim2', 'stim3', 'stim4']
        wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(header)
        wr.writerows(runs[i])
        file.close()
    i=0
    for run in runs:
        tr_file = open(os.path.join(data_path,'exp1-run' + str(i + 1) + '-TRs.txt'), 'wb')
        tr = BEGIN_TRIAL_DELAY/2 + 5
        tr_file.write("%d\t%d\tREST\r\n" %(1,tr-1))
        for trial in run:
            all = "".join(trial)
            if all.find("Catch") >0:
                tr_file.write("%d\t%d\tCATCH\r\n" %(tr,tr+5))
            elif all.find("Z2")>0:
                tr_file.write("%d\t%d\tZ2\r\n" %(tr,tr+5))
            else:
                tr_file.write("%d\t%d\tZ3\r\n" %(tr,tr+5))
            tr+=6
        i+=1
        tr_file.close()


def generateLocalizerRun():
    global loc, run, file, header, wr
    loc = LocalizerBlocks(os.path.join('stimuli', 'FF'), os.path.join('stimuli', 'W'), 12)
    run = loc.getRun()
    file = open(os.path.join(data_path,'loc.csv'), 'wb')
    header = ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10', 'stim11',
              'stim12']
    wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(header)
    wr.writerows(run)
    file.close()

    tr_file = open(os.path.join(data_path,'loc-TRs.txt'), 'wb')
    tr = BEGIN_TRIAL_DELAY/2 +1
    tr_file.write("%d\t%d\tREST\r\n" %(1,tr-1))
    for trial in run:
        all = "".join(trial)
        if all.find("FF") >0:
            tr_file.write("%d\t%d\tREST\r\n" %(tr,tr-5))
            tr_file.write("%d\t%d\tFF\r\n" %(tr+6,tr+11))
        else:
            tr_file.write("%d\t%d\tREST\r\n" %(tr,tr-5))
            tr_file.write("%d\t%d\tLANG\r\n" %(tr+6,tr+11))
        tr+=12
    tr_file.close()

def generateTriplets():
    runs = [[], [],[],[]]
    t = Triplets(os.path.join('stimuli','Triplets'))
    t.splitToRuns(runs)
    print runs
    catch_trials = os.listdir(os.path.join('stimuli', 'Catch'))
    catch_trials = map(lambda file: os.path.join('stimuli', 'Catch',file),catch_trials)
    random.shuffle(catch_trials)
    for run in runs:
        random.shuffle(run)
        for i in range(len(run) / 7):
            index = (7 * (i + 1)) - random.randrange(4) + i
            flat_run = sum(run[:index], [])
            word = flat_run[random.randrange(len(flat_run))]
            catch_block = [word]
            catch_block.insert(random.randrange(2),catch_trials[i])
            run.insert(index, catch_block)
    for i in range(len(runs)):
        file = open(os.path.join(data_path,'exp2-run' + str(i + 1) + '.csv'), 'wb')
        header = ['stim1', 'stim2']
        wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(header)
        wr.writerows(runs[i])
        print runs[i]
        file.close()
    i=0
    for run in runs:
        tr_file = open(os.path.join(data_path,'exp2-run' + str(i + 1) + '-TRs.txt'), 'wb')
        tr = BEGIN_TRIAL_DELAY/2 + 3
        tr_file.write("%d\t%d\tREST\r\n" %(1,tr-1))
        for trial in run:
            all = "".join(trial)
            if all.find("Catch") >0:
                tr_file.write("%d\t%d\tCATCH\r\n" %(tr,tr+1))
            elif all.find("sub") >0:
                tr_file.write("%d\t%d\tSUBS\r\n" %(tr,tr+1))
            elif all.find("trans")>0:
                tr_file.write("%d\t%d\tTRANS\r\n" %(tr,tr+1))
            else:
                tr_file.write("%d\t%d\tSAME\r\n" %(tr,tr+1))
            tr+=2
        i+=1
        tr_file.close()


print os.path.dirname(__file__)
generateTriplets()
generateMVPARuns()
generateLocalizerRun()