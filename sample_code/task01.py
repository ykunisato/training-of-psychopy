# %%

# -*- coding: utf-8 -*-
from psychopy import visual, core

try:
    # 画面の準備
    myWin = visual.Window (fullscr=True, monitor= 'Default', allowGUI=False, units='norm', color= (0,0,0))
    # 文字刺激の準備
    myText = visual.TextStim(myWin,text = 'Hello, Python!',color = (-1,-1,-1))
    # 文字刺激を画面に描く
    myText.draw()
    # 画面を提示
    myWin.flip()
    # 3秒待つ
    core.wait(3)
except TypeError as e:
    print(e)


# %%
