#!/bin/bash

red="\e[0;31m"
green="\e[0;32m"
off="\e[0m"

function banner(){
    echo "nothing"
}
function install(){
    echo -e "$red [$green+$red]$off Installing Python ...";
    sudo apt-get install -y python3
    echo -e "$red [$green+$red]$off Checking directories..."
if [ -d "/usr/share/VulnX" ]; then
    echo -e "$red [$green+$red]$off A Directory VulnX Was Found! Do You Want To Replace It? [Y/n]:" ;
    read replace
    if [ "$replace" = "y" ]; then
      sudo rm -r "/usr/share/VulnX"
      sudo rm "/usr/share/icons/VulnX.png"
      sudo rm "/usr/share/applications/VulnX.desktop"
      sudo rm "/usr/local/bin/VulnX"

else
echo -e "$red [$green✘$red]$off If You Want To Install You Must Remove Previous Installations";
echo -e "$red [$green✘$red]$off Installation Failed";
        exit
    fi
fi 

echo -e "$red [$green+$red]$off Installing ...";
echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
echo -e "#!/bin/bash
python3 /usr/share/VulnX/vulnx.py" '${1+"$@"}' > "VulnX";
    chmod +x "VulnX";
    sudo mkdir "/usr/share/VulnX"
    sudo cp "install.sh" "/usr/share/VulnX"
    sudo cp "update.sh" "/usr/share/VulnX"
    sudo chmod +x /usr/share/VulnX/update.sh
    sudo cp "VulnX.py" "/usr/share/VulnX"
    sudo cp "conf/vulnxicon.png" "/usr/share/icons"
    sudo cp "conf/vulnx.desktop" "/usr/share/applications"
    sudo cp "vulnx" "/usr/local/bin/"
    rm "vulnx";

if [ -d "/usr/share/VulnX" ] ;
then
echo -e "$red [$green+$red]$off Tool Successfully Installed And Will Start In 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing VulnX"
sleep 5;
VulnX
else
echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi 
}
if [ -d "/usr/bin/" ];then
banner
echo -e "$red [$green+$red]$off Th3inspector Will Be Installed In Your System";
linux
fi