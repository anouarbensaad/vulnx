red="\e[0;31m"
green="\e[0;32m"
off="\e[0m"
function banner(){
    echo "nothing"
}
function update() {
echo -e "$red [$green+$red]$off Cleaning Up Old Directories ...";
  sudo rm -r "/usr/share/vulnx"
  echo -e "$red [$green+$red]$off Installing ...";
 sudo git clone https://github.com/anouarbensaad/vulnx "/usr/share/vulnx";
  sudo rm -r "/usr/share/vulnx/conf"

if [ -d "/usr/share/vulnx" ] ;
then
echo -e "$red [$green+$red]$off Tool Successfully Updated And Will Start In 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing vulnx";
sleep 5;
vulnx
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi 
}

if [ -d "/usr/bin/" ];then
banner
echo -e "$red [$green+$red]$off vulnx Will Be Installed In Your System";
update
fi