#!/bin/bash

red="\e[0;31m"
blue="\e[0;94m"
green="\e[0;32m"
off="\e[0m"

#vulnx install function for Android. termux
function banner(){
    echo -e "===== VULNX INSTALL ====="
}

function termuxOS() {
    echo -e "$red [$green+$red]$off Installing Python ...";
    pkg install python
    echo -e "$red [$green+$red]$off Installing Packages ...";
    pip install -r ./requirements.txt
    echo -e "$red [$green+$red]$off Checking directories ..."
    if [ -e "/data/data/com.termux/files/usr/share/vulnx" ]; then
        echo -e "$red [$green+$red]$off A previous installation was found Do you want to replace it? [Y/n]: "
        read replace
        if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
            rm -r "/data/data/com.termux/files/usr/share/vulnx"
            rm "/data/data/com.termux/files/usr/bin/vulnx"
        else
            echo -e "$red [$green✘$red]$off If You Want To Install You Must Remove Previous Installations";
            echo -e "$red [$green✘$red]$off Installation Failed";
            exit
        fi
    fi
    echo -e "$red [$green+$red]$off Installing ...";
    mkdir "/data/data/com.termux/files/usr/share/vulnx" 
    cp "vulnx.py" "/data/data/com.termux/files/usr/share/vulnx"
    cp "install.sh" "/data/data/com.termux/files/usr/share/vulnx"
    cp "update.sh" "/data/data/com.termux/files/usr/share/vulnx"
    cp -r "./common" "/data/data/com.termux/files/usr/share/vulnx"
    cp -r "./modules" "/data/data/com.termux/files/usr/share/vulnx"
    cp -r "./shell" "/data/data/com.termux/files/usr/share/vulnx"
    chmod +x /data/data/com.termux/files/usr/share/vulnx/update.sh
    echo -e "$red [$green+$red]$off Creating Symbolic Link ...";
    echo "#!/data/data/com.termux/files/usr/bin/bash 
    python /data/data/com.termux/files/usr/share/vulnx/vulnx.py" '${1+"$@"}' > "vulnx";
    cp "vulnx" "/data/data/com.termux/files/usr/bin"
    chmod +x "/data/data/com.termux/files/usr/bin/vulnx"
    rm "vulnx";
    if [ -d "/data/data/com.termux/files/usr/share/vulnx" ] ;
    then
        echo -e "$red [$green+$red]$off Tool successfully installed and will start in 5s!";
        echo -e "$red [$green+$red]$off You can execute tool by typing vulnx"
        sleep 5;
        vulnx
    else
        echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
        exit
    fi
}

#vulnx install function for debian operating system. linux.
function debianOS(){
    echo -e "$red [$green+$red]$off Installing python3... ";
    sudo apt-get install -y python3
    pip install -r ./requirements.txt
    echo -e "$red [$green+$red]$off Checking directories... "
    if [ -d "/usr/share/VulnX" ]; then
        echo -e "$red [$green+$red]$off A Directory VulnX Was Found! Do You Want To Replace It? [Y/n]:" ;
        read replace
        if [ "$replace" == "y" ] || [ "$replace" == "Y" ] || [ -z "$replace" ]; then
            sudo rm -r "/usr/share/vulnx"
            sudo rm "/usr/share/icons/vulnxicon.png"
            sudo rm "/usr/share/applications/vulnx.desktop"
            sudo rm "/usr/local/bin/vulnx"
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
    sudo cp -r "./common" "/usr/share/vulnx/"
    sudo cp -r "./modules" "/usr/share/vulnx/"
    sudo cp -r "./shell" "/usr/share/vulnx/"
    sudo chmod +x /usr/share/vulnx/update.sh
    sudo cp "vulnx.py" "/usr/share/vulnx"
    sudo cp "bin/vulnxicon.png" "/usr/share/icons"
    sudo cp "bin/vulnx.desktop" "/usr/share/applications"
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
#main
if [ -d "/data/data/com.termux/files/usr/" ]; then
    banner
    echo -e "$red [$green+$red]$off Vulnx Will Be Installed In Your System";
    termuxOS
elif [ -d "/usr/bin/" ];then
    banner
    echo -e "$red [$green+$red]$off Vulnx Will Be Installed In Your System";
    debianOS
else
    echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
fi
