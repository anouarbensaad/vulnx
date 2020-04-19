'''
Module Of Colors.
OS : Ubuntu
'''

import sys

if sys.platform.lower().startswith(('os', 'win', 'darwin', 'ios')):
    # Colors shouldn't be displayed on Mac and Windows
    bannerblue = bannerblue2 = yellowhead = \
        W = Y = R = G = B = bg = green = \
        run = good = bad = info = red = end = que = \
        failexploit = vulnexploit = portopen = portclose = ''
else:
    # banner Colors
    bannerblue = '\033[1;0;34m'
    bannerblue2 = '\033[1;1;94m'
    yellowhead = '\033[1;1;94m'
    # default colors
    W = '\033[1;97m'  # white
    Y = '\033[1;93m'  # yellow
    R = '\033[1;91m'
    G = '\033[1;92m'
    B = '\033[1;94m'
    bg = '\033[7;91m'
    green = '\033[1;92m'
    # action colors
    run = '\033[1;93m[~]\033[1;97m'
    good = '\033[1;92m[+]\033[1;97m'
    bad = '\033[1;91m[-]\033[1;97m'
    info = '\033[1;93m[!]\033[1;97m'
    red = '\033[1;91m'
    end = '\033[1;0m'
    que = '\033[1;94m[?]\033[1;97m'
    # test colors
    failexploit = '\033[91mFAIL\033[1m'
    vulnexploit = '\033[92mVULN\033[1m'
    portopen = '\033[92mOPEN \033[1m'
    portclose = '\033[91mCLOSE\033[1m'
