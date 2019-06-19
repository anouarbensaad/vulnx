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
    #banner Colors
    bannerblue  = '\033[34m'
    bannerblue2 = '\033[1;1;94m'
    yellowhead  = '\033[1;1;94m'
    #default colors
    W           = '\033[97m'  # white
    Y           = '\033[93m' # yellow
    R           = '\033[91m'
    G           = '\033[92m'
    B           = '\033[94m'
    bg          = '\033[7;91m'
    green       = '\033[92m'
    #action colors
    run         = '\033[93m[~]\033[0m'
    good        = '\033[92m[+]\033[0m'
    bad         = '\033[91m[-]\033[0m'
    info        = '\033[93m[!]\033[0m'
    red         = '\033[91m'
    end         = '\033[0m'
    que         = '\033[94m[?]\033[0m'
    #test colors
    failexploit = '\033[91mFAIL\033[0m'
    vulnexploit = '\033[92mVULN\033[0m'
    portopen    = '\033[92mOPEN \033[0m'
    portclose   = '\033[91mCLOSE\033[0m'
