'''
#########################################################################

                            TicTacToe:

#########################################################################

Description: - This tool allows you to play tic-tac-toe on maya(python 2.7);
             - Functions and behaviour of the enemy;
             - Ui management (score and "new games" functions).

#########################################################################

 Author: Laura Siviero
         laura.seav@gmail.com
 
 License: MIT https://github.com/laurasiviero/TicTacToe/blob/main/LICENSE
 
 Date 2021.05.05

#########################################################################
'''



import sys
import maya.cmds as cmds
import random

###############################################################
####################   PROVIDE SYS PATHS   ####################
###############################################################


def get_paths_icons(USERPATH):
    PATH_ICONS = USERPATH + "\\tic_tac_toe_icons\\"

    sys.path.append(USERPATH)
    sys.path.append(PATH_ICONS)

    user_icon = PATH_ICONS + "ttt_cross.png"
    ia_icon = PATH_ICONS + "ttt_circle.png"
    idle_icon = PATH_ICONS + "ttt_idle.png"

    icons = [user_icon, ia_icon, idle_icon]

    return icons


###############################################################
####################   MAPPING GAMEFIELD   ####################
###############################################################

def map_weights(user_icon, ia_icon):
    weights = []
    buttons = ["ttt_button01", "ttt_button02", "ttt_button03",
               "ttt_button04", "ttt_button05", "ttt_button06",
               "ttt_button07", "ttt_button08", "ttt_button09"]

    for button in buttons:
        image_path = cmds.iconTextButton(button, query=True, image=True)

        if image_path == ia_icon:
            weights.append(3)
        elif image_path == user_icon:
            weights.append(10)
        else:
            weights.append(0)

    return weights, buttons


def search_for_victory(user_icon, ia_icon, idle_icon, criteria):

    if criteria == "victory":
        threshold = 6
    else:
        threshold = 20

    counter_move = ""

    weights, buttons = map_weights(user_icon, ia_icon)

    # Manage ROWS:
    # #############################################
    rows_start = [0, 3, 6]
    rows_end = [2 + 1, 5 + 1, 8 + 1]

    for index in range(0, len(rows_start)):
        sum_weights = sum(weights[rows_start[index]:rows_end[index]])
        if sum_weights == threshold:
            for index in range(rows_start[index], rows_end[index]):
                if weights[index] == 0:
                    cmds.iconTextButton(buttons[index], edit=True,
                                        image=ia_icon)
                    counter_move = "DONE"
                    return counter_move

    # Manage COLUMNS:
    # #############################################
    for index in range(0, 3):
        sum_column = weights[index] + weights[index + 3] + weights[index + 6]
        if sum_column == threshold:
            for button_index in [index, index + 3, index + 6]:
                if cmds.iconTextButton(buttons[button_index], query=True, image=True) == idle_icon:
                    cmds.iconTextButton(buttons[button_index], edit=True,
                                        image=ia_icon)
                    counter_move = "DONE"
                    return counter_move

    # Manage DIAGONALS:
    # #############################################
    sum_diagonal01 = weights[0] + weights[4] + weights[8]
    sum_diagonal02 = weights[2] + weights[4] + weights[6]

    if sum_diagonal01 == threshold:
        for index in [0, 4, 8]:
            if cmds.iconTextButton(buttons[index], query=True, image=True) == idle_icon:
                cmds.iconTextButton(buttons[index], edit=True,
                                    image=ia_icon)
                counter_move = "DONE"
                return counter_move

    elif sum_diagonal02 == threshold:
        for index in [2, 4, 6]:
            if cmds.iconTextButton(buttons[index], query=True, image=True) == idle_icon:
                cmds.iconTextButton(buttons[index], edit=True,
                                    image=ia_icon)
                counter_move = "DONE"
                return counter_move

    return (counter_move)


###############################################################
######################   RESTART GAME   #######################
###############################################################


def restart_match(USERPATH):
    user_icon, ia_icon, idle_icon = get_paths_icons(USERPATH)
    buttons = ["ttt_button01", "ttt_button02", "ttt_button03",
               "ttt_button04", "ttt_button05", "ttt_button06",
               "ttt_button07", "ttt_button08", "ttt_button09"]

    for button in buttons:
        cmds.iconTextButton(button, edit=True, image=idle_icon)


