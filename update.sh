red="\e[0;31m"
green="\e[0;32m"
off="\e[0m"
function banner(){
    echo "nothing"
}
function update() {
echo -e "$red [$green+$red]$off Cleaning Up Old Directories ...";
  sudo rm -r "/usr/share/VulnX"
  echo -e "$red [$green+$red]$off Installing ...";
 sudo git clone https://github.com/anouarbensaad/VulnX "/usr/share/VulnX";
  sudo rm -r "/usr/share/VulnX/conf"

if [ -d "/usr/share/VulnX" ] ;
then
echo -e "$red [$green+$red]$off Tool Successfully Updated And Will Start In 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing VulnX";
sleep 5;
VulnX
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi 
}

if [ -d "/usr/bin/" ];then
banner
echo -e "$red [$green+$red]$off VulnX Will Be Installed In Your System";
update
fi