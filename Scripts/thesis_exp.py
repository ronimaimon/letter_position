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
        types = ['same','subs','trans']
        for root, dirs, files in os.walk(self.root, topdown=False):
            for name in dirs:
                random.shuffle(types)
                path = os.path.join(root, name)
                for i in range(len(types)):
                    runs[i].append([os.path.join(self.root[3:],name,'base'+'.bmp'),(os.path.join(self.root[3:],name,types[i]+'.bmp')),'',''])

def generateMVPARuns():
    global z2, runs, run, i, index, catch_trial, flat_run, word, word2, word3, loc, file, header, wr
    z2 = PWBlocks(os.path.join('..', 'stimuli', 'Z2'), os.path.join('..', 'stimuli', 'Z3'), 4)
    runs = [[], []]
    z2.splitToRuns(runs)
    for run in runs:
        random.shuffle(run)
        for i in range(len(run) / 5):
            index = (5 * (i + 1)) - random.randrange(3) + i
            catch_trial = []
            flat_run = sum(run[:index], [])
            word = flat_run[random.randrange(len(flat_run))]
            word2 = flat_run[random.randrange(len(flat_run))]
            word3 = flat_run[random.randrange(len(flat_run))]
            loc = random.randrange(3)
            if (loc == 0):
                catch_trial = [word, word, word2, word3]
            elif (loc == 1):
                catch_trial = [word2, word, word, word3]
            else:
                catch_trial = [word2, word3, word, word]
            print index
            run.insert(index, catch_trial)
    for i in range(len(runs)):
        file = open('exp1-run' + str(i + 1) + '.csv', 'wb')
        header = ['stim1', 'stim2', 'stim3', 'stim4']
        wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        wr.writerow(header)
        wr.writerows(runs[i])
        print runs[i]

print os.path.dirname(__file__)
generateMVPARuns()
t = Triplets(os.path.join('..','stimuli','Triplets'))
t.splitToRuns(runs)
