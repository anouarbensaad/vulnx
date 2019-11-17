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

numberpage=1 #default page−dork variable
output_dir='logs'#default output−dork

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

class Helpers():

    @staticmethod
    def _general_help():
        print("""
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

    @staticmethod
    def _url_action_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        timeout                 set timeout
        ports                   scan ports
        domain                  get domains & sub domains
        cms info                get cms info (version , user ..)
        web info                get web info
        dump dns                dump dns get sub domains [mx-server..]
        run exploit             run exploits corresponding to cms
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    #dorks - command helpers. 

    @staticmethod
    def _dorks_action_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        list                    list dorks
        set dork                set exploit name
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        pages                   set num page
        output                  output file.
        run                     search web with specified dork
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_page_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        output                  output file.
        run                     search web with specified dork
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_output_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        pages                   set num page
        run                     search web with specified dork
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

    @staticmethod
    def _dorks_setdork_page_output_help():
        print("""
        Command                 Description
        --------                -------------
        help/?                  Show this help menu.
        run                     search web with specified dork
        clear/cls               clear the vulnx screen
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)

class Cli(object):

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
    def _clearscreen():
        return os.system('clear')

    @staticmethod
    def getDork(pattern):
        dork_search=r'^set dork (.+)'
        try:
            dork=re.search(re.compile(dork_search),pattern).group(1)
        except AttributeError:  # No match is found
            dork=re.search(re.compile(dork_search),pattern)
        if dork:
            return dork
    
    @staticmethod
    def setPage(page):
        page_search=r'^page (\d+$)'
        try:
            page=re.search(re.compile(page_search),page).group(1)
        except AttributeError:  # No match is found
            page=re.search(re.compile(page_search),page)
        if page:
            return int(page)

    @staticmethod
    def setOutput(directory):
        output=r'^output (\w+$)'
        try:
            rep=re.search(re.compile(output),directory).group(1)
        except AttributeError:  # No match is found
            rep=re.search(re.compile(output),directory)
        if rep:
            return rep

    @property
    def getUrl(self,pattern):
        url_search=r'^set url (.+)'
        try:
            url=re.search(re.compile(url_search),pattern).group(1)
        except AttributeError:  # No match is found
            url=re.search(re.compile(url_search),pattern)
        if url:
            return url#ParseURL(url)

    def variable(self):
        print("a")

    def setdorkCLI(self,cmd_interpreter):
        
        # REGEX

        output=re.compile(r'^output \w+$')
        page=re.compile(r'^page \d+$')
        dorkname=re.compile(r'^set dork .+')
        
        '''SET DORK VARIABLE'''
        
        while True:
            cmd_interpreter=input("%s%svulnx%s%s (%sDorks%s)> %s" %(bannerblue2,W_UL,end,W,B,W,end))
            if cmd_interpreter == 'back':
                break
            if cmd_interpreter == 'list':
            
                '''SET DORK LIST'''

                print('\n%s[*]%s Listing dorks name..' %(B,end))
                from modules.dorksEngine import DorkList as DL
                DL.dorkslist()
            if cmd_interpreter=='clear' or cmd_interpreter=='cls':
                Cli._clearscreen()
            if cmd_interpreter=='exit':
                sys.exit()
            if cmd_interpreter == 'help' or cmd_interpreter == '?':
                Helpers._dorks_action_help()

                '''SET DORK NAME.'''

            if dorkname.search(cmd_interpreter):
                while True:
                    cmd_interpreter_wp=input("%s%svulnx%s%s (%sDorks-%s%s)> %s" %(bannerblue2,W_UL,end,W,B,Cli.getDork(cmd_interpreter),W,end))

                    '''SET PAGE VARIABLE.'''

                    if page.search(cmd_interpreter_wp):
                        while True:
                            cmd_interpreter_wp_page=input("%s%svulnx%s%s (%sDorks-%s-%s%s)> %s" %(bannerblue2,W_UL,end,W,B,Cli.getDork(cmd_interpreter),Cli.setPage(cmd_interpreter_wp),W,end))
                            
                            if output.search(cmd_interpreter_wp_page):
                                while True:
                                    cmd_interpreter_wp_page_output=input("%s%svulnx%s%s (%sDorks-%s-%s%s)> %s" %(bannerblue2,W_UL,end,W,B,Cli.getDork(cmd_interpreter),Cli.setPage(cmd_interpreter_wp),W,end))
                                    
                                    if cmd_interpreter_wp_page_output=='run':
                                        print('\n')
                                        from modules.dorksEngine import Dorks as D
                                        D.searchengine(Cli.getDork(cmd_interpreter),headers,Cli.setOutput(cmd_interpreter_wp),Cli.setPage(cmd_interpreter_wp))
                                    if cmd_interpreter_wp_page_output=='back':
                                        break
                                    if cmd_interpreter_wp_page_output=='help' or cmd_interpreter_wp_page_output=='?':
                                        Helpers._dorks_setdork_page_output_help()
                                    if cmd_interpreter_wp_page_output=='clear' or cmd_interpreter_wp_page_output=='cls':
                                        Cli._clearscreen()
                                    if cmd_interpreter_wp_page_output=='exit':
                                        sys.exit()

                            if cmd_interpreter_wp_page=='run':
                                print('\n')
                                from modules.dorksEngine import Dorks as D
                                D.searchengine(Cli.getDork(cmd_interpreter),headers,output_dir,Cli.setPage(cmd_interpreter_wp))
                            if cmd_interpreter_wp_page=='back':
                                break
                            if cmd_interpreter_wp_page=='help' or cmd_interpreter_wp_page=='?':
                                Helpers._dorks_setdork_page_help()
                            if cmd_interpreter_wp_page=='clear' or cmd_interpreter_wp_page=='cls':
                                Cli._clearscreen()
                            if cmd_interpreter_wp_page=='exit':
                                sys.exit()

                    '''SET OUTPUT VARIABLE.'''

                    if output.search(cmd_interpreter_wp):
                        while True:
                            cmd_interpreter_wp_output=input("%s%svulnx%s%s (%sDorks-%s%s)> %s" %(bannerblue2,W_UL,end,W,B,Cli.getDork(cmd_interpreter),W,end))
                            if cmd_interpreter_wp_output=='run':
                                print('\n')
                                from modules.dorksEngine import Dorks as D
                                D.searchengine(Cli.getDork(cmd_interpreter),headers,Cli.setOutput(cmd_interpreter_wp),numberpage)
                            if cmd_interpreter_wp_output=='back':
                                break
                            if cmd_interpreter_wp_output=='clear' or cmd_interpreter_wp_output=='cls':
                                Cli._clearscreen()
                            if cmd_interpreter_wp_output=='exit':
                                sys.exit()
                            if cmd_interpreter_wp_output=='help' or cmd_interpreter_wp_output=='?':
                                Helpers._dorks_setdork_output_help()

                    if cmd_interpreter_wp=='run':
                        print('\n')
                        from modules.dorksEngine import Dorks as D
                        D.searchengine(Cli.getDork(cmd_interpreter),headers,output_dir,numberpage)
                    if cmd_interpreter_wp=='back':
                        break
                    if cmd_interpreter_wp=='help' or cmd_interpreter_wp=='?':
                        Helpers._dorks_setdork_help()
                    if cmd_interpreter_wp=='clear' or cmd_interpreter_wp=='cls':
                        Cli._clearscreen()
                    if cmd_interpreter_wp=='exit':
                        sys.exit()



    def send_commands(self,cmd):
        reurl=re.compile(r'^set url .+')
        redork=re.compile(r'^dork')
        while True:
            cmd = input("%s%svulnx%s > "% (bannerblue2,W_UL,end))
            dork_command="dorks"
            if reurl.search(cmd):
                #url session
                while True:
                    cmd_interpreter=input("%s%svulnx%s%s target(%s%s%s) > %s" %(bannerblue2,W_UL,end,W,R,self.getUrl(cmd),W,end))
                    if cmd_interpreter == 'back':
                        break
                    elif cmd_interpreter == 'run exploit':
                        print('\n%s[*]%s Running exploits..' %(B,end))
                        root = self.getUrl(cmd)
                        if root.startswith('http'):
                            url_root = root
                        else:
                            url_root = 'http://'+url_root
                        self.__runExploits(url_root,headers)
                    elif cmd_interpreter == 'help' or cmd_interpreter == '?':
                        Helpers._url_action_help()
                    elif cmd == 'quit' or cmd == 'exit':
                        sys.exit()
                    else:
                        print("you mean (cms info) or (web info) show more use help ?")
            elif redork.search(cmd):
                #dork session
                self.setdorkCLI(cmd)
            elif cmd == 'quit' or cmd == 'exit':
                sys.exit()
            elif cmd == 'help' or cmd == '?':
                Helpers._general_help()
            elif cmd == 'clear' or cmd == 'cls':
                Cli._clearscreen()

            else:
                print("you mean (cms info) or (web info) show more use help ?")
