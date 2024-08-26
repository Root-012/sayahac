#!/bin/bash
# Bash Script for install Fsociety tools
# Must run to install tool

clear
echo "

░██████╗░█████╗░██╗░░░██╗░█████╗░██╗░░██╗░█████╗░░█████╗░
██╔════╝██╔══██╗╚██╗░██╔╝██╔══██╗██║░░██║██╔══██╗██╔══██╗
╚█████╗░███████║░╚████╔╝░███████║███████║███████║██║░░╚═╝
░╚═══██╗██╔══██║░░╚██╔╝░░██╔══██║██╔══██║██╔══██║██║░░██╗
██████╔╝██║░░██║░░░██║░░░██║░░██║██║░░██║██║░░██║╚█████╔╝
╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░

██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░███████╗██████╗░
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░██╔════╝██╔══██╗
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░█████╗░░██████╔╝
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗███████╗██║░░██║
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝
";

sudo chmod +x uninstall

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/sayahac"
    BIN_DIR="$PREFIX/bin/"
    BASH_PATH="$PREFIX/bin/bash"
    TERMUX=true

    pkg install -y git python2
elif [ "$(uname)" = "Darwin" ]; then
    INSTALL_DIR="/usr/local/sayahac"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false
else
    INSTALL_DIR="$HOME/.sayahac"
    BIN_DIR="/usr/local/bin/"
    BASH_PATH="/bin/bash"
    TERMUX=false

    sudo apt-get install -y git python2.7
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[◉] A directory sayahac was found! Do you want to replace it? [Y/n]:" ;
    read -r mama
    if [ "$mama" = "y" ]; then
        if [ "$TERMUX" = true ]; then
            rm -rf "$INSTALL_DIR"
            rm "$BIN_DIR/sayahac*"
        else
            sudo rm -rf "$INSTALL_DIR"
            sudo rm "$BIN_DIR/sayahac*"
        fi
    else
        echo "[✘] If you want to install you must remove previous installations [✘] ";
        echo "[✘] Installation failed! [✘] ";
        exit
    fi
fi
echo "[✔] Cleaning up old directories...";
if [ -d "$ETC_DIR/Root-012" ]; then
    echo "$DIR_FOUND_TEXT"
    if [ "$TERMUX" = true ]; then
        rm -rf "$ETC_DIR/Root-012"
    else
        sudo rm -rf "$ETC_DIR/Root-012"
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone --depth=1 https://github.com/Root-012/sayahac "$INSTALL_DIR";
echo "#!$BASH_PATH
python $INSTALL_DIR/sayahac.py" "${1+"$@"}" > "$INSTALL_DIR/sayahac";
chmod +x "$INSTALL_DIR/sayahac";
if [ "$TERMUX" = true ]; then
    cp "$INSTALL_DIR/sayahac" "$BIN_DIR"
    cp "$INSTALL_DIR/sayahac.cfg" "$BIN_DIR"
else
    sudo cp "$INSTALL_DIR/sayahac" "$BIN_DIR"
    sudo cp "$INSTALL_DIR/sayahac.cfg" "$BIN_DIR"
fi
rm "$INSTALL_DIR/sayahac";


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔] Tool installed successfully! [✔]";
    echo "";
    echo "[✔]====================================================================[✔]";
    echo "[✔]      All is done!! You can execute tool by typing sayahac  !       [✔]";
    echo "[✔]====================================================================[✔]";
    echo "";
else
    echo "[✘] Installation failed! [✘] ";
    exit
fi
