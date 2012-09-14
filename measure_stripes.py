#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./measure_stripes.py
#
# (c) 2012 Nora Umbach <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: (1) Measure luminance of monitor:
#               (1.1) horizontal stripes
#               (1.2) vertical stripes
#
# input: --
# output: --
#
# created 2012-09-14 NU
# last mod 2012-09-14 NU

import sys
sys.path.append("../achrolabutils")

from achrolab.eyeone.eyeone import EyeOne
from monitor import eizoGS320

from stimuliclass import SquareWave

eyeone = EyeOne()

mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
        screen=1, colorSpace="rgb255", allowGUI=False)

eyeone.calibrate()

###### (1) Measure luminance of monitor ######

SquareWave(usingeizo=True, measuring=True, calibrate=False, prefix="",
        frequency=5)

