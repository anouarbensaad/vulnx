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
      sudo rm -r "/usr/share/vulnx"
      sudo rm "/usr/share/icons/vulnxicon.png"
      sudo rm "/usr/share/applications/vulnx.desktop"
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
python3 /usr/share/vulnx/vulnx.py" '${1+"$@"}' > "vulnx";
    chmod +x "vulnx";
    sudo mkdir "/usr/share/vulnx"
    sudo cp "install.sh" "/usr/share/vulnx"
    sudo cp "update.sh" "/usr/share/vulnx"
    sudo chmod +x /usr/share/vulnx/update.sh
    sudo cp "vulnx.py" "/usr/share/vulnx"
    sudo cp "conf/vulnxicon.png" "/usr/share/icons"
    sudo cp "conf/vulnx.desktop" "/usr/share/applications"
    sudo cp "vulnx" "/usr/local/bin/"
    rm "vulnx";

if [ -d "/usr/share/vulnx" ] ;
then
echo -e "$red [$green+$red]$off Tool Successfully Installed And Will Start In 5s!";
echo -e "$red [$green+$red]$off You can execute tool by typing vulnx"
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
install
fi
