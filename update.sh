red   = "\e[0;31m"
green = "\e[0;32m"
off   = "\e[0m"
function banner(){
    echo -e "===== VULNX INSTALL ====="
}
function termuxOS() {
  echo -e "$red [$green+$red]$Cleaning Up Old Directories ...";
  rm -r "/data/data/com.termux/files/usr/share/vulnx"
  echo -e "$red [$green+$red]$off Installing ...";
  git clone https://github.com/anouarbensaad/vulnx "/data/data/com.termux/files/usr/share/vulnx";
  rm -r "/data/data/com.termux/files/usr/share/vulnx/config"
  if [[ -d "/data/data/com.termux/files/usr/share/vulnx" ]]; then
    echo -e "$red [$green+$red]$off Tool Successfully Updated And Will Start In 5s!";
    echo -e "$red [$green+$red]$off You can execute tool by typing vulnx"
    sleep 5;
    vulnx
  else
    echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
  fi 
}

function debianOS() {
  echo -e "$red [$green+$red]$off Cleaning Up Old Directories ...";
  sudo rm -r "/usr/share/vulnx"
  echo -e "$red [$green+$red]$off Installing ...";
  sudo git clone https://github.com/anouarbensaad/vulnx "/usr/share/vulnx";
  sudo rm -r "/usr/share/vulnx/config"
  if [[ -d "/usr/share/vulnx" ]]; then
    echo -e "$red [$green+$red]$off Tool Successfully Updated And Will Start In 5s!";
    echo -e "$red [$green+$red]$off You can execute tool by typing vulnx";
    sleep 5;
    vulnx
  else
    echo -e "$red [$green✘$red]$off Tool Cannot Be Installed On Your System! Use It As Portable !";
    exit
  fi 
}
if [[ -d "/data/data/com.termux/files/usr/" ]]; then
banner
echo -e "$red [$green+$red]$off vulnx Will Be Installed In Your System";
termuxOS
elif [ -d "/usr/bin/" ];then
banner
echo -e "$red [$green+$red]$off vulnx Will Be Installed In Your System";
debianOS
fi
