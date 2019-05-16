<h1 align="center">
  <br>
  <a href="https://github.com/anouarbensaad/VulnX"><img src="https://i.ibb.co/kXW18B6/vulnxsmall.png" alt="VulnX"></a>
  <br>
  VulnX
  <br>
</h1>

<h4 align="center">VulnX 🕷️ CMS-Detector and Vulnerability Scanner & exec automatic exploit process.</h4>

![demo](https://i.ibb.co/yQP80Ss/New-Project-2.jpg)

<p align="center">
  <a href="#">VulnX Wiki</a> •
  <a href="#">How To Use</a> •
  <a href="#">Compatibility</a> •
  <a href="#">VulnX Library</a> •
</p>

### Exploits

#### Joomla


#### Wordpress

[Wysija-Newsletters](https://www.exploit-db.com/exploits/33991)
[Simple Ads Manager](https://www.exploit-db.com/exploits/36614)
[InBoundio Marketing](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_inboundio_marketing_file_upload)
[WPshop eCommerce](https://www.rapid7.com/db/modules/exploit/unix/webapp/wp_wpshop_ecommerce_file_upload)
[Synoptic](https://cxsecurity.com/issue/WLB-2017030099)
[Showbiz Pro](https://www.exploit-db.com/exploits/35385)
[Job Manager](https://www.exploit-db.com/exploits/45031)
[Formcraft](https://www.exploit-db.com/exploits/30002)
[PowerZoom](http://www.exploit4arab.org/exploits/399)
[Download Manager](https://www.exploit-db.com/exploits/35533)
[CherryFramework](https://www.exploit-db.com/exploits/45896)
[Catpro](https://vulners.com/zdt/1337DAY-ID-20256)
[Blaze SlideShow](https://0day.today/exploits/18500)


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


** VulnX is licensed under [MIT License](https://github.com/anouarbensaad/VulnX/blob/master/LICENSE) **