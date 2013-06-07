#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# stimulus.py
#
# New version for exp III with transparent layer
#
# (c) 2012 Konstantin Sering <konstantin.sering [aet] gmail.com>
# (c) 2013 Nora Umbach <nora.umbach [aet] web.de>
# GPL 3.0+ or (cc) by-sa (http://creativecommons.org/licenses/by-sa/3.0/)
#
# created 2013-01-04 NU
# last mod 2013-01-29 11:36 KS

"""This module contains classes to create and present two infield surround
stimulus configurations with and without transparent layers with psychopy
on the eizoGS320 monitor.

ATTENTION: left refers to the left on the eizoGS320 -- but this is right in
terms of defining that stimulus."""

from psychopy import visual
import eizoGS320

class InfieldSurround(object):
    def __init__(self, win, inf_left, sur_left, inf_right, sur_right,
            background):
        """
        :Paramters:

            win: psychopy.Window instance
            inf_left: 0..1023
                grey value for left infield
            sur_left: 0..1023
                grey value for left surround
            inf_right: 0..1023
                grey value for right infield
            sur_right: 0..1023
                grey value for right surround
            background: 0..1023
                grey value of background (must be the same as the
                background of the window)

        """
        self.win = win

        width_mon_half = 512
        size_inf  = 80
        size_sur  = 454
        size_diff = 40
        x_pos_right = size_diff/2.+size_sur/2.-width_mon_half
        x_pos_left = width_mon_half-size_diff/2.-size_sur/2.
        y_pos = 0

        self.sur_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(sur_right, background))
        self.sur_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, sur_left))
        self.inf_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_inf, colorSpace="rgb255",
                color=eizoGS320.encode_color(inf_right, background))
        self.inf_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_inf, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, inf_left))

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.sur_left.draw(win)
        self.sur_right.draw(win)
        self.inf_left.draw(win)
        self.inf_right.draw(win)

class InfieldSurroundTrans(object):
    def __init__(self, win, inf_left, sur_left, trans_left,
             inf_right, sur_right, trans_right, background,
             angle_left=20, angle_right=-20, opacity_left=0.5,
             opacity_right=0.5):
        """
        :Paramters:

            win: psychopy.Window instance
            inf_left: 0..1023
                grey value for left infield
            sur_left: 0..1023
                grey value for left surround
            trans_left: 0..1023
                grey value for left transparent layer
            angle_left: 0..360 or negative
                angle for rotation of transparent layer
            opacity_left: 0..1
                0 = completely transparent, 1 = opaque
            inf_right: 0..1023
                grey value for right infield
            sur_right: 0..1023
                grey value for right surround
            trans_right: 0..1023
                grey value for right transparent layer
            angle_right: 0..360 or negative
                angle for rotation of transparent layer
            opacity_right: 0..1
                0 = completely transparent, 1 = opaque
            background: 0..1023
                grey value of background (must be the same as the
                background of the window)

        """
        self.win = win

        width_mon_half = 512
        size_inf  = 80
        size_sur  = 390
        size_diff = 120
        x_pos_right = size_diff/2.+size_sur/2.-width_mon_half
        x_pos_left = width_mon_half-size_diff/2.-size_sur/2.
        y_pos = 0

        self.sur_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(sur_right, background))
        self.sur_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_sur,
                colorSpace="rgb255",
                color=eizoGS320.encode_color(background, sur_left))
        self.inf_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_inf,
                colorSpace="rgb255",
                color=eizoGS320.encode_color(inf_right, background))
        self.inf_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_inf, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, inf_left))
        self.trans_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(trans_right, background),
                ori=angle_right, opacity=opacity_right)
        self.trans_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, trans_left),
                ori=angle_left, opacity=opacity_left)

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.sur_left.draw(win)
        self.sur_right.draw(win)
        self.inf_left.draw(win)
        self.inf_right.draw(win)
        self.trans_left.draw(win)
        self.trans_right.draw(win)

class InfieldSurroundTransBar(object):
    def __init__(self, win, inf_left, sur_left, trans_left, inf_right,
            sur_right, trans_right, background, reference, angle_left=20,
            angle_right=-20, opacity_left=0.5, opacity_right=0.5):
        """
        :Paramters:

            win: psychopy.Window instance
            inf_left: 0..1023
                grey value for left infield
            sur_left: 0..1023
                grey value for left surround
            trans_left: 0..1023
                grey value for left transparent layer
            angle_left: 0..360 or negative
                angle for rotation of transparent layer
            opacity_left: 0..1
                0 = completely transparent, 1 = opaque
            inf_right: 0..1023
                grey value for right infield
            sur_right: 0..1023
                grey value for right surround
            trans_right: 0..1023
                grey value for right transparent layer
            background: 0..1023
                grey value for background
            reference: 0..1023
                grey value for reference bar
            angle_right: 0..360 or negative
                angle for rotation of transparent layer
            opacity_right: 0..1
                0 = completely transparent, 1 = opaque
            background: 0..1023
                grey value of background (must be the same as the
                background of the window)

        """
        self.win = win

        width_mon_half = 512
        size_inf  = 80
        size_sur  = 390
        size_diff = 90
        size_trans = (300, 500)
        x_pos_right = size_diff/2.+size_sur/2.-width_mon_half
        x_pos_left = width_mon_half-size_diff/2.-size_sur/2.
        y_pos = 0

        self.sur_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_sur, colorSpace="rgb255",
                color=eizoGS320.encode_color(sur_right, background))
        self.sur_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_sur,
                colorSpace="rgb255",
                color=eizoGS320.encode_color(background, sur_left))
        self.inf_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_inf,
                colorSpace="rgb255",
                color=eizoGS320.encode_color(inf_right, background))
        self.inf_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_inf, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, inf_left))
        self.trans_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right, y_pos), size=size_trans, colorSpace="rgb255",
                color=eizoGS320.encode_color(trans_right, background),
                ori=angle_right, opacity=opacity_right)
        self.trans_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left, y_pos), size=size_trans, colorSpace="rgb255",
                color=eizoGS320.encode_color(background, trans_left),
                ori=angle_left, opacity=opacity_left)
        self.ref_left = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_left+size_diff/2., y_pos+390/2.+80),
                size=(size_sur+size_diff, 100), colorSpace="rgb255",
                color=eizoGS320.encode_color(background, reference))
        self.ref_right = visual.GratingStim(win, tex=None, units="pix",
                pos=(x_pos_right-size_diff/2., y_pos+390/2.+80),
                size=(size_sur+size_diff, 100), colorSpace="rgb255",
                color=eizoGS320.encode_color(reference, background))

    def draw(self, win=None):
        """Draw the stimulus in its relevant window. You must call this
        method after every win.flip().
        """
        if win==None: win=self.win
        self.sur_left.draw(win)
        self.sur_right.draw(win)
        self.inf_left.draw(win)
        self.inf_right.draw(win)
        self.ref_left.draw(win)
        self.ref_right.draw(win)
        self.trans_left.draw(win)
        self.trans_right.draw(win)


