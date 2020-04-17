'''    
if dorks:
        headers = {
            'host': 'google.com',
            'User-Agent': random_UserAgent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive', }
        from modules.dorksEngine import Dorks as D
        D.searchengine(dorks, headers, output_dir, numberpage)
    if dorkslist == 'all':
        from modules.dorksEngine import DorkList as DL
        DL.dorkslist()
    if dorkslist == 'wordpress':
        from modules.dorksEngine import DorkList as DL
        DL.wp_dorkTable()
    if dorkslist == 'joomla':
        from modules.dorksEngine import DorkList as DL
        DL.joo_dorkTable()
    if dorkslist == 'prestashop':
        from modules.dorksEngine import DorkList as DL
        DL.ps_dorkTable()
    if dorkslist == 'lokomedia':
        from modules.dorksEngine import DorkList as DL
        DL.loko_dorkTable()
    if dorkslist == 'drupal':
        from modules.dorksEngine import DorkList as DL
        DL.dru_dorkTable()
    if cli:
        from cli import Cli
        cli = Cli()
        cli.send_commands("")
'''