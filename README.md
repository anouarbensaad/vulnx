<h1 align="center">
  <br>
  <a href="https://github.com/anouarbensaad/VulnX"><img src="https://i.ibb.co/kXW18B6/vulnxsmall.png" alt="VulnX"></a>
  <br>
  VulnX
  <br>
</h1>

<h4 align="center">VulnX 🕷️ CMS-Detector and Vulnerability Scanner & exec automatic exploit process.</h4>

<p align="center">
  <a href="https://github.com/anouarbensaad/vulnx/releases">
    <img src="https://img.shields.io/github/release/anouarbensaad/vulnx.svg">
  </a>
  <a href="https://github.com/anouarbensaad/vulnx/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues-closed/anouarbensaad/vulnx.svg">
  </a>
  <a href="https://travis-ci.com/anouarbensaad/vulnx">
    <img src="https://img.shields.io/travis/com/anouarbensaad/vulnx.svg">
  </a>
</p>

![demo](https://i.ibb.co/wrZgjWn/New-Project-2.jpg)

<p align="center">
  <a href="https://github.com/anouarbensaad/vulnx/wiki">VulnX Wiki</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Usage">How To Use</a> •
  <a href="https://github.com/anouarbensaad/vulnx/wiki/Compatibility-&-Dependencies">Compatibility</a> •
</p>

### Exploits
<h1 align="center">
<a href="https://github.com/anouarbensaad/VulnX"><img src="https://user-images.githubusercontent.com/23563528/58003677-2e03be80-7ad9-11e9-9774-c69a38248c64.gif" alt="Exploits Running"></a>
</h1>

#### Joomla
- [ComJCE](#) `2018`

#### Wordpress
###### Plugins 
- [Simple Ads Manager](https://www.exploit-db.com/exploits/36614)
- [InBoundio Marketing](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_inboundio_marketing_file_upload) 
- [WPshop eCommerce](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_wpshop_ecommerce_file_upload)
- [Synoptic](https://cxsecurity.com/issue/WLB-2017030099) 
- [Showbiz Pro](https://www.exploit-db.com/exploits/35385) 
- [Job Manager](https://www.exploit-db.com/exploits/45031) 
- [Formcraft](https://www.exploit-db.com/exploits/30002)
- [PowerZoom](http://www.exploit4arab.org/exploits/399)
- [Download Manager](https://www.exploit-db.com/exploits/35533)
- [CherryFramework](https://www.exploit-db.com/exploits/45896)
- [Catpro](https://vulners.com/zdt/1337DAY-ID-20256)
- [Blaze SlideShow](https://0day.today/exploits/18500)
 ###### Themes
- [Wysija-Newsletters](https://www.exploit-db.com/exploits/33991)

#### Prestashop


#### Drupal 


### Docker

VulnX can be launched in docker.

```bash
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ docker build -t vulnx ./docker/
$ docker run -it --name vulnx vulnx:latest -u http://exemple.com
```

make a local volume to view the results into a logfile

```bash
$ docker run -it --name vulnx -v "$PWD/logs:/VulnX/logs" vulnx:latest -u http://exemple.com
```

### Install VulnX


```bash
$ git clone https://github.com/anouarbensaad/VulnX.git
$ cd VulnX
$ chmod + x install.sh
$ ./install.sh
```

### Contribution & License

You can contribute in following ways:

- [Report bugs & add issues](https://github.com/anouarbensaad/VulnX/issues/new)
- Search for new vulnerability

Do you want to have a conversation in private? email me : Bensaad.tig@gmail.com


***VulnX*** is licensed under [MIT License](https://github.com/anouarbensaad/VulnX/blob/master/LICENSE) **
