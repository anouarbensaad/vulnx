<h1 align="center">
  <br>
  <a href="https://github.com/anouarbensaad/VulnX"><img src="https://i.ibb.co/ZxxFqxQ/vxv2.png" alt="VulnX"></a>
  <br>
  VulnX
  <br>
</h1>

<h4 align="center">Vulnx 🕷️ is An Intelligent Bot Auto Shell Injector that detects vulnerabilities in multiple types of Cms </h4>

<p align="center">
   <a href="https://github.com/anouarbensaad/vulnx/releases">
    <img src="https://img.shields.io/github/release/anouarbensaad/vulnx.svg">
  </a>

  <a href="https://pypi.org/project/vulnx/">
    <img src="https://img.shields.io/badge/pypi-vulnx-red.svg">
  </a>

  <a href="https://github.com/anouarbensaad/vulnx/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed/anouarbensaad/vulnx.svg">
  </a>
  <a href="https://travis-ci.com/anouarbensaad/vulnx">
    <img src="https://img.shields.io/travis/com/anouarbensaad/vulnx.svg">
  </a>
</p>

![Screenshot from 2019-06-19 05-22-04](https://user-images.githubusercontent.com/23563528/59736664-7c2fed00-9252-11e9-936d-53ea02628711.png)

https://github.com/anouarbensaad/vulnx/archive/master.zip
<p align="center">
  <a href="https://github.com/anouarbensaad/vulnx/wiki">VulnX Wiki</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Usage">How To Use</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Compatibility-&-Dependencies">Compatibility</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Vulnx-Library">Library</a> •
</p>

**Vulnx** is An Intelligent Bot Auto [Shell Injector](https://github.com/anouarbensaad/vulnx/wiki/Usage#run-exploits) that detects vulnerabilities in multiple types of Cms, fast cms detection,informations gathering and vulnerabilitie Scanning of the target like subdomains, ipaddresses, country, org, timezone, region, ans and more ...

Instead of injecting each and every shell manually like all the other tools do, VulnX analyses the target website checking the presence of a vulnerabilitie if so the shell will be Injected.searching urls with [dorks](https://github.com/anouarbensaad/vulnx/wiki/Usage#searching-dorks) Tool. 

-------------------------------------

### _🕷️ Features_

- Detects cms (wordpress, joomla, prestashop, drupal, opencart, magento, lokomedia)
- Target informations gatherings
- Target Subdomains gathering
- Multi-threading on demand
- Checks for vulnerabilities
- Auto shell injector
- Exploit dork searcher
- [`Ports Scan`](https://user-images.githubusercontent.com/23563528/58365946-40a83a00-7ec3-11e9-87c5-055ed67109b7.jpg) High Level
- [`Dns`](https://user-images.githubusercontent.com/23563528/58365784-09388e00-7ec1-11e9-8a05-e71fa39f146d.png)-Servers Dump
- Input multiple target to scan.
- Dorks Listing by Name& by ExploitName.
- Export multiple target from Dorks into a logfile.

-------------------------------------


### _🕷️ DNS-Map-Results_

To do this,run a scan with the --dns flag and -d for subdomains.
To generate a map of isetso.rnu.tn, you can run the command 
`vulnx -u isetso.rnu.tn --dns -d --output $PATH`in a new terminal.

`$PATH` : Where the graphs results will be stored.

![vokoscreen-2019-06-19_05-44-07](https://user-images.githubusercontent.com/23563528/59737395-696ae780-9255-11e9-9e09-26416de89bee.gif)


Let's generates an image displaying target Subdomains,MX & DNS data.


![demo](https://i.ibb.co/WfdhvWC/isetso-rnu-tn.png)

-------------------------------------

### _🕷️ Exploits_
<h1 align="center">
<a href="https://github.com/anouarbensaad/VulnX"><img src="https://user-images.githubusercontent.com/23563528/59737042-06c51c00-9254-11e9-87f8-876b33c87be1.gif" alt="Exploits Running"></a>
</h1>

##### Joomla
- [x] [Com Jce            ]('#')
- [x] [Com Jwallpapers    ]('#')
- [x] [Com Jdownloads     ]('#')
- [x] [Com Jdownloads2    ]('#')
- [x] [Com Weblinks       ]('#')
- [x] [Com Fabrik         ]('#')
- [x] [Com Fabrik2        ]('#')
- [x] [Com Jdownloads Index]('#')
- [x] [Com Foxcontact     ]('#')
- [x] [Com Blog           ]('#')
- [x] [Com Users          ]('#')
- [x] [Com Ads Manager    ]('#')
- [x] [Com Sexycontactform]('#')
- [x] [Com Media          ]('#')
- [x] [Mod_simplefileupload]('#')
- [x] [Com Facileforms    ]('#')
- [x] [Com Facileforms    ]('#')
- [x] [Com extplorer      ]('#')

##### Wordpress
- [x] [Simple Ads Manager   ](https://www.exploit-db.com/exploits/36614)
- [x] [InBoundio Marketing  ](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_inboundio_marketing_file_upload) 
- [x] [WPshop eCommerce     ](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_wpshop_ecommerce_file_upload)
- [x] [Synoptic             ](https://cxsecurity.com/issue/WLB-2017030099) 
- [x] [Showbiz Pro          ](https://www.exploit-db.com/exploits/35385) 
- [x] [Job Manager          ](https://www.exploit-db.com/exploits/45031) 
- [x] [Formcraft            ](https://www.exploit-db.com/exploits/30002)
- [x] [PowerZoom            ](http://www.exploit4arab.org/exploits/399)
- [x] [Download Manager     ](https://www.exploit-db.com/exploits/35533)
- [x] [CherryFramework      ](https://www.exploit-db.com/exploits/45896)
- [x] [Catpro               ](https://vulners.com/zdt/1337DAY-ID-20256)
- [x] [Blaze SlideShow      ](https://0day.today/exploits/18500)
- [x] [Wysija-Newsletters   ](https://www.exploit-db.com/exploits/33991)

##### Drupal
- [ ] [Add Admin            ]('#')
- [ ] [Drupal BruteForcer   ]('#')
- [ ] [Drupal Geddon2       ]('#')

##### PrestaShop
- [x] [attributewizardpro   ]('#')
- [x] [columnadverts        ]('#')
- [ ] [soopamobile          ]('#')
- [x] [pk_flexmenu          ]('#')
- [x] [pk_vertflexmenu      ]('#')
- [x] [nvn_export_orders    ]('#')
- [x] [megamenu             ]('#')
- [x] [tdpsthemeoptionpanel ]('#')
- [ ] [psmodthemeoptionpanel]('#')
- [x] [masseditproduct      ]('#')
- [ ] [blocktestimonial     ]('#')
- [x] [soopabanners         ]('#')
- [x] [Vtermslideshow       ]('#')
- [x] [simpleslideshow      ]('#')
- [x] [productpageadverts   ]('#')
- [x] [homepageadvertise    ]('#')
- [ ] [homepageadvertise2   ]('#')
- [x] [jro_homepageadvertise]('#')
- [x] [advancedslider       ]('#')
- [x] [cartabandonmentpro   ]('#')
- [x] [cartabandonmentproOld]('#')
- [x] [videostab            ]('#')
- [x] [wg24themeadministration]('#')
- [x] [fieldvmegamenu       ]('#')
- [x] [wdoptionpanel        ]('#')

##### Opencart
- [ ] [Opencart BruteForce]('#')


-------------------------------------

### _🕷️ VulnxMode_ 
`NEW`
vulnx now have an interactive mode.
***URLSET***

![vulnxmode_url](https://user-images.githubusercontent.com/23563528/68983791-fddd7400-080c-11ea-8e2b-c463a2c8f8c5.png)

***DORKSET***

![vulnxmode_dorks](https://user-images.githubusercontent.com/23563528/68985825-bf01eb00-0819-11ea-83ea-3db022b1d645.png)

-------------------------------------



### _🕷️ Available command line options_
[`READ VULNX WIKI`](https://github.com/anouarbensaad/vulnx/wiki/Usage)

    usage: vulnx [options]
    
      -u --url              url target
      -D --dorks            search webs with dorks
      -o --output           specify output directory
      -t --timeout          http requests timeout
      -c --cms-info         search cms info[themes,plugins,user,version..]
      -e --exploit          searching vulnerability & run exploits
      -w --web-info         web informations gathering
      -d --domain-info      subdomains informations gathering
      -l, --dork-list       list names of dorks exploits
      -n, --number-page     number page of search engine(Google)
      -p, --ports           ports to scan
      -i, --input           specify domains to scan from an input file 
      --threads             number of threads
      --dns                 dns informations gathering

-------------------------------------

### _🕷️ Docker_

VulnX in DOCKER !!.

```bash
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ docker build -t vulnx ./docker/
$ docker run -it --name vulnx vulnx:latest -u http://example.com
```

run vulnx container in interactive mode


![vokoscreen-2019-06-23_11-53-20](https://user-images.githubusercontent.com/23563528/59975226-a31d5480-95ad-11e9-8252-ddd8291cbee4.gif)


to view logfiles mount it in a volume like so:

```bash
$ docker run -it --name vulnx -v "$PWD/logs:/VulnX/logs" vulnx:latest -u http://example.com
```

change the [mounting directory](https://github.com/anouarbensaad/vulnx/blob/master/docker/Dockerfile#L46)..

```Dockerfile
VOLUME [ "$PATH" ]
```

-------------------------------------

### _🕷️ Install vulnx on Ubuntu_


```bash
$ git clone https://github.com/anouarbensaad/vulnx.git
$ cd VulnX
$ chmod +x install.sh
$ ./install.sh
```
Now run `vulnx`

![vokoscreen-2019-07-05_03-59-48](https://user-images.githubusercontent.com/23563528/60695392-7a645b80-9ed9-11e9-94fb-f6025594a9e3.gif)


### _🕷️ Install vulnx on Termux_

```BASH
$ pkg update
$ pkg install -y git
$ git clone http://github.com/anouarbensaad/vulnx
$ cd vulnx
$ chmod +x install.sh
$ ./install.sh
```
[**CLICK HERE TO SHOW THE RESULT**](https://user-images.githubusercontent.com/23563528/58364091-98847800-7ea6-11e9-9a9a-c27717e4dda1.png)


### _🕷️ Install vulnx in Windows_

- [click here](https://github.com/anouarbensaad/vulnx/archive/master.zip) to download vulnx
- download and install python3
- unzip **vulnx-master.zip** in ***c:/***
- open the command prompt **cmd**.
```
> cd c:/vulnx-master
> python vulnx.py
```

-------------------------------------

##### example command with options : settimeout=3 , cms-gathering = all , -d subdomains-gathering , run --exploits
`vulnx -u http://example.com --timeout 3 -c all -d -w --exploit` 

##### example command for searching dorks : -D or --dorks , -l --list-dorks 
`vulnx --list-dorks`
return table of exploits name.
`vulnx -D blaze`
return urls found with blaze dork

-------------------------------------

### _🕷️ Versions_
- [v1.9](https://github.com/anouarbensaad/vulnx/releases/tag/v1.9)
- [v1.8](https://github.com/anouarbensaad/vulnx/releases/tag/v1.8)
- [v1.7](https://github.com/anouarbensaad/vulnx/releases/tag/v1.7)
- [v1.6](https://github.com/anouarbensaad/vulnx/releases/tag/v1.6)
- [v1.5](https://github.com/anouarbensaad/vulnx/releases/tag/v1.5)
- [v1.4](https://github.com/anouarbensaad/vulnx/releases/tag/v1.4)
- [v1.3](https://github.com/anouarbensaad/vulnx/releases/tag/v1.3)
- [v1.2](https://github.com/anouarbensaad/vulnx/releases/tag/v1.2)
- [v1.1](https://github.com/anouarbensaad/vulnx/releases/tag/v1.1)

-------------------------------------

### :warning: Warning!

***I Am Not Responsible of any Illegal Use***

-------------------------------------

### _🕷️ Contribution & License_

You can contribute in following ways:

- [Report bugs & add issues](https://github.com/anouarbensaad/VulnX/issues/new)
- Search for new vulnerability
- Develop plugins
- Searching Exploits
- Give suggestions **(Ideas)** to make it better

Do you want to have a conversation in private? email me : Bensaad.tig@gmail.com

***VulnX*** is licensed under [GPL-3.0 License](https://github.com/anouarbensaad/VulnX/blob/master/LICENSE)
