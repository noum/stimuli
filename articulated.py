#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./articulated.py
#
# (c) 2012 James McMurray, Konstantin Sering, Nora Umbach
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: produce articulated stimuli
#
# input: --
# output: stimulilistac_*.txt
#         stimulilistnc_*.txt
#
# created
# last mod 2012-10-23 14:49 KS

"""
Produce articulated stimuli for experiments. Produces stimuli both with and
without articulated (transparent) infields. Modify the seed variable to change
whether the backgrounds are random or not = for non-random use a constant, for
random use the time plus a random number.
"""

import sys
sys.path.append("../achrolabutils")

from stimuliclass import Mondrian
import numpy as np
import Image
import time
from monitor import eizoGS320

MONITORSIZE = [2048, 1536]
BGGRAY = 621
SEPARATION = 40
INFIELDSIZE = 80
SURROUNDSIZE = 454
MONDRIANLENGTH = 40

STIMULILIST = [(376, 456), (396, 476), (416, 496), (436, 516), (456, 536),
               (436, 476), (396, 516)]

if __name__ == '__main__':
    timeset = time.strftime("%Y%m%d_%H%M", time.localtime())
    fileoutac = open("stimulilistac"+str(timeset)+".txt", "w")
    fileoutnc = open("stimulilistnc"+str(timeset)+".txt", "w")
    for left_stim in STIMULILIST:
        for right_stim in STIMULILIST:
            leftweightsvar = 10
            leftweightsmean = left_stim[1]
            rightweightsvar = 10
            rightweightsmean = right_stim[1]

            leftpatchgray = left_stim[0]
            rightpatchgray = right_stim[0]

            leftgrayminus = left_stim[1]-left_stim[0]
            rightgrayminus = right_stim[1]-right_stim[0]

            seedleft = 1
            seedright = 1

            leftweights = []
            for i in range(1023):
                leftweights.append(((1.0/(leftweightsvar * np.sqrt(2*np.pi))) * np.exp(-0.5*(((i-leftweightsmean)/leftweightsvar)**2))))

            rightweights = []
            for i in range(1023):
                rightweights.append(((1.0/(rightweightsvar * np.sqrt(2*np.pi))) * np.exp(-0.5*(((i-rightweightsmean)/rightweightsvar)**2))))


            rightweights = rightweights/sum(rightweights)
            leftweights = leftweights/sum(leftweights)

            bigarray = np.ones((MONITORSIZE[1], MONITORSIZE[0]))
            bigarray = BGGRAY*bigarray

            #Draw Mondrian surrounds
            mymondleft = Mondrian(usingeizo=False, imagesize=[SURROUNDSIZE,
                                                              SURROUNDSIZE],
                                  meanlength=MONDRIANLENGTH, encode=False,
                                  weights=leftweights, saveimage=False,
                                  seed=seedleft)

            bigarray[(MONITORSIZE[1]/2.0)-SURROUNDSIZE/2.0:
                     (MONITORSIZE[1]/2.0)+SURROUNDSIZE/2.0,
                     (MONITORSIZE[0]/2.0)-SURROUNDSIZE-SEPARATION/2.0:
                     (MONITORSIZE[0]/2.0)-SEPARATION/2.0] = mymondleft.mondrianarray

            mymondright = Mondrian(usingeizo=False, imagesize=[SURROUNDSIZE,
                                                               SURROUNDSIZE],
                                   meanlength=MONDRIANLENGTH, encode=False,
                                   weights=rightweights, saveimage=False,
                                   seed=seedright)

            bigarray[(MONITORSIZE[1]/2.0)-SURROUNDSIZE/2.0:
                     (MONITORSIZE[1]/2.0)+SURROUNDSIZE/2.0,
                     (MONITORSIZE[0]/2.0)+SEPARATION/2.0:
                     (MONITORSIZE[0]/2.0)+SURROUNDSIZE+SEPARATION/2.0] = mymondright.mondrianarray

            #Overlay transparent insets
            bigarray[(MONITORSIZE[1]/2.0)-(INFIELDSIZE/2.0):
                     (MONITORSIZE[1]/2.0)+(INFIELDSIZE/2.0),
                     (MONITORSIZE[0]/2.0)-(SURROUNDSIZE/2.0)-(SEPARATION/2.0)-(INFIELDSIZE/2.0):
                     (MONITORSIZE[0]/2.0)-(SEPARATION/2.0)-(SURROUNDSIZE/2.0)+(INFIELDSIZE/2.0)] -= leftgrayminus

            bigarray[(MONITORSIZE[1]/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[1]/2.0)+(INFIELDSIZE/2.0),(MONITORSIZE[0]/2.0)+(SEPARATION/2.0)+(SURROUNDSIZE/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[0]/2.0)+(SURROUNDSIZE/2.0)+(SEPARATION/2.0)+(INFIELDSIZE/2.0)] -= leftgrayminus

            bigarray[bigarray>1023] = 1023
            bigarray[bigarray<0] = 0

            # (N, M) = np.shape(bigarray)
            # newarray = np.zeros((N, M, 3), dtype=np.uint8)
            # newarray[:,:,0] = np.uint8(bigarray[:,:]/4)
            # newarray[:,:,1] = np.uint8(bigarray[:,:]/4)
            # newarray[:,:,2] = np.uint8(bigarray[:,:]/4)
            newarray = eizoGS320.encode_np_array(bigarray)
            pil_im = Image.fromarray(newarray)
            pngfile = "stimuli/ac"+str(leftweightsmean)+"_"+str(leftweightsvar)+"_"+str(leftgrayminus)+"_"+str(rightweightsmean)+"_"+str(rightweightsvar)+"_"+str(rightgrayminus)+"_"+str(BGGRAY)+"_"+str(seedleft)+"_"+str(seedright)+".png"

            fileoutac.write("trial(['"+str(pngfile)+"', "+str(leftweightsmean)+","+str(leftweightsvar)+","+str(leftgrayminus)+","+str(rightweightsmean)+","+str(rightweightsvar)+","+str(rightgrayminus)+","+str(BGGRAY)+","+str(seedleft)+","+str(seedright)+"], 'left', outputFile)\n")
            pil_im.save(pngfile)

            #do NC image
            bigarray[(MONITORSIZE[1]/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[1]/2.0)+(INFIELDSIZE/2.0),(MONITORSIZE[0]/2.0)-(SURROUNDSIZE/2.0)-(SEPARATION/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[0]/2.0)-(SEPARATION/2.0)-(SURROUNDSIZE/2.0)+(INFIELDSIZE/2.0)] = leftpatchgray
            bigarray[(MONITORSIZE[1]/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[1]/2.0)+(INFIELDSIZE/2.0),(MONITORSIZE[0]/2.0)+(SEPARATION/2.0)+(SURROUNDSIZE/2.0)-(INFIELDSIZE/2.0):(MONITORSIZE[0]/2.0)+(SURROUNDSIZE/2.0)+(SEPARATION/2.0)+(INFIELDSIZE/2.0)] = rightpatchgray

            bigarray[bigarray>1023] = 1023
            bigarray[bigarray<0] = 0

            # (N, M) = np.shape(bigarray)
            # newarray = np.zeros((N, M, 3), dtype=np.uint8)
            # newarray[:,:,0] = np.uint8(bigarray[:,:]/4)
            # newarray[:,:,1] = np.uint8(bigarray[:,:]/4)
            # newarray[:,:,2] = np.uint8(bigarray[:,:]/4)
            newarray = eizoGS320.encode_np_array(bigarray)
            pil_im  =  Image.fromarray(newarray)
            pngfile = "stimuli/nc"+str(leftweightsmean)+"_"+str(leftweightsvar)+"_"+str(leftgrayminus)+"_"+str(rightweightsmean)+"_"+str(rightweightsvar)+"_"+str(rightgrayminus)+"_"+str(BGGRAY)+"_"+str(seedleft)+"_"+str(seedright)+".png"

            fileoutnc.write("trial(['"+str(pngfile)+"', "+str(leftweightsmean)+","+str(leftweightsvar)+","+str(leftgrayminus)+","+str(rightweightsmean)+","+str(rightweightsvar)+","+str(rightgrayminus)+","+str(BGGRAY)+","+str(seedleft)+","+str(seedright)+"], 'left', outputFile)\n")
            pil_im.save(pngfile)

    fileoutac.close()
    fileoutnc.close()
