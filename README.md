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

### CMS

#### Joomla


#### Wordpress


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
