'''
#########################################################################

                            TicTacToe:

#########################################################################

Description: - This tool allows you to play tic-tac-toe on maya(python 2.7);
             - TicTacToe ui functions.

#########################################################################

 Author: Laura Siviero
         laura.seav@gmail.com
 
 License: MIT https://github.com/laurasiviero/TicTacToe/blob/main/LICENSE
 
 Date 2021.05.05

#########################################################################
'''


import sys
import maya.cmds as cmds


import ttt_enemy_functions as ttt


def tic_tac_toe_ui(USERPATH):
    PATH_ICONS = USERPATH + "\\tic_tac_toe_icons\\"
    sys.path.append(USERPATH)
    sys.path.append(PATH_ICONS)
    print("directories have been updated")

    ui_title = "tic tac_toe"
    main_color = [0.492, 0.980, 0.570]
    secondary_color = [0.953, 0.588, 0.4]

    window = cmds.window(ui_title, title="Tic Tac Toe",
                         backgroundColor=main_color,
                         sizeable=True,
                         resizeToFitChildren=True)

    # DELETE if it already exists:
    if cmds.window(ui_title, exists=True):
        cmds.deleteUI(ui_title)


    ###############################################################
    ##########################   HEADER   #########################
    ###############################################################
    cmds.columnLayout(rowSpacing=5)

    cmds.formLayout("ttt_form_count", backgroundColor=main_color,
                    numberOfDivisions=100)

    ttt_count_user = cmds.image("ttt_count_user",
                                image=PATH_ICONS + "ttt_number\\" + 'ttt_0.png')

    ttt_count_ia = cmds.image("ttt_count_ia",
                              image=PATH_ICONS + "ttt_number\\" + 'ttt_0.png')
    cmds.image("ttt_bg", image=PATH_ICONS + 'ttt_banner.png')

    cmds.formLayout("ttt_form_count", edit=True,
                    attachForm=[(ttt_count_user, 'left', 70), (ttt_count_user, 'top', 88),
                                (ttt_count_ia, 'left', 385), (ttt_count_ia, 'top', 88)])
    cmds.setParent("..")


    ###############################################################
    ####################   TIC TAC TOE GRID    ####################
    ###############################################################
    cmds.formLayout("ttt_formlayout", backgroundColor=main_color,
                    numberOfDivisions=100)
    cmds.image("ttt_bg", image=PATH_ICONS + 'ttt_grid.png')

    ttt_button01 = cmds.iconTextButton("ttt_button01", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button01', USERPATH)")
    ttt_button02 = cmds.iconTextButton("ttt_button02", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button02', USERPATH)")
    ttt_button03 = cmds.iconTextButton("ttt_button03", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button03', USERPATH)")
    ttt_button04 = cmds.iconTextButton("ttt_button04", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button04', USERPATH)")
    ttt_button05 = cmds.iconTextButton("ttt_button05", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button05', USERPATH)")
    ttt_button06 = cmds.iconTextButton("ttt_button06", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button06', USERPATH)")
    ttt_button07 = cmds.iconTextButton("ttt_button07", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button07', USERPATH)")
    ttt_button08 = cmds.iconTextButton("ttt_button08", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button08', USERPATH)")
    ttt_button09 = cmds.iconTextButton("ttt_button09", style='iconOnly',
                                       image=PATH_ICONS + 'ttt_idle.png',
                                       command="ttt.set_turn('ttt_button09', USERPATH)")

    cmds.formLayout("ttt_formlayout", edit=True,
                    attachForm=[(ttt_button01, 'left', 25), (ttt_button01, 'top', 25),
                                (ttt_button02, 'left',180), (ttt_button02, 'top', 25),
                                (ttt_button03, 'left',335), (ttt_button03, 'top', 25),
                                (ttt_button04, 'left',25), (ttt_button04, 'top', 180),
                                (ttt_button05, 'left',180), (ttt_button05, 'top', 180),
                                (ttt_button06, 'left',335), (ttt_button06, 'top', 180),
                                (ttt_button07, 'left',25), (ttt_button07, 'top', 335),
                                (ttt_button08, 'left',180), (ttt_button08, 'top', 335),
                                (ttt_button09, 'left', 335), (ttt_button09, 'top', 335)])
    cmds.setParent("..")

    ###############################################################
    #########################   BUTTONS    ########################
    ###############################################################
    cmds.rowLayout(numberOfColumns=2)
    ttt_button_match = cmds.iconTextButton("ttt_button_match", style='iconOnly',
                                           image=PATH_ICONS + 'ttt_restart_match.png',
                                           command="ttt.restart_match(USERPATH)")

    ttt_button_game = cmds.iconTextButton("ttt_button_game", style='iconOnly',
                                          image=PATH_ICONS + 'ttt_new_game.png',
                                          command="ttt.restart_game(USERPATH)")
    cmds.showWindow()
