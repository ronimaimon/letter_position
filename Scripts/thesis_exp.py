from psychopy.visual import SimpleImageStim
import os, random, cPickle
import csv
os.chdir(os.path.dirname(__file__))

NO_OF_RUNS = 3
class PWBlocks:
    def __init__(self, path,block_len):
        self.block_len = block_len
        self.root = path

    def splitToRuns(self,runs=[]):
        random.shuffle(runs)
        for root, dirs, files in os.walk(self.root, topdown=False):
            random.shuffle(files)
            for j in range(len(files)/self.block_len):
                names = []
                for i in range(self.block_len):
                    names.append(os.path.join(self.root[3:],files.pop()))
                runs[j%len(runs)].append(names)


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


t = Triplets(os.path.join('..','stimuli','Triplets'))
z2 = PWBlocks(os.path.join('..','stimuli','Z2'),4)
z3 = PWBlocks(os.path.join('..','stimuli','Z3'),4)
runs = [[],[],[]]
t.splitToRuns(runs)
z2.splitToRuns(runs)
z3.splitToRuns(runs)
for run in runs:
    random.shuffle(run)
    for i in range(len(run)/5):
        word = ''
        while word=='':
            flat_run =  sum(run,[])
            index = random.randrange(len(flat_run))
            word = flat_run[index]
        index = (5*(i+1))-random.randrange(3)+i
        print index
        run.insert(index,[word,'','',''])
        # run.insert((5*(i+1))-random.randrange(3)+2,[word,None,None,None])
for i in range(len(runs)):
    file = open('run'+str(i+1)+'.csv', 'wb')
    header = ['stim1','stim2','stim3','stim4']
    wr = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
    wr.writerow(header)
    wr.writerows(runs[i])
    print runs[i]
    # win=visual.Window(fullscr=True)
    # im1 = SimpleImageStim(win, image=os.path.join('..','stimuli', '1.bmp'), units='', pos=(0.0, 0.0), flipHoriz=False, flipVert=False, name='PW1',
    #                 autoLog=True)
    # im1.draw()
    # win.flip()

    # core.wait(8.0)