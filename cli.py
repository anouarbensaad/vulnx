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
from modules.wpExploits import(wp_wysija,
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


headers = {
    'host': 'google.com',
    'User-Agent': random_UserAgent(),
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive', }

history = []

# VARIABLE
numberpage = 1  # default page−dork variable
output_dir = 'logs'  # default output−dork
dorkname = ''
url = ''
timeout = ''

W_UL = "\033[4m"
RED_U = '\033[1;1;91m'

# autocompleter
autocompleter_global = ["help", "clear", "use", "info",
                        "set", "variables", "history", "exec", "dork"]
autocompleter_dork = ["help", "list", "set dork",
                      "clear", "history", "variables", "exec", "back"]
autocompleter_setdork = ["help", "output", "page",
                         "run", "clear", "exec", "history", "variables", "back"]
autocompleter_dork_page = ["help", "output", "run",
                           "clear", "exec", "history", "variables", "back"]
autocompleter_dork_output = ["help", "page", "run",
                             "clear", "exec", "history", "variables", "back"]
autocompleter_dork_page_output = [
    "help", "run", "clear", "exec", "history", "variables", "back"]

vulnresults = set()  # results of vulnerability exploits. [success or failed]
# return cms_detected the version , themes , plugins , user ..
grabinfo = set()
subdomains = set()  # return subdomains & ip.
hostinfo = set()  # host info
data = [vulnresults, grabinfo, subdomains, hostinfo]

data_names = ['vulnresults', 'grabinfo', 'subdomains', 'hostinfo']

data = {
    'vulnresults': list(vulnresults),
    'grabinfo': list(grabinfo),
    'subdomains': list(subdomains),
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
        exec       <command>    Execute a system command without closing the vulnx-mode
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

    # dorks - command helpers.

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
        exec       <command>    Execute a system command without closing the vulnx-mode
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
        exec       <command>    Execute a system command without closing the vulnx-mode
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
        exec       <command>    Execute a system command without closing the vulnx-mode
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
        exec       <command>    Execute a system command without closing the vulnx-mode
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
        exec       <command>    Execute a system command without closing the vulnx-mode
        history                 Display command-line most important history from the beginning.
        variables               Prints all previously specified variables.
        back                    move back from current context
        """)


class Cli():

    def __runExploits(self, url, headers):
        wp_wysija(url, headers, vulnresults)
        wp_blaze(url, headers, vulnresults)
        wp_catpro(url, headers, vulnresults)
        wp_cherry(url, headers, vulnresults)
        wp_dm(url, headers, vulnresults)
        wp_fromcraft(url, headers, vulnresults)
        wp_shop(url, headers, vulnresults)
        wp_revslider(url, headers, vulnresults)
        wp_adsmanager(url, headers, vulnresults)
        wp_inboundiomarketing(url, headers, vulnresults)
        wp_levoslideshow(url, headers, vulnresults)
        wp_adblockblocker(url, headers, vulnresults)

    def pathCompleter(self, text, state):
        line = readline.get_line_buffer().split()
        return [x for x in glob.glob(text+'*')][state]

    def createListCompleter(self, ll):
        def listCompleter(text, state):
            line = readline.get_line_buffer()
            if not line:
                return [c + " " for c in ll][state]
            else:
                return [c + " " for c in ll if c.startswith(line)][state]
        self.listCompleter = listCompleter

    @staticmethod
    def autoComplete_Global():
        t = Cli()
        t.createListCompleter(autocompleter_global)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def autoComplete_Dork():
        t = Cli()
        t.createListCompleter(autocompleter_dork)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def autoComplete_Page():
        t = Cli()
        t.createListCompleter(autocompleter_dork_page)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def autoComplete_Output():
        t = Cli()
        t.createListCompleter(autocompleter_dork_output)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def autoComplete_Page_Output():
        t = Cli()
        t.createListCompleter(autocompleter_dork_page_output)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def autoComplete_setdork():
        t = Cli()
        t.createListCompleter(autocompleter_setdork)
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(t.listCompleter)

    @staticmethod
    def dork_variable(dorkname, output, page):
        print("""
        VARIABLE        VALUE
        --------        -----
        dorkname        %s
        output          %s
        pages           %s

        """ % (dorkname, output, page))

    @staticmethod
    def url_variable(url, timeout):
        print("""
        VARIABLE        VALUE
        --------        -----
        url             %s
        timeout         %s

        """ % (url, timeout))

    @staticmethod
    def global_variables(dorkname, output, page, url, timeout):
        print("""
        VARIABLE        VALUE
        --------        -----
        url             %s
        timeout         %s
        dorkname        %s
        output          %s
        pages           %s

        """ % (dorkname, output, page, url, timeout))

    @staticmethod
    def _clearscreen():
        return os.system('clear')

    @staticmethod
    def _exec(cmd):
        regx = r'^exec (.+)'
        try:
            command = re.search(re.compile(regx), cmd).group(1)
        except AttributeError:  # No match is found
            command = re.search(re.compile(regx), cmd)
        if command:
            return os.system(command)

    @staticmethod
    def getDork(pattern):
        dork_search = r'^set dork (.+)'
        try:
            dork = re.search(re.compile(dork_search), pattern).group(1)
        except AttributeError:  # No match is found
            dork = re.search(re.compile(dork_search), pattern)
        if dork:
            return dork

    @staticmethod
    def setPage(page):
        page_search = r'^page (\d+$)'
        try:
            page = re.search(re.compile(page_search), page).group(1)
        except AttributeError:  # No match is found
            page = re.search(re.compile(page_search), page)
        if page:
            return int(page)

    @staticmethod
    def setOutput(directory):
        output = r'^output (\w+$)'
        try:
            rep = re.search(re.compile(output), directory).group(1)
        except AttributeError:  # No match is found
            rep = re.search(re.compile(output), directory)
        if rep:
            return rep

    @property
    def getUrl(self, pattern):
        url_search = r'^set url (.+)'
        try:
            url = re.search(re.compile(url_search), pattern).group(1)
        except AttributeError:  # No match is found
            url = re.search(re.compile(url_search), pattern)
        if url:
            return url  # ParseURL(url)

    def setdorkCLI(self, cmd_interpreter):

        # REGEX
        '''SET DORK VARIABLE'''

        while True:
            Cli.autoComplete_Dork()
            cmd_interpreter = input("%s%svulnx%s%s (%sDorks%s)> %s" % (
                bannerblue2, W_UL, end, W, B, W, end))
            history.append(cmd_interpreter)
            if back_regx.search(cmd_interpreter):
                break
            if list_regx.search(cmd_interpreter):

                '''SET DORK LIST'''

                print('\n%s[*]%s Listing dorks name..' % (B, end))
                from modules.dorksEngine import DorkList as DL
                DL.dorkslist()
            if cls_regx.search(cmd_interpreter) or cmd_interpreter == 'cls':
                Cli._clearscreen()
            if exit_regx.search(cmd_interpreter) or cmd_interpreter == 'quit':
                sys.exit()
            if help_regx.search(cmd_interpreter) or cmd_interpreter == '?':
                Helpers._dorks_action_help()
            if history_regx.search(cmd_interpreter):
                for i in range(len(history)):
                    print(" %s  %s" % (i+1, history[i-1]))
            if exec_regx.search(cmd_interpreter):
                Cli._exec(cmd_interpreter)
            if var_regx.search(cmd_interpreter):
                Cli.dork_variable(dorkname, output_dir, numberpage)

                '''SET DORK NAME.'''

            if dorkname_regx.search(cmd_interpreter):
                while True:
                    Cli.autoComplete_setdork()
                    cmd_interpreter_wp = input("%s%svulnx%s%s (%sDorks-%s%s)> %s" % (
                        bannerblue2, W_UL, end, W, B, Cli.getDork(cmd_interpreter), W, end))
                    history.append(cmd_interpreter_wp)
                    '''SET PAGE VARIABLE.'''
                    if page.search(cmd_interpreter_wp):
                        while True:
                            Cli.autoComplete_Page()
                            cmd_interpreter_wp_page = input("%s%svulnx%s%s (%sDorks-%s-%s%s)> %s" % (
                                bannerblue2, W_UL, end, W, B, Cli.getDork(cmd_interpreter), Cli.setPage(cmd_interpreter_wp), W, end))
                            history.append(cmd_interpreter_wp_page)
                            if output.search(cmd_interpreter_wp_page):
                                while True:
                                    Cli.autoComplete_Page_Output()
                                    cmd_interpreter_wp_page_output = input("%s%svulnx%s%s (%sDorks-%s-%s%s)> %s" % (
                                        bannerblue2, W_UL, end, W, B, Cli.getDork(cmd_interpreter), Cli.setPage(cmd_interpreter_wp), W, end))
                                    history.append(
                                        cmd_interpreter_wp_page_output)
                                    if run_regx.search(cmd_interpreter_wp_page_output):
                                        print('\n')
                                        from modules.dorksEngine import Dorks as D
                                        D.searchengine(Cli.getDork(cmd_interpreter), headers, Cli.setOutput(
                                            cmd_interpreter_wp), Cli.setPage(cmd_interpreter_wp))
                                    if back_regx.search(cmd_interpreter_wp_page_output):
                                        break
                                    if help_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == '?':
                                        Helpers._dorks_setdork_page_output_help()
                                    if cls_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == 'cls':
                                        Cli._clearscreen()
                                    if exit_regx.search(cmd_interpreter_wp_page_output) or cmd_interpreter_wp_page_output == 'quit':
                                        sys.exit()
                                    if history_regx.search(cmd_interpreter_wp_page_output):
                                        for i in range(len(history)):
                                            print(" %s  %s" %
                                                  (i+1, history[i-1]))
                                    if exec_regx.search(cmd_interpreter_wp_page_output):
                                        Cli._exec(
                                            cmd_interpreter_wp_page_output)
                                    if var_regx.search(cmd_interpreter_wp_page_output):
                                        Cli.dork_variable(Cli.getDork(cmd_interpreter), Cli.setOutput(
                                            cmd_interpreter_wp), Cli.setPage(cmd_interpreter_wp))

                            if run_regx.search(cmd_interpreter_wp_page):
                                print('\n')
                                from modules.dorksEngine import Dorks as D
                                D.searchengine(Cli.getDork(
                                    cmd_interpreter), headers, output_dir, Cli.setPage(cmd_interpreter_wp))
                            if back_regx.search(cmd_interpreter_wp_page):
                                break
                            if help_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == '?':
                                Helpers._dorks_setdork_page_help()
                            if cls_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == 'cls':
                                Cli._clearscreen()
                            if exit_regx.search(cmd_interpreter_wp_page) or cmd_interpreter_wp_page == 'quit':
                                sys.exit()
                            if history_regx.search(cmd_interpreter_wp_page):
                                for i in range(len(history)):
                                    print(" %s  %s" % (i+1, history[i-1]))
                            if exec_regx.search(cmd_interpreter_wp_page):
                                Cli._exec(cmd_interpreter_wp_page)
                            if var_regx.search(cmd_interpreter_wp_page):
                                Cli.dork_variable(Cli.getDork(
                                    cmd_interpreter), output_dir, Cli.setPage(cmd_interpreter_wp))

                    '''SET OUTPUT VARIABLE.'''

                    if output.search(cmd_interpreter_wp):
                        while True:
                            Cli.autoComplete_Output()
                            cmd_interpreter_wp_output = input("%s%svulnx%s%s (%sDorks-%s%s)> %s" % (
                                bannerblue2, W_UL, end, W, B, Cli.getDork(cmd_interpreter), W, end))
                            history.append(cmd_interpreter_wp_output)
                            if run_regx.search(cmd_interpreter_wp_output):
                                print('\n')
                                from modules.dorksEngine import Dorks as D
                                D.searchengine(Cli.getDork(cmd_interpreter), headers, Cli.setOutput(
                                    cmd_interpreter_wp), numberpage)
                            if back_regx.search(cmd_interpreter_wp_output):
                                break
                            if cls_regx.search(cmd_interpreter_wp_output) or cmd_interpreter_wp_output == 'cls':
                                Cli._clearscreen()
                            if exit_regx.search(cmd_interpreter_wp_output) or cmd_interpreter_wp_output == 'quit':
                                sys.exit()
                            if help_regx.search(cmd_interpreter_wp_output) or cmd_interpreter_wp_output == '?':
                                Helpers._dorks_setdork_output_help()
                            if history_regx.search(cmd_interpreter_wp_output):
                                for i in range(len(history)):
                                    print(" %s  %s" % (i+1, history[i-1]))
                            if exec_regx.search(cmd_interpreter_wp_output):
                                Cli._exec(cmd_interpreter_wp_output)
                            if var_regx.search(cmd_interpreter_wp_output):
                                Cli.dork_variable(Cli.getDork(cmd_interpreter), Cli.setOutput(
                                    cmd_interpreter_wp), numberpage)

                    if run_regx.search(cmd_interpreter_wp):
                        print('\n')
                        from modules.dorksEngine import Dorks as D
                        D.searchengine(Cli.getDork(cmd_interpreter),
                                       headers, output_dir, numberpage)
                    if back_regx.search(cmd_interpreter_wp):
                        break
                    if help_regx.search(cmd_interpreter_wp) or cmd_interpreter_wp == '?':
                        Helpers._dorks_setdork_help()
                    if cls_regx.search(cmd_interpreter_wp) or cmd_interpreter_wp == 'cls':
                        Cli._clearscreen()
                    if exit_regx.search(cmd_interpreter_wp) or cmd_interpreter_wp == 'quit':
                        sys.exit()
                    if history_regx.search(cmd_interpreter_wp):
                        for i in range(len(history)):
                            print(" %s  %s" % (i+1, history[i-1]))
                    if exec_regx.search(cmd_interpreter_wp):
                        Cli._exec(cmd_interpreter_wp)
                    if var_regx.search(cmd_interpreter_wp):
                        Cli.dork_variable(Cli.getDork(
                            cmd_interpreter), output_dir, numberpage)

    def send_commands(self, cmd):
        while True:
            Cli.autoComplete_Global()
            cmd = input("%s%svulnx%s > " % (bannerblue2, W_UL, end))
            history.append(cmd)
            if url_regx.search(cmd):
                # url session
                while True:
                    cmd_interpreter = input("%s%svulnx%s%s target(%s%s%s) > %s" % (
                        bannerblue2, W_UL, end, W, R, self.getUrl(cmd), W, end))
                    history.append(cmd_interpreter)
                    if cmd_interpreter == 'back':
                        break
                    elif cmd_interpreter == 'run exploit':
                        print('\n%s[*]%s Running exploits..' % (B, end))
                        root = self.getUrl(cmd)
                        if root.startswith('http'):
                            url_root = root
                        else:
                            url_root = 'http://'+url_root
                        self.__runExploits(url_root, headers)
                    elif help_regx.search(cmd_interpreter) or cmd_interpreter == '?':
                        Helpers._url_action_help()
                    elif exit_regx.search(cmd_interpreter) or cmd_interpreter == 'quit':
                        sys.exit()
                    else:
                        print("use (help) (?) to show man commands.")
            elif dork_regx.search(cmd):
                # dork session
                self.setdorkCLI(cmd)
            elif exit_regx.search(cmd) or cmd == 'quit':
                sys.exit()
            elif help_regx.search(cmd) or cmd == '?':
                Helpers._general_help()
            elif cls_regx.search(cmd) or cmd == 'cls':
                Cli._clearscreen()
            elif history_regx.search(cmd):
                for i in range(len(history)):
                    print(" %s  %s" % (i+1, history[i-1]))
            elif exec_regx.search(cmd):
                Cli._exec(cmd)
            elif var_regx.search(cmd):
                Cli.global_variables(dorkname, output_dir,
                                     numberpage, url, timeout)
            else:
                print("use (help) (?) to show man commands.")
