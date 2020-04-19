
import sys

import time
import os
import re
import readline
import glob
import subprocess
from common.colors import end, W, R, B, bannerblue2
from common.banner import banner
from common.requestUp import random_UserAgent
from common.uriParser import parsing_url
from modules.cli.helpers import Helpers
from modules.dorks.engine import Dork
from modules.detector import CMS

url_regx = re.compile(r'^set url .+')
dork_regx = re.compile(r'^dork')
exec_regx = re.compile(r'^exec .+')
help_regx = re.compile(r'^help')
history_regx = re.compile(r'^history')
exit_regx = re.compile(r'^exit')
cls_regx = re.compile(r'^clear')
var_regx = re.compile(r'^variable')
back_regx = re.compile(r'^back')
run_regx = re.compile(r'^run')
output = re.compile(r'^output \w+$')
page = re.compile(r'^page \d+$')
dorkname_regx = re.compile(r'^set dork .+')
list_regx = re.compile(r'^list')

W_UL = "\033[4m"
RED_U = '\033[1;1;91m'
man_gloabal = ["help", "clear", "use", "info", "set", "variables", "history", "exec", "dork"]
man_dork = ["help", "list", "set dork", "clear", "history", "variables", "exec", "back"]
man_setdork = ["help", "output", "page", "run", "clear", "exec", "history", "variables", "back"]
man_dorkpage = ["help", "output", "run", "clear", "exec", "history", "variables", "back"]
man_dorkoutput = ["help", "page", "run", "clear", "exec", "history", "variables", "back"]
man_dorkpage_output = [ "help", "run", "clear", "exec", "history", "variables", "back" ]
history=[]

# VARIABLE
numberpage = 1  # default page−dork variable
output_dir = 'logs'  # default output−dork
dorkname = ''
url = ''
timeout = ''

