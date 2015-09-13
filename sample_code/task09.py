# -*- coding: utf-8 -*-
from psychopy import visual, core, event, gui, data, misc
import numpy, os, random, time, csv

try:
    #　画面の準備（灰色の画面、マウスはallowGUI=Falseで表示されないようにしている）
    myWin = visual.Window (fullscr=True, monitor= 'Default', allowGUI=False, units='norm', color= (0,0,0))
    # 文字（漢字)のリスト
    kanjiList = [u'赤',u'黄',u'青',u'赤',u'黄',u'青',u'赤',u'黄',u'青']
    # 色のリスト(visual.TextStimのcolorにいれる)
    colorList = [(1,-1,-1),(1,-1,-1),(1,-1,-1),(1,1,-1),(1,1,-1),(1,1,-1),(-1,-1,1),(-1,-1,1),(-1,-1,1)]
    # ランダムに提示するためのリスト
    randomList = range(9)
    # 内側のforループを2回繰り返すためのfor文
    for m in range(2):
        # randomListをシャッフルする。
        numpy.random.shuffle(randomList)
        # 内側のfor文（range(9)で0~8のリストを作成し、前から順番でiにいれる）
        for i in range(9):
            #　kanjiListのrandomList[i]番目（kanjiList[randomList[i]]）を、
            # colorListのrandomList[i]番目の色(colorList[randomList[i]])で提示する。
            myText = visual.TextStim(myWin,text = kanjiList[randomList[i]],pos=(0,0),color = colorList[randomList[i]],height=0.2)
            myText.draw()
            myWin.flip()
            core.wait(1)
            #　中視点(+)を1秒提示する。
            myText = visual.TextStim(myWin,text = '+',pos=(0,0),color = (-1,-1,-1),height=0.2)
            myText.draw()
            myWin.flip()
            core.wait(1)
except TypeError, e:
    print e
