#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./example.py
#
# (c) 2012 Nora Umbach <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Do visual tests for monitor:
#          (1) Measure luminance of monitor: up, down, random
#
# input: --
# output: --
#
# created 2012-09-13 NU
# last mod 2012-09-13 NU

import sys
sys.path.append("../achrolabutils")

from achrolab.eyeone.eyeone import EyeOne
from achrolab.calibmonitor import CalibMonitor
from psychopy import visual
from monitor import eizoGS320
from ctypes import c_float

eyeone = EyeOne()

mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
        screen=1, colorSpace="rgb255", allowGUI=False)

mon = CalibMonitor(eyeone, mywin)

###### (1) Measure luminance of monitor: up, down, random ######

mon.startMeasurement()
mon.measurePatchStimColor(eizoGS320.encode_color(range(1024), range(1024)))


