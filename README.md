*************************************************************************

Tic-tac-toe:

*************************************************************************
 Author: Laura Siviero;
         laura.seav@gmail.com
 
 Date 2021.05.05
*************************************************************************

Description:
  - the tool allows you to play tic tac toe on maya (python 2.7);
  - Tool for Maya;

*************************************************************************
 License: MIT https://github.com/laurasiviero/TicTacToe/blob/main/LICENSE
 
 Author: Laura Siviero
         laura.seav@gmail.com
 
*************************************************************************

Instructions:
   - Put the useless_ui folder in the folder: 
     C:\Users\YOU\Documents\maya\20XX\scripts
   - Extract everything in the same location;
   - Launch maya;
   - Copy the following line in the script editor, make sure to change the path in the next lines too:

*************************************************************************
import sys

USERPATH = r"C:\Users\YOU\Documents\maya\20XX\scripts\TicTacToe"
sys.path.append(USERPATH)

import ttt_ui
ttt_ui.tic_tac_toe_ui(USERPATH)
 
 *************************************************************************
 
 - Feel free to add the code to your shelf;
 - Replace the default shelf icon with the appropriate one: TicTacToe\tic_tac_toe_icons\tic_tac_toe_shelf;
 - DO NOT MOVE ANY SUBFOLDERS;
 - Have fun!
