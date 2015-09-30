## load libraries
import pickle
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import random
from libpysegfit import PySegFit



## configuration
inputDir = '/home/lin/Documents/Thesis/exec/phaseAndPredictionPerformance/tdb/'

firstNDay = 180

## load data
videoID_viewcount = pickle.load(open( inputDir + 'videoID_viewcount_735.pickle' ))

## gui

videoID_all = videoID_viewcount.keys()
# last run : set(['gmUBLhS2YX4', 'VE02FUOwMmU', 'rJu_NbEr2sY', '1BF7TrKLC1I', 'HCGtKrx1q5U', 'e7G1s9G8-H8', 'D-Dqz9ziRWY', 'MPdLtRexwqw', 'Rc0tU9JhMmU', 'n7m-9s5P3kE', 'ONr0bc2Roxw', 'XKLDUWsx2Rs', 'zqFhS7GswpM', 'aFyazIQsg7c', '0GJzQFGQZF0'])
# videoID_selected = set()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)
t = range(firstNDay)
videoID = random.sample( videoID_all, 1 )[0]
s = videoID_viewcount[videoID][0:firstNDay]
l, = plt.plot(t, s, '.')

segFitObj = PySegFit()
segFitObj.set_smp(6.0)

class Index:
    ind = 0
    videoID = ''

    def next(self, event):

        ax.clear()
        
        # plot viewcount
        self.videoID = random.sample( videoID_all, 1 )[0]
        newViewcount = videoID_viewcount[self.videoID][0:firstNDay]
        ax.plot(newViewcount, '.')

        # plot segments
        vcRate = max(newViewcount)/100.0
        segInfo = segFitObj.segfit(newViewcount)
        segX = []
        segY = []
        
        for (si, ei, a, b, c, o) in segInfo:
            si -= 1
            ei -= 1
            segX = range(si, ei+1)
            segY = []
            
            for i in range(1, ei - si + 2):
                segY.append( (a*pow(i, b) + c)*vcRate )

            if o == 0:
                ax.plot(segX, segY, 'r')
            else:
                ax.plot(segX, list(reversed(segY)), 'r')
        
        
        plt.draw()

    def save(self, event):
        videoID_selected.add( self.videoID )
        print len(videoID_selected), videoID_selected
        
callback = Index()
axsave = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bsave = Button(axsave, 'Save')
bsave.on_clicked(callback.save)

plt.show()

## save to json

# format of json {index : data to plot}
index_data = {}

for idx, videoID in enumerate(videoID_selected):
    data = []

    # push viewcount
    viewcount = videoID_viewcount[videoID][0:firstNDay]
    data.append({
        'values' : [{'x': x, 'y': y} for x, y in enumerate(viewcount)],
        'key'    : 'viewcount',
        'color': '#3399FF'
    })

    # push segments    
    vcRate = max(viewcount)/100.0
    segInfo = segFitObj.segfit(viewcount)
    segX = []
    segY = []

    for segIdx, (si, ei, a, b, c, o) in enumerate(segInfo):
        si -= 1
        ei -= 1
        segX = range(si, ei+1)
        segY = []

        for i in range(1, ei - si + 2):
            segY.append( (a*pow(i, b) + c)*vcRate )

        if o != 0:
            segY = list(reversed(segY))

        data.append({
            'values' : [{'x': x, 'y': y} for x, y in zip(segX, segY)],
            'key'    : 'seg%d' % segIdx,
            'color'  : '#8B0000',
            'stroke-width': 5
        })
            

    index_data[idx] = {
        'videoID' : videoID,
        'data'    : data
    }


## dump file
json.dump(index_data, open('segResultData.json', 'w'))

