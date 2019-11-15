import sys
import time
import os
import re
from common.colors import end,W,R,B,bannerblue2
from common.banner import banner
from common.requestUp import random_UserAgent
from common.uriParser import parsing_url
from modules.wpExploits import(   wp_wysija,
                                  wp_blaze,
                                  wp_catpro,
                                  wp_cherry,
                                  wp_dm,
                                  wp_fromcraft,
                                  wp_jobmanager,
                                  wp_showbiz,
                                  wp_synoptic,
                                  wp_shop,
                                  wp_powerzoomer,
                                  wp_revslider,
                                  wp_adsmanager,
                                  wp_inboundiomarketing,
                                  wp_levoslideshow,
                                  wp_adblockblocker,
                                )

headers = {
'host' : 'google.com',
'User-Agent' : random_UserAgent(),
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Connection': 'keep-alive',}

history = []

variables = {
	"URL":'',
	"TIMEOUT":'',
	"URL":'',
	"COMMAND":'',
	"FILE_PATH":'',
	"USERNAME":'',
	"PASSWORD":''
}

W_UL= "\033[4m"
RED_U='\033[1;1;91m'


vulnresults = set()  # results of vulnerability exploits. [success or failed]
grabinfo = set()  # return cms_detected the version , themes , plugins , user .. 
subdomains = set() # return subdomains & ip.
hostinfo = set() # host info
data = [ vulnresults, grabinfo, subdomains , hostinfo]

data_names = ['vulnresults', 'grabinfo', 'subdomains' , 'hostinfo']

data = {
    'vulnresults':list(vulnresults),
    'grabinfo':list(grabinfo),
    'subdomains':list(subdomains),
}

class Cli():
    #banner_function
    banner()

    def __runExploits(self,url,headers):
        wp_wysija(url,headers,vulnresults)
        wp_blaze(url,headers,vulnresults)
        wp_catpro(url,headers,vulnresults)
        wp_cherry(url,headers,vulnresults)
        wp_dm(url,headers,vulnresults)
        wp_fromcraft(url,headers,vulnresults)
        wp_shop(url,headers,vulnresults)
        wp_revslider(url,headers,vulnresults)
        wp_adsmanager(url,headers,vulnresults)
        wp_inboundiomarketing(url,headers,vulnresults)
        wp_levoslideshow(url,headers,vulnresults)
        wp_adblockblocker(url,headers,vulnresults)

    @staticmethod
    def _general_help():
        generalhelp=print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        clear/cls               clear the vulnx screen
        use       <Variable>    Use an variable.
        info      <Variable>    Get information about an available variable.
        set <variable> <value>  Sets a context-specific variable to a value to use while using vulnx.
        variables               Prints all previously specified variables.
        banner                  Display banner.
        history                 Display command-line most important history from the beginning.
        makerc                  Save command-line history to a file.
        os         <command>    Execute a system command without closing the vulnx-mode
        exit/quit               Exit the vulnx-mode
        """)
        return generalhelp

    @staticmethod
    def _url_action_help():
        urlactions=print("""
        Command                 Description
        --------                -------------
        ?          \t\tHelp menu
        timeout    \t\tset timeout
        ports      \t\tscan ports
        domain     \t\tget domains & sub domains
        cms info   \t\tget cms info (version , user ..)
        web info   \t\tget web info
        dump dns   \t\tdump dns get sub domains [mx-server..]
        run exploit\t\trun exploits corresponding to cms
        back       \t\tmove back from current context
        """)
        return urlactions

    @staticmethod
    def _dorks_action_help():
        print("""
        Command                 Description
        --------                -------------
        ?          \t\tHelp menu
        list       \t\tset timeout
        use        \t\tscan ports
        num page   \t\tget domains & sub domains
        run        \t\tget cms info (version , user ..)
        back       \t\tmove back from current context
        """)

    @staticmethod
    def _clearscreen():
        return os.system('clear')

    @staticmethod
    def _generalCLI(url):
        regex=r'^set url (.+)'
        url=re.search(re.compile(regex),url).group(1)
        if url:
            return url#ParseURL(url)
        else:
            print("need (help) (?)")

    def send_commands(self,cmd):
        regxpr=re.compile(r'^set url')

        while True:
            cmd = input("%s%svulnx%s > "% (bannerblue2,W_UL,end))
            dork_command="dorks"
            
            if regxpr.search(cmd):
                # url target
                while True:
                    cmd_interpreter=input("%s%svulnx%s%s target(%s%s%s) > %s" %(bannerblue2,W_UL,end,W,R,Cli._generalCLI(cmd),W,end))
                    if cmd_interpreter == 'back':
                        break
                    elif cmd_interpreter == 'run exploit':
                        print('\n%s[*]%s Running exploits..' %(B,end))
                        root = Cli._generalCLI(cmd)
                        if root.startswith('http'):
                            url_root = root
                        else:
                            url_root = 'http://'+url_root
                        self.__runExploits(url_root,headers)
                    elif cmd_interpreter == 'help' or cmd_interpreter == '?':
                        Cli._url_action_help()
                    elif cmd == 'quit' or cmd == 'exit':
                        sys.exit()
                    else:
                        print("you mean (cms info) or (web info) show more use help ?")
            elif cmd == dork_command:
                
                while True:
                    cmd_interpreter=input("%svulnx (%sDorks%s)> %s" %(W,B,W,end))
                    if cmd_interpreter == 'back':
                        break
                    if cmd_interpreter == 'run exploit':
                        print('\n%s[*]%s Running exploits..' %(B,end))
                    if cmd_interpreter == 'help' or cmd_interpreter == '?':
                        self._dorks_action_help()
            elif cmd == 'quit' or cmd == 'exit':
                sys.exit()
            elif cmd == 'help' or cmd == '?':
                self._general_help()
            elif cmd == 'clear' or cmd == 'cls':
                Cli._clearscreen()

            else:
                print("you mean (cms info) or (web info) show more use help ?")
