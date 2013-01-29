#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# stimMidgrey.py
#
# (c) 2012 Dominik Wabersich <dominik.wabersich [aet] gmail.com>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2012-05-21
# last mod 2013-01-29 11:21 KS
#
"""
This module contains a class to create and present an infield surround
stimulus with psychopy.

.. warning::
    This module works only for the EIZO GS320.

"""

from psychopy import visual
import eizoGS320

class Stimulus(object):
    """
    This class is for the EIZO GS320.

    """

    def __init__(self, win, grey_left, grey_mid, grey_right, grey_background,
            name=None):

        """
        Paramters
        ---------

            win: psychopy.Window instance
            grey_left: 0..1023
                grey value for left infield
            grey_right: 0..1023
                grey value for left surround
            grey_mid: 0..1023
                grey value for right infield
            grey_background: 0..1023
                grey value of background (must be the same as the
                background of the window)

        """
        self.win = win
        self.grey_left = grey_left
        self.grey_mid = grey_mid
        self.grey_right = grey_right
        self.grey_background = grey_background
        self.name = name

        width_mon_half = 512.
        size_stim  = 99. # 1 deg
        size_between  = 50. # 0.5 deg
        x_pos_left = width_mon_half - (size_stim/2. + size_between +
                size_stim/2.)
        x_pos_right = -width_mon_half + (size_stim/2. + size_between +
                size_stim/2.)
        x_pos_mid_left = width_mon_half
        x_pos_mid_right = -width_mon_half
        y_pos = 0.

        self.stim_left = visual.GratingStim(self.win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_stim, colorSpace="rgb255",
                color=eizoGS320.encode_color(grey_background, grey_left))
        self.stim_right = visual.GratingStim(self.win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_stim, colorSpace="rgb255",
                color=eizoGS320.encode_color(grey_right, grey_background))
        self.stim_mid_l = visual.GratingStim(self.win, tex=None, units="pix",
                pos=(x_pos_mid_left, y_pos), size=size_stim, colorSpace="rgb255",
                color=eizoGS320.encode_color(grey_background, grey_mid))
        self.stim_mid_r = visual.GratingStim(self.win, tex=None, units="pix",
                pos=(x_pos_mid_right, y_pos), size=size_stim, colorSpace="rgb255",
                color=eizoGS320.encode_color(grey_mid, grey_background))

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.stim_left.draw(win)
        self.stim_right.draw(win)
        self.stim_mid_l.draw(win)
        self.stim_mid_r.draw(win)


if __name__ == '__main__':
    from psychopy import event
    mywin = visual.Window([1024,1536], monitor='mymon', color=(155,155,17),
            screen=1, colorSpace="rgb255", allowGUI=False,)
    teststim = Stimulus(mywin, 500,700,1023,621)
    teststim.draw()
    mywin.flip()
    event.waitKeys(keyList='escape')

