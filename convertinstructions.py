#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# ./convertinstructions.py
#
# (c) 2012 James McMurray, Konstantin Sering, Nora Umbach
# <colorlab[at]psycho.uni-tuebingen.de>
#
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# content: convert instructions to eizoGS320 format
#
# input: --
# output: stimulilistac_*.txt
#         stimulilistnc_*.txt
#
# created
# last mod 2012-11-20 17:09 KS

"""
This script converts a bunch of png files into the corresponding png files,
that have the format to be shown on the eizoGS320.

"""

import eizoGS320

filenames=["ende.png", "ende_training_left.png", "ende_training_right.png",
           "instructions1.png", "instructions2_left.png",
           "instructions2_right.png", "instructions3.png", "new_block.png"]

for filename in filenames:
   eizoGS320.convert_to_eizo_picture("instructions/"+filename,
                                     "instructions/conv"+str(filename)+".png")