def restart_game(USERPATH):
    PATH_ICONS = USERPATH + "\\tic_tac_toe_icons\\"
    number_image_path = PATH_ICONS + "\\ttt_number\\ttt_0.png"
    restart_match(USERPATH)

    for image in ["ttt_count_user", "ttt_count_ia"]:
        cmds.image(image, edit=True, image=number_image_path)


###############################################################
#########################   END GAME   ########################
###############################################################

def pop_up_massage_win_game(winner):
    if winner == "user":
        message = "Congratulations, you won the Game!"
        icon = "information"

    elif winner == "ia":
        message = "Sorry you lost.\nDo you want to start a new game?"
        icon = "critical"

    cmds.confirmDialog(title="tic tac toe",
                       message=message,
                       messageAlign="center",
                       icon=icon,
                       button=["OK"],
                       defaultButton="OK",
                       cancelButton="OK")


def keep_track_score(winner):
    if winner == "user":
        score_image = "ttt_count_user"

    elif winner == "ia":
        score_image = "ttt_count_ia"
    else:
        return

    image_path = cmds.image(score_image, query=True, image=True)
    score = str(int(image_path[-5]) + 1)
    if score == "10":
        pop_up_massage_win_game(winner)
        score = "0"
        new_image_path = image_path[:-5] + score + ".png"
        cmds.image("ttt_count_user", edit=True, image=new_image_path)
        cmds.image("ttt_count_ia", edit=True, image=new_image_path)

    new_image_path = image_path[:-5] + score + ".png"
    cmds.image(score_image, edit=True, image=new_image_path)


def pop_up_message_win_match(winner, USERPATH):
    if winner == "user":
        message = "Congratulations, you won!"
        icon = "information"

    elif winner == "ia":
        message = "It was that close, but not close enough. \nDo you want a rematch?"
        icon = "critical"
    else:
        message = "It looks like a tie. \nDo you want a rematch?"
        icon = "question"

    cmds.confirmDialog(title="tic tac toe",
                       message=message,
                       messageAlign="center",
                       icon=icon,
                       backgroundColor = [0.121, 0.50, 0.31],
                       button=["OK"],
                       defaultButton="OK",
                       cancelButton="OK")
    restart_match(USERPATH)
    keep_track_score(winner)


def check_results(USERPATH):
    user_icon, ia_icon, idle_icon = get_paths_icons(USERPATH)
    weights, buttons = map_weights(user_icon, ia_icon)
    winner = ""

    for threshold in [30, 9]:
        # Search victory through rows:
        ##################################################
        rows_start = [0, 3, 6]
        rows_end = [2 + 1, 5 + 1, 8 + 1]

        for index in range(0, len(rows_start)):
            sum_rows = sum(weights[rows_start[index]:rows_end[index]])
            if sum_rows == threshold:
                winner = threshold
                break

        # Search victory through columns:
        #################################################

        for index in range(0, 3):
            sum_column = weights[index] + \
                weights[index + 3] + weights[index + 6]
            if sum_column == threshold:
                winner = threshold
                break

        # Manage DIAGONALS:
        # #############################################
        sum_diagonal01 = weights[0] + weights[4] + weights[8]
        sum_diagonal02 = weights[2] + weights[4] + weights[6]

        if sum_diagonal01 == threshold:
            winner = threshold
            break

        elif sum_diagonal02 == threshold:
            winner = threshold
            break

        # search for tie:
        tie_icons = []

        for button in buttons:
            icon = cmds.iconTextButton(button, query=True, image=True)
            if icon != idle_icon:
                tie_icons.append("NOT")

            if len(tie_icons) == 9:
                winner = "TIE"

    if winner:
        if winner == 30:
            pop_up_message_win_match("user", USERPATH)
        elif winner == 9:
            pop_up_message_win_match("ia", USERPATH)
        elif winner == "TIE":
            pop_up_message_win_match("TIE", USERPATH)

###############################################################
####################   COUNTER STRATEGY   #####################
###############################################################


