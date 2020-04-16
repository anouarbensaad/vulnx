#### v2.0
- Add Module to get the operating system of target and web server name & version.
#### v1.9
- Add Vulnx−Mode `interactive mode`
- Add Command Line Interface Class `cli`
- Add Dork Functionnality to Vulnx−Mode
- Fix DNSDUMP Functionnality

#### v1.8
- Remove pip & rename conf to config to excute update without problem.
- Fix port arg to give port to scan.
- CI : Change pip package. 
- Docker : change pip package.
- Remove the ENV Variable.

#### v1.7
- add documentation vulnx for windows.
- add minor changes in dockerfile.
- add documentation for developper used vulnx library
- fix regEx in prestashop version.
- error handling and ignore warnings.

#### v1.6
- Added Payloads.
- Added PS Exploits
- Added Joomla Exploits
- Fix Issues
- Added Dorks Output {logs}
- Scan Multiple targets.
- Docker Using User. {`Fix Permissions`}
- Fix .travis {`CI`: Run tests after merge or pull requests}
- Listing Dorks {list `ps` , `joo` , `wp` , `dru`} exploits manually

#### v1.5
- Added 8 Prestashop Exploits.
- Added `Windows` & `MacOS` Comptability
- Fixed a few bugs
- Added vulnx to Docker from Ubuntu Image.

#### v1.4
- Fix parsing url
- Fix Robot Detected when you searching for dorks.
- Deserialize `json` data from dnsdumpster
- Added `Bot` Automate Scan
- Fix Modules Name
- Exports `Dorks` Search into file

#### v1.3
- Added vulnx to `PyPi`
- Added a `ports` scanner **plugin**.
- Improve `dorks` google searching. 
- Added `termux` compatibility & fix pip package.

#### v1.2
- Use of `ThreadPoolExecutor` for more speed
- Added pip packages.
- Added `travis.yml` continuous integration
- Added shields to README.MD

#### v1.1
- Added `--timeout` , `--exploits` , `--cms-info` , `--domains-info` ,  options
- Added `Dorks` list
- Fixed `Dork Search`
- Added `wordpress`, `joomla` ,`prestashop`, `drupal` , `lokomedia` , `magento` , `opencart`  CMS DETECT.
- Disabled `SSL` Warning
- Added `WP-Exploits`
- Fixed `Dockerfile`
