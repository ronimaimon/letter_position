from psychopy.visual import SimpleImageStim
import os, random, cPickle
import csv
os.chdir(os.path.dirname(__file__))

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
                    names1.append(os.path.join(self.root[3:],file_name))
                    names2.append(os.path.join(self.second_root[3:],file_name))
                all_blocks.append(names1)
                all_blocks.append(names2)
        random.shuffle(all_blocks)
        runs[0] = runs[0]+ all_blocks[:len(all_blocks)/2]
        runs[1] = runs[1]+ all_blocks[len(all_blocks)/2:]


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
                    all_blocks.append([os.path.join(self.root[3:],name,'base'+'.png'),(os.path.join(self.root[3:],name,types[i]+'.png'))])
        random.shuffle(all_blocks)
        runs[0] = runs[0]+ all_blocks[:len(all_blocks)/2]
        runs[1] = runs[1]+ all_blocks[len(all_blocks)/2:]

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
                    names1.append(os.path.join(self.root[3:],file_name))
                    names2.append(os.path.join(self.second_root[3:],file_name))
                all_blocks.append(names1)
                all_blocks.append(names2)
        random.shuffle(all_blocks)
        return all_blocks


def generateMVPARuns():
    global z2, runs, run, i, index, catch_trial, flat_run, word, word2, word3, loc, file, header, wr
    z2 = PWBlocks(os.path.join('..', 'stimuli', 'Z2'), os.path.join('..', 'stimuli', 'Z3'), 4)
    runs = [[], []]
    z2.splitToRuns(runs)
    catch_trials = os.listdir(os.path.join('..', 'stimuli', 'Catch'))
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
            print index
            run.insert(index, catch_block)
    for i in range(len(runs)):
        file = open('exp1-run' + str(i + 1) + '.csv', 'wb')
        header = ['stim1', 'stim2', 'stim3', 'stim4']
        wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(header)
        wr.writerows(runs[i])
        print runs[i]


def generateLocalizerRun():
    global loc, run, file, header, wr
    loc = LocalizerBlocks(os.path.join('..', 'stimuli', 'FF'), os.path.join('..', 'stimuli', 'W'), 12)
    run = loc.getRun()
    file = open('loc.csv', 'wb')
    header = ['stim1', 'stim2', 'stim3', 'stim4', 'stim5', 'stim6', 'stim7', 'stim8', 'stim9', 'stim10', 'stim11',
              'stim12']
    wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(header)
    wr.writerows(run)

def generateTriplets():
    runs = [[], []]
    t = Triplets(os.path.join('..','stimuli','Triplets'))
    t.splitToRuns(runs)
    catch_trials = os.listdir(os.path.join('..', 'stimuli', 'Catch'))
    catch_trials = map(lambda file: os.path.join('stimuli', 'Catch',file),catch_trials)
    random.shuffle(catch_trials)
    for run in runs:
        random.shuffle(run)
        for i in range(len(run) / 14):
            index = (14 * (i + 1)) - random.randrange(10) + i
            flat_run = sum(run[:index], [])
            word = flat_run[random.randrange(len(flat_run))]
            catch_block = [word]
            catch_block.insert(random.randrange(2),catch_trials[i])
            print index
            run.insert(index, catch_block)
    for i in range(len(runs)):
        file = open('exp2-run' + str(i + 1) + '.csv', 'wb')
        header = ['stim1', 'stim2']
        wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(header)
        wr.writerows(runs[i])
        print runs[i]



print os.path.dirname(__file__)
generateTriplets()
generateMVPARuns()
generateLocalizerRun()
# t = Triplets(os.path.join('..','stimuli','Triplets'))
# t.splitToRuns(runs)