def set_turn(button, USERPATH):
    user_icon, ia_icon, idle_icon = get_paths_icons(USERPATH)

    edge_buttons = ["ttt_button01", "ttt_button03",
                    "ttt_button07", "ttt_button09"]

    center_button = "ttt_button05"

    cross_buttons = ["ttt_button02", "ttt_button04",
                     "ttt_button06", "ttt_button08"]

    # USER TURN:
    # ################################################
    icon = cmds.iconTextButton(button, query=True, image=True)
    if icon == idle_icon:
        user_move = cmds.iconTextButton(button, edit=True, image=user_icon)

        # ENEMY MOVE:
        # ############################################
        # read game field
        for criteria in ["victory", "defeat"]:
            counter_move = search_for_victory(user_icon, ia_icon,
                                              idle_icon, criteria)
            if counter_move:
                check_results(USERPATH)
                return

        # counter move center:
        ###############################################
        if button == center_button:
            possibilities = ""
            counter_indexes = [1, 3, 7, 9]
            enemy_button = "ttt_button0" + str(random.choice(counter_indexes))
            counter_icon = cmds.iconTextButton(enemy_button,
                                               query=True, image=True)

            if counter_icon == idle_icon:
                cmds.iconTextButton(enemy_button, edit=True, image=ia_icon)

            else:
                for counter_index in counter_indexes:
                    enemy_button = "ttt_button0" + str(counter_index)
                    counter_icon = cmds.iconTextButton(enemy_button, query=True,
                                                       image=True)
                    if counter_icon == idle_icon:
                        cmds.iconTextButton(enemy_button,
                                            edit=True, image=ia_icon)
                        possibilities = "None"
                        break

            # what if counter move is not available
            # -------------------------------------
            if not possibilities:
                for counter_index in [2, 4, 6, 8]:
                    if counter_icon == idle_icon:
                        cmds.iconTextButton(enemy_button, edit=True,
                                            image=ia_icon)

        # counter move center edges:
        ###############################################
        elif button in cross_buttons:
            possibilities = ""

            if cmds.iconTextButton(center_button, query=True, image=True) == idle_icon:
                cmds.iconTextButton(center_button, edit=True,
                                    image=ia_icon)
                possibilities = "None"

            elif cmds.iconTextButton(center_button, query=True, image=True) == user_icon:
                user_indexes = [2, 4, 6, 8]
                conter_indexes = [8, 6, 4, 2]

                for index in range(len(user_indexes)):
                    if user_move == "ttt_button0" + str(user_indexes[index]):
                        counter_button = "ttt_button0" + \
                            str(conter_indexes[index])
                        if cmds.iconTextButton(user_move, query=True, image=True) == user_icon:
                            if cmds.iconTextButton(user_move, query=True, image=True) == idle_icon:
                                cmds.iconTextButton(counter_button,
                                                    edit=True, image=ia_icon)
                                possibilities = "None"
                                break

            # what if counter move is not available
            # #####################################
            if not possibilities:
                for counter_index in range(1, 9):
                    counter_button = "ttt_button0" + str(counter_index)
                    if cmds.iconTextButton(counter_button, query=True, image=True) == idle_icon:
                        cmds.iconTextButton(counter_button, edit=True,
                                            image=ia_icon)
                        break

        # counter move outer edges:
        ###############################################

        elif button in edge_buttons:
            possibilities = ""

            if center_button == idle_icon:
                edge_buttons.remove(user_move)
                counter_buttons = []
                for edge_button in edge_buttons:
                    counter_button = cmds.iconTextButton(edge_button, query=True,
                                                         image=True)
                    if counter_button == idle_icon:
                        counter_buttons.append(counter_button)

                if len(counter_buttons) == 3:
                    cmds.iconTextButton(center_button, edit=True,
                                        image=ia_icon)

            else:
                user_indexes = [1, 3, 7, 9]
                counter_index = [9, 7, 3, 1]
                for index in range(len(user_indexes)):
                    if user_move == "ttt_button0" + str(user_indexes[index]):
                        counter_button = "ttt_button0" + \
                            str(counter_index[index])
                        if cmds.iconTextButton(user_move, query=True, image=True) == user_icon:
                            if cmds.iconTextButton(user_move, query=True, image=True) == idle_icon:
                                cmds.iconTextButton(counter_button,
                                                    edit=True, image=ia_icon)
                                possibilities = "None"
                                break

            # what if counter move is not available
            # #####################################
            if not possibilities:
                for counter_index in range(1, 9):
                    counter_button = "ttt_button0" + str(counter_index)
                    if cmds.iconTextButton(counter_button, query=True, image=True) == idle_icon:
                        cmds.iconTextButton(
                            counter_button, edit=True, image=ia_icon)
                        break
    check_results(USERPATH)
