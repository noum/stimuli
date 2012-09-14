#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./example_singrating.py
#
# (c) 2012 Nora Umbach <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: Test for frame dropping
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

from stimuliclass import PatchBrightnessTest

patch = PatchBrightnessTest(usingeizo=True, measuring=False, calibrate=False,
        prefix="")

patch.run()

