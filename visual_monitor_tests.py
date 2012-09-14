#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./visual_monitor_tests.py
#
# (c) 2012 Nora Umbach <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) Measure luminance of monitor with horizontal and vertical
#              stripes
#
# input: --
# output: --
#
# created 2012-09-14 NU
# last mod 2012-09-14 NU

import sys
sys.path.append("../achrolabutils")

from psychopy import visual

from achrolab.eyeone.eyeone import EyeOne
from monitor import eizoGS320

from stimuliclass import Lines

eyeone = EyeOne()

mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
        screen=1, colorSpace="rgb255", allowGUI=False)

#eyeone.calibrate()

###### (1) Measure luminance of monitor with h- and v-stripes ######

lines = Lines(usingeizo=True, measuring=True, calibrate=True,
        prefix="../achrolabutils/calibdata/measurements/lines_linewidth8_box",
        linewidth=8, monitorsize=[2048, 1536], lowgray=0, highgray=1023)

lines.run()