headers = {
    'host': 'google.com',
    'User-Agent': random_UserAgent(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive', }

class CLI():

    def __init__(self,headers=None):
        self.headers = headers

    def run_exploits(self,url,headers):
        cms = CMS(url=url,headers=headers,exploit=True)
        cms.instanciate()
    
    def dork_variable(self,dorkname, output, page):
        print("""
        VARIABLE        VALUE
        --------        -----
        dorkname        %s
        output          %s
        pages           %s

        """ % (dorkname, output, page))

    def url_variable(self,url, timeout):
        print("""
        VARIABLE        VALUE
        --------        -----
        url             %s
        timeout         %s

        """ % (url, timeout))

    def global_variables(self,dorkname, output, page, url, timeout):
        print("""
        VARIABLE        VALUE
        --------        -----
        url             %s
        timeout         %s
        dorkname        %s
        output          %s
        pages           %s

        """ % (dorkname, output, page, url, timeout))

    def __clearscreen__(self):
        return os.system('clear')

    def createListCompleter(self, ll):
        def listCompleter(text, state):
            line = readline.get_line_buffer()
            if not line:
                return [c + " " for c in ll][state]
            else:
                return [c + " " for c in ll if c.startswith(line)][state]
        self.listCompleter = listCompleter

    def autocompleter(self,manual):
        self.createListCompleter(manual)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(self.listCompleter)

    def _exec(self,cmd):
        regx = r'^exec (.+)'
        try:
            command = re.search(re.compile(regx), cmd).group(1)
        except AttributeError:  # No match is found
            command = re.search(re.compile(regx), cmd)
        if command:
            return os.system(command)

    def get_dork(self,pattern):
        dork_search = r'^set dork (.+)'
        try:
            dork = re.search(re.compile(dork_search), pattern).group(1)
        except AttributeError:  # No match is found
            dork = re.search(re.compile(dork_search), pattern)
        if dork:
            return dork

    def set_page(self,page):
        page_search = r'^page (\d+$)'
        try:
            page = re.search(re.compile(page_search), page).group(1)
        except AttributeError:  # No match is found
            page = re.search(re.compile(page_search), page)
        if page:
            return int(page)

    def set_output(self,directory):
        output = r'^output (\w+$)'
        try:
            rep = re.search(re.compile(output), directory).group(1)
        except AttributeError:  # No match is found
            rep = re.search(re.compile(output), directory)
        if rep:
            return rep

    def get_url(self, pattern):
        url_search = r'^set url (.+)'
        try:
            url = re.search(re.compile(url_search), pattern).group(1)
        except AttributeError:  # No match is found
            url = re.search(re.compile(url_search), pattern)
        if url:
            return url  # ParseURL(url)

    def cli_dork(self,interepter):
        helpers = Helpers()

        while True:

            self.autocompleter(man_dork)
            cmd_interpreter = input("{0}{1}vulnx{2}{3} ({4}Dorks{5})>> {6}" .format(bannerblue2, W_UL, end, W, B, W, end))
            history.append(cmd_interpreter)
            if back_regx.search(cmd_interpreter):
                break
            if list_regx.search(cmd_interpreter):
                print('\n{0}[*]{1} Listing dorks name..' .format (B, end))
            if cls_regx.search(cmd_interpreter) or cmd_interpreter == 'cls':
                self.__clearscreen__()
            if exit_regx.search(cmd_interpreter) or cmd_interpreter == 'quit':
                sys.exit()
            if help_regx.search(cmd_interpreter) or cmd_interpreter == '?':
                helpers._dorks_action_help()
        
            if history_regx.search(cmd_interpreter):
                for i in range(len(history)):
                    print(" {0}  {1}" .format(i+1, history[i-1]))
            if exec_regx.search(cmd_interpreter):
                self._exec(cmd_interpreter)
            if var_regx.search(cmd_interpreter):
                self.dork_variable(dorkname, output_dir, numberpage)
            if dorkname_regx.search(cmd_interpreter):

                while True:

                    self.autocompleter(man_setdork)
                    cmd_interpreter_wp = input("{0}{1}vulnx{2}{3} ({4}Dorks-{5}{6})>> {7}" .format (bannerblue2, W_UL, end, W, B, self.get_dork(cmd_interpreter), W, end))
                    history.append(cmd_interpreter_wp)
                    '''SET PAGE VARIABLE.'''

                    if page.search(cmd_interpreter_wp):

                        while True:

                            self.autocompleter(man_dorkpage)
                            cmd_interpreter_wp_page = input("{0}{1}vulnx{2}{3} ({4}Dorks-{5}-{6}{7})>> {8}" .format (
                                bannerblue2, W_UL, end, W, B, self.get_dork(cmd_interpreter), self.set_page(cmd_interpreter_wp), W, end))
                            history.append(cmd_interpreter_wp_page)
                            if output.search(cmd_interpreter_wp_page):
                                while True:
                                    self.autocompleter(man_dorkoutput)
                                    cmd_interpreter_wp_page_output = input("{0}{1}vulnx{2}{3} ({4}Dorks-{5}-{6}{7})>> {8}" .format (
                                        bannerblue2, W_UL, end, W, B, self.get_dork(cmd_interpreter), self.set_page(cmd_interpreter_wp), W, end))
                                    history.append(cmd_interpreter_wp_page_output)

                                    if run_regx.search(cmd_interpreter_wp_page_output):
                                        print('\n')
                                        DEngine = Dork(exploit=self.get_dork(cmd_interpreter),headers=self.headers,pages=self.set_page(cmd_interpreter_wp))
                                        DEngine.search()
                                    if run_regx.search(cmd_interpreter_wp_page_output):
                                        print('\n')
                                    if back_regx.search(cmd_interpreter_wp_page_output):
                                        break
                                    if help_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == '?':
                                        helpers._dorks_setdork_page_output_help()
                                    if cls_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == 'cls':
                                        self.__clearscreen__()
                                    if exit_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == 'quit':
                                        sys.exit()
                                    if history_regx.search(cmd_interpreter_wp_page_output):
                                        for i in range(len(history)):
                                            print(" {0}  {1}" .format(i+1, history[i-1]))
                                    if exec_regx.search(cmd_interpreter_wp_page_output):
                                        self._exec(
                                            cmd_interpreter_wp_page_output)



                            if run_regx.search(cmd_interpreter_wp_page):
                                print('\n')
                                DEngine = Dork(exploit=self.get_dork(cmd_interpreter),headers=self.headers,pages=self.set_page(cmd_interpreter_wp))
                                DEngine.search()
                            if run_regx.search(cmd_interpreter_wp_page):
                                print('\n')
                            if back_regx.search(cmd_interpreter_wp_page):
                                break
                            if help_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == '?':
                                Helpers._dorks_setdork_page_help()
                            if cls_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == 'cls':
                                self.__clearscreen__()
                            if exit_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == 'quit':
                                sys.exit()
                            if history_regx.search(cmd_interpreter_wp_page):
                                for i in range(len(history)):
                                    print(" {0}  {1}" .format(i+1, history[i-1]))
                            if exec_regx.search(cmd_interpreter_wp_page):
                                self._exec(cmd_interpreter_wp_page)
                            if var_regx.search(cmd_interpreter_wp_page):
                                self.dork_variable(self.get_dork(cmd_interpreter), output_dir, self.set_page(cmd_interpreter_wp))


    def general(self,cmd):
        while True:
            self.autocompleter(man_gloabal)
            cmd = input("%s%svulnx%s > " % (bannerblue2, W_UL, end))
            history.append(cmd)
            if url_regx.search(cmd):
                # url session
                while True:
                    cmd_interpreter = input("%s%svulnx%s%s target(%s%s%s) > %s" % (
                        bannerblue2, W_UL, end, W, R, self.get_url(cmd), W, end))
                    history.append(cmd_interpreter)
                    if cmd_interpreter == 'back':
                        break
                    elif cmd_interpreter == 'run exploit':
                        print('\n%s[*]%s Running exploits..' % (B, end))
                        root = self.get_url(cmd)
                        if root.startswith('http'):
                            url_root = root
                        else:
                            url_root = 'http://'+url_root
                        self.run_exploits(url_root,self.headers)
                    elif help_regx.search(cmd_interpreter) or cmd_interpreter == '?':
                        Helpers._url_action_help()
                    elif exit_regx.search(cmd_interpreter) or cmd_interpreter == 'quit':
                        sys.exit()
                    else:
                        print("use (help) (?) to show man commands.")
            elif dork_regx.search(cmd):
                # dork session
                self.cli_dork(cmd)
            elif exit_regx.search(cmd) or cmd == 'quit':
                sys.exit()
            elif help_regx.search(cmd) or cmd == '?':
                Helpers._general_help()
            elif cls_regx.search(cmd) or cmd == 'cls':
                self.__clearscreen__()
            elif history_regx.search(cmd):
                for i in range(len(history)):
                    print(" %s  %s" % (i+1, history[i-1]))
            elif exec_regx.search(cmd):
                self._exec(cmd)
            elif var_regx.search(cmd):
                self.global_variables(dorkname, output_dir,
                                     numberpage, url, timeout)
            else:
                print("use (help) (?) to show man commands.")

